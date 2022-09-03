import matplotlib.pyplot as plt
import numpy as np


def norm(arr: np.ndarray):
    """
    Compute the L2 norm;
    :param arr: vector we want to compute
    :return: numpy array
    """
    return np.sqrt(np.sum(arr**2))


def project(u: np.ndarray, v: np.ndarray):
    """
    Projection function which projects vector v on vector u;
    :param u: vector to be projected on
    :param v: vector we want to project
    :return: numpy array
    """
    return u.dot(v) / u.dot(u) * u


def gram_schmidt_process(accel_z_imu: np.ndarray, plot=False):
    # Transform unit from m/s^2 to gravity for better visualization
    accel_z_imu = accel_z_imu / norm(accel_z_imu)

    # Initialize global orthonormal basis
    accel_x_g = np.array([1, 0, 0])
    accel_y_g = np.array([0, 1, 0])
    accel_z_g = np.array([0, 0, 1])

    u1 = v1 = accel_z_imu
    e1 = u1 / norm(u1)

    v2 = accel_x_g
    proj_u1_v2 = project(u1, v2)
    u2 = v2 - proj_u1_v2
    e2 = u2 / norm(u2)

    # Check if e1 and e2 are orthogonal
    assert e1.dot(e2) < 1e-6, 'e1 and e2 are not orthogonal'

    v3 = accel_y_g
    proj_u1_v3 = project(u1, v3)
    proj_u2_v3 = project(u2, v3)
    u3 = v3 - proj_u1_v3 - proj_u2_v3
    e3 = u3 / norm(u3)

    # Check if e1, e2 and e3 are all orthogonal
    assert e1.dot(e2) < 1e-6 and e1.dot(e3) < 1e-6 and e2.dot(e3) < 1e-6, 'e1, e2 and e3 are not orthogonal'

    print('Orthonormal basis in IMU coordinate:')
    print('X(e2):', e2)
    print('Y(e3):', e3)
    print('Z(e1):', e1)

    rot_g_to_imu = np.array([
        #  X      Y      Z
        [e2[0], e3[0], e1[0]],
        [e2[1], e3[1], e1[1]],
        [e2[2], e3[2], e1[2]]
    ])

    if plot:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_title('Global Coordinate')

        ax.quiver(0, 0, 0, accel_x_g[0], accel_x_g[1], accel_x_g[2], color='black')
        ax.quiver(0, 0, 0, accel_y_g[0], accel_y_g[1], accel_y_g[2], color='black')
        ax.quiver(0, 0, 0, accel_z_g[0], accel_z_g[1], accel_z_g[2], color='black')
        ax.text(accel_x_g[0], accel_x_g[1], accel_x_g[2], r'$accel^X_G$')
        ax.text(accel_y_g[0], accel_y_g[1], accel_y_g[2], r'$accel^Y_G$')
        ax.text(accel_z_g[0], accel_z_g[1], accel_z_g[2], r'$accel^Z_G$')

        ax.quiver(0, 0, 0, proj_u1_v2[0], proj_u1_v2[1], proj_u1_v2[2], color='red')
        ax.text(proj_u1_v2[0], proj_u1_v2[1], proj_u1_v2[2], r'$proj_{u_1}(v_2)$')
        ax.quiver(0, 0, 0, proj_u1_v3[0], proj_u1_v3[1], proj_u1_v3[2], color='red')
        ax.text(proj_u1_v3[0], proj_u1_v3[1], proj_u1_v3[2], r'$proj_{u_1}(v_3)$')
        ax.quiver(0, 0, 0, proj_u2_v3[0], proj_u2_v3[1], proj_u2_v3[2], color='red')
        ax.text(proj_u2_v3[0], proj_u2_v3[1], proj_u2_v3[2], r'$proj_{u_2}(v_3)$')

        ax.quiver(0, 0, 0, e1[0], e1[1], e1[2], color='blue', label=r'$\vec{e_1}$')
        ax.text(e1[0], e1[1], e1[2], r'$\vec{e_1}$')
        ax.quiver(0, 0, 0, e2[0], e2[1], e2[2], color='blue', label=r'$\vec{e_2}$')
        ax.text(e2[0], e2[1], e2[2], r'$\vec{e_2}$')
        ax.quiver(0, 0, 0, e3[0], e3[1], e3[2], color='blue', label=r'$\vec{e_3}$')
        ax.text(e3[0], e3[1], e3[2], r'$\vec{e_3}$')

        ax.legend()
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_zlim(-1, 1)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    return rot_g_to_imu
