import smbus
import time

class MPU6050:
    def __init__(self):
        # Initialize I2C bus and MPU6050 address
        self.bus = smbus.SMBus(1)
        self.address = 0x68
        
        # Wake up the MPU6050
        self.bus.write_byte_data(self.address, 0x6B, 0)

    def read_value(self, register):
        # Read 2 bytes and convert to signed value
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)
        value = (high << 8) | low
        
        if value > 32768:
            value -= 65536
        return value

    def get_readings(self):
        # Get accelerometer values (registers 0x3B-0x40)
        ax = self.read_value(0x3B) / 16384.0  # Convert to g
        ay = self.read_value(0x3D) / 16384.0
        az = self.read_value(0x3F) / 16384.0
        
        # Get gyroscope values (registers 0x43-0x48)
        gx = self.read_value(0x43) / 131.0  # Convert to degrees/sec
        gy = self.read_value(0x45) / 131.0
        gz = self.read_value(0x47) / 131.0
        
        return ax, ay, az, gx, gy, gz

def main():
    sensor = MPU6050()
    print("Reading MPU6050 values, press Ctrl+C to stop...")
    
    try:
        while True:
            ax, ay, az, gx, gy, gz = sensor.get_readings()
            print(f"\nAccel: x={ax:.1f}g, y={ay:.1f}g, z={az:.1f}g")
            print(f"Gyro: x={gx:.1f}°/s, y={gy:.1f}°/s, z={gz:.1f}°/s")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopped by user")

if __name__ == "__main__":
    main()
