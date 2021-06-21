from power_helpers import solar_gen
import numpy as np

def test_solar_gen() -> None:
    """
    test for solar_gen function

    :return: None
    """
    s_v = np.array([1,0,0])
    expected_power_1 = 4.490136550288065e+16
    expected_power_2 = 0

    assert solar_gen(s_v, 1) == expected_power_1, "the function solar_gen does not match the expected output"
    assert solar_gen(s_v, 0) == expected_power_2, "the function solar_gen does not match the expected output, as the satellite is in eccipse region, the total power should be 0"

test_solar_gen()


