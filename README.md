# Gram-Schmidt Process
Given a gravity vector, compute the rotation from the IMU reference coordinate to this vector.


## Usage
Given the static acceleration values, one can get rotation matrix from global coordinate to IMU coordinate.  
If ```plot=True```, you can get the 3D plot illustrate the relation between global coordinate and IMU coordinate.
```Python
from gram_schmidt_tools import *


if __name__ == '__main__':
    # Given the random reasonable values read from accelerometer
    accel = np.array([4.29, 5.34, 7.02])
    rot_g_to_imu = gram_schmidt_process(accel, plot=False)
    print('\nGlobal to IMU:')
    print(rot_g_to_imu.dot([1, 0, 0]))
    print(rot_g_to_imu.dot([0, 1, 0]))
    print(rot_g_to_imu.dot([0, 0, 1]))
```
```commandline
Orthonormal basis in IMU coordinate:
X(e2): [ 0.89927159 -0.26480864 -0.34811923]
Y(e3): [-3.48731968e-17  7.95899952e-01 -6.05428168e-01]
Z(e1): [0.43739069 0.54444435 0.71573021]

Global to IMU:
[ 0.89927159 -0.26480864 -0.34811923]
[-3.48731968e-17  7.95899952e-01 -6.05428168e-01]
[0.43739069 0.54444435 0.71573021]
```
![Example](https://github.com/luckykk273/Gram-Schmidt-Process/blob/main/example.png)
## Reference
### Theory
1. [Gram-Schmidt Process - Wiki](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process)
2. [Animation Of Gram-Schmidt Process - zhihu](https://zhuanlan.zhihu.com/p/136627868)

## Contact
Welcome to contact me for any further question, below is my gmail address:
luckykk273@gmail.com