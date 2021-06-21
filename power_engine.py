from power_helpers import get_current_charging


def power_engine_main(soc: float) -> dict:
    """
    get power_engine calculations
    :param soc: state of charge float [0,1]
    :return: power_cal_dict: with voltage and current calculated values
    """
    power_cal_dict = {"current": get_current_charging(soc)}
    return power_cal_dict