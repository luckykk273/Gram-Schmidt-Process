from gram_schmidt_tools import *


if __name__ == '__main__':
    # Given the random reasonable values read from accelerometer
    accel = np.array([4.29, 5.34, 7.02])
    rot_g_to_imu = gram_schmidt_process(accel, plot=False)
    print('\nGlobal to IMU:')
    print(rot_g_to_imu.dot([1, 0, 0]))
    print(rot_g_to_imu.dot([0, 1, 0]))
    print(rot_g_to_imu.dot([0, 0, 1]))
