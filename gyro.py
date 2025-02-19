import smbus
import math
import time

class MPU6050:
    # MPU6050 Registers and their Address
    DEVICE_ADDR = 0x68
    PWR_MGMT_1 = 0x6B
    SMPLRT_DIV = 0x19
    CONFIG = 0x1A
    GYRO_CONFIG = 0x1B
    ACCEL_CONFIG = 0x1C
    ACCEL_XOUT_H = 0x3B
    ACCEL_YOUT_H = 0x3D
    ACCEL_ZOUT_H = 0x3F
    GYRO_XOUT_H = 0x43
    GYRO_YOUT_H = 0x45
    GYRO_ZOUT_H = 0x47

    def __init__(self, bus_num=1):
        self.bus = smbus.SMBus(bus_num)
        # Wake up the MPU6050
        self.bus.write_byte_data(self.DEVICE_ADDR, self.PWR_MGMT_1, 0)

    def read_raw_data(self, addr):
        # Read raw 16-bit value
        high = self.bus.read_byte_data(self.DEVICE_ADDR, addr)
        low = self.bus.read_byte_data(self.DEVICE_ADDR, addr + 1)

        # Combine high and low bytes
        value = ((high << 8) | low)
        
        # Get signed value
        if value > 32768:
            value = value - 65536
        return value

    def get_data(self):
        # Read Accelerometer raw data
        acc_x = self.read_raw_data(self.ACCEL_XOUT_H)
        acc_y = self.read_raw_data(self.ACCEL_YOUT_H)
        acc_z = self.read_raw_data(self.ACCEL_ZOUT_H)

        # Read Gyroscope raw data
        gyro_x = self.read_raw_data(self.GYRO_XOUT_H)
        gyro_y = self.read_raw_data(self.GYRO_YOUT_H)
        gyro_z = self.read_raw_data(self.GYRO_ZOUT_H)

        # Full scale range +/- 250 degree/C as per sensitivity scale factor
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0

        Gx = gyro_x/131.0
        Gy = gyro_y/131.0
        Gz = gyro_z/131.0

        return {
            'acceleration': {'x': Ax, 'y': Ay, 'z': Az},
            'gyroscope': {'x': Gx, 'y': Gy, 'z': Gz}
        }

def main():
    mpu = MPU6050()
    print("Reading Data of Gyroscope and Accelerometer")

    try:
        while True:
            data = mpu.get_data()
            print("\nAccelerometer data")
            print(f"X = {data['acceleration']['x']:.2f}g")
            print(f"Y = {data['acceleration']['y']:.2f}g")
            print(f"Z = {data['acceleration']['z']:.2f}g")
            
            print("\nGyroscope data")
            print(f"X = {data['gyroscope']['x']:.2f}°/s")
            print(f"Y = {data['gyroscope']['y']:.2f}°/s")
            print(f"Z = {data['gyroscope']['z']:.2f}°/s")
            
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram stopped by user")

if __name__ == "__main__":
    main()
