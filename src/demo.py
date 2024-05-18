import BadgeScanStream
import utils

event_list = BadgeScanStream.generate_random_date(
    duration_sec=3000,
    num_unique_badges=10,
    num_scan_events=10
)

for e in event_list:
    print(e)

print({e[0] for e in event_list})

windows_to_check = list()
i = 0
while i < len(event_list):
    window_bounds = utils.get_window(event_list[i][0], 60)
    windows_to_check.append(window_bounds)
    while i < len(event_list) and event_list[i][0] <= window_bounds[1]:
        i += 1

print(windows_to_check)
