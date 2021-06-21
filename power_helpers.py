"""Helper functions for power_engine
Detailed description goes here. TODO
"""

import numpy as np
import math


def get_voltage_discharging(soc: float) -> float:
    """

    :param soc: battery soc
    :return: corresponding battery voltage when discharging
    """
    voltage = (
            (-1.8289e-36 * (soc ** 10))
            + (9.512e-32 * (soc ** 9))
            - (2.0931e-27 * (soc ** 8))
            + (2.5621e-23 * (soc ** 7))
            - (1.9206e-19 * (soc ** 6))
            + (9.1164e-16 * (soc ** 5))
            - (2.7287e-12 * (soc ** 4))
            + (4.9592e-9 * (soc ** 3))
            - (5.0485e-6 * (soc ** 2))
            + 0.0025335 * soc
            + 3.0153
    )
    return voltage


def get_current_charging(soc: float) -> float:
    """

    :param soc: battery soc
    :return: current corresponding battery current when charging
    """
    current = (
            (-0.046197 * (soc ** 10))
            + (-0.45015 * (soc ** 9))
            + (-1.6715 * (soc ** 8))
            + (-2.724 * (soc ** 7))
            + (-1.0427 * (soc ** 6))
            + (2.3278 * (soc ** 5))
            + (2.4213 * (soc ** 4))
            + (-0.39841 * (soc ** 3))
            + (-1.4183 * (soc ** 2))
            + (-0.58125 * (soc ** 1))
            + 0.74672
    )
    return round(current, 10)


def solar_gen(sun_vector: np.array, eclipse: float) -> float:
    """
    power obtained by the solar panels from the sun vector
    :param sun_vector:
    :param eclipse:
    :return:
    """

    pow_sun = 3.828e+26

    # unit area vectors of the solar panels in body frame
    # on +X, +Y, -Z

    normal_vector_1 = np.array([1, 0, 0])
    normal_vector_2 = np.array([0, 1, 0])
    normal_vector_3 = np.array([0, 0, -1])

    # magnitude of the area vectors of the solar panels
    area_1, area_2, area_3 = 5.5e-3, 11e-3, 11e-3

    # efficiency of solar panels
    efficiency = 0.268

    # Calculations Done:
    # incident_angle=dot_product(sun_vector,normal_to_plane)/((mag(sun_vector).mag(normal_to_plane))
    # magnitude of normal will be 1 as it is a unit vector

    # magnitude of sun vector in kilometers
    sun_mag = np.linalg.norm(sun_vector)
    sun_mag_square = sun_mag ** 2

    # cosine of incident angles
    incident_angle_1 = np.dot(sun_vector, normal_vector_1) / sun_mag
    incident_angle_2 = np.dot(sun_vector, normal_vector_2) / sun_mag
    incident_angle_3 = np.dot(sun_vector, normal_vector_3) / sun_mag

    # intensity of light hitting panels
    intensity = pow_sun / (4 * math.pi * sun_mag_square * 1e6)

    # power generated on each panel
    power_1 = 0 if incident_angle_1 < 0 else efficiency * intensity * area_1 * incident_angle_1
    power_2 = 0 if incident_angle_2 < 0 else efficiency * intensity * area_2 * incident_angle_2
    power_3 = 0 if incident_angle_3 < 0 else efficiency * intensity * area_3 * incident_angle_3

    # total power generated
    total_power = power_1 + power_2 + power_3

  

    # in eclipse region power generated is zero as no light is incident on the panels
    if eclipse == 0:
        total_power = 0

    return total_power

s_v = np.array([1,0,0])
a = solar_gen(s_v,0)
print(a)
