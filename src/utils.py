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
    return (
        window_range * math.floor(timestamp / window_range),
        window_range * math.ceil(timestamp / window_range)
    )
