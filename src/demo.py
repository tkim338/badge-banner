import BadgeScanStream
import utils
import boto3
from VideoOverlay import VideoOverlay

video_sample_map = {
    (1, 14): 'clip_1.mp4',
    (15, 28): 'clip_2.mp4',
    (29, 42): 'clip_3.mp4',
    (43, 56): 'clip_4.mp4',
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

videos_to_scan = [video_sample_map[window] for window in windows_to_check]

print(videos_to_scan)

# upload video to S3
video_name = videos_to_scan[0]
bucket_name = 'badge-banner'
object_name = 'test_clip.mp4'

# s3_client = boto3.client('s3')
# s3_client.upload_file(
#     Filename=f'../resources/{video_name}',
#     Bucket=bucket_name,
#     Key=object_name
# )

# query Rekognition API
# sns_arn = 'arn:aws:sns:us-east-1:432660864273:badge-banner-person-tracking'
rekognition_client = boto3.client('rekognition')
# rekognition_job_id = rekognition_client.start_person_tracking(
#     Video={
#         'S3Object': {
#             'Bucket': bucket_name,
#             'Name': object_name
#         }
#     },
#     NotificationChannel={
#         'SNSTopicArn': sns_arn,
#         'RoleArn': 'arn:aws:iam::432660864273:role/RekognitionRole'
#     }
# )

# tracking_results = rekognition_client.get_person_tracking(
#     # JobId=rekognition_job_id
#     JobId='7be5b2eebe313220383fe7b8d51287908c8fd43f975caad19593984b67a26d65'
# )
#
# print(tracking_results)
# print()

# compare people and badge counts

video_overlay = VideoOverlay(
    video_path=f'../resources/{videos_to_scan[0]}',
    rekognition_tracking_results=dict()
)

video_overlay.display()
