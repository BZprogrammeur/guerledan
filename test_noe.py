import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'drivers-ddboat-v2'))

import imu9_driver_v2 as imudrv
imu = imudrv.Imu9IO()

xmag, ymag, zmag = imu.read_mag_raw()
xaccel, yaccel, zaccel = imu.read_accel_raw()
xgyro, ygyro, zgyro = imu.read_gyro_raw()

print(xmag, ymag, zmag '\n')
print(xaccel, yaccel, zaccel '\n')
print(xgyro, ygyro, zgyro'\n')
