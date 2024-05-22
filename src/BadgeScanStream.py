import random
import uuid


def generate_random_data(
        duration_sec: int,
        num_unique_badges: int,
        num_scan_events: int
):
    """
    Function to generate random badge scan event data.
    :param duration_sec: integer representation of total time window of events (in seconds)
    :param num_unique_badges: number of unique badges from which to generate data
    :param num_scan_events: number of scan events for which to generate data.  If this number is greater than the number
    of unique badges, multiple scan events for one or more badges will be present in the returned data.
    :return:
    """
    badge_list = [str(uuid.uuid4()) for i in range(num_unique_badges)]
    event_timestamps = random.sample(range(1, duration_sec), num_scan_events)

    event_list = []
    badge_index = 0
    for timestamp in event_timestamps:
        event_list.append((timestamp, badge_list[badge_index]))
        badge_index += 1
        if badge_index >= len(badge_list):
            badge_index = 0
    return sorted(event_list, key=lambda event_tuple: event_tuple[0])
