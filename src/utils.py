import math


def get_window(
        timestamp: int,
        window_range: int
):
    """
    This function calculates the lower and upper bounds of a time window of width = window_range within which exists
    the given timestamp.
    :param timestamp: int representation of timestamp
    :param window_range: int representation of width of window to use in calcuation
    :return: (int, int) consisting of int upper and lower bounds of window
    """
    lower_bound = window_range * math.floor(timestamp / window_range) + 1
    return (
        lower_bound,
        lower_bound + window_range - 1
    )
