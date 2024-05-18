import BadgeScanStream

event_list = BadgeScanStream.generate_random_date(
    duration_sec=100,
    num_unique_badges=10,
    num_scan_events=10
)

for e in event_list:
    print(e)

print({e[0] for e in event_list})
