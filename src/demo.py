import BadgeScanStream
import utils

video_sample_ref = {
    (0, 14): 'clip_1.mp4',
    (14, 28): 'clip_2.mp4',
    (28, 42): 'clip_3.mp4',
    (42, 56): 'clip_4.mp4',
}

event_list = BadgeScanStream.generate_random_date(
    duration_sec=56,
    num_unique_badges=4,
    num_scan_events=4
)

for e in event_list:
    print(e)

print({e[0] for e in event_list})

windows_to_check = list()
i = 0
while i < len(event_list):
    window_bounds = utils.get_window(event_list[i][0], 14)
    windows_to_check.append(window_bounds)
    while i < len(event_list) and event_list[i][0] <= window_bounds[1]:
        i += 1

print(windows_to_check)
