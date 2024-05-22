import BadgeScanStream
import utils
import boto3
from VideoOverlay import VideoOverlay
import time


rekognition_client = boto3.client('rekognition')


def generate_random_data():
    video_sample_map = {
        (1, 14): 'clip_1.mp4',
        (15, 28): 'clip_2.mp4',
        (29, 42): 'clip_3.mp4',
        (43, 56): 'clip_4.mp4',
    }

    event_list = BadgeScanStream.generate_random_data(
        duration_sec=56,
        num_unique_badges=4,
        num_scan_events=4
    )

    for e in event_list:
        print(e)

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

    return videos_to_scan


def upload_video(video_path: str):
    # upload video to S3
    bucket_name = 'badge-banner'
    object_name = 'test_clip.mp4'

    s3_client = boto3.client('s3')
    s3_client.upload_file(
        Filename=video_path,
        Bucket=bucket_name,
        Key=object_name
    )

    # query Rekognition API
    sns_arn = 'arn:aws:sns:us-east-1:432660864273:badge-banner-person-tracking'

    rekognition_job_id = rekognition_client.start_person_tracking(
        Video={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': object_name
            }
        },
        NotificationChannel={
            'SNSTopicArn': sns_arn,
            'RoleArn': 'arn:aws:iam::432660864273:role/RekognitionRole'
        }
    )

    return rekognition_job_id


def process_results(rekognition_job_id: str, video_path: str):
    tracking_results = rekognition_client.get_person_tracking(JobId=rekognition_job_id)
    while tracking_results['JobStatus'] == 'IN_PROGRESS':
        tracking_results = rekognition_client.get_person_tracking(JobId=rekognition_job_id)
        time.sleep(5)
    if tracking_results['JobStatus'] == 'FAILED':
        print('Video processing by Rekognition has failed.')
    else:  # tracking_results['JobStatus'] == 'SUCCEEDED'
        print(tracking_results)

    video_overlay = VideoOverlay(
        video_path=video_path,
        rekognition_tracking_results=tracking_results
    )

    video_overlay.display()

    person_set = set()
    for p in tracking_results['Persons']:
        print(p)
        person_set.add(p['Person']['Index'])

    print(person_set)


# video_list = generate_random_data()
video_list = ['clip_1.mp4', 'clip_3.mp4', 'clip_4.mp4']
# job_id = upload_video(f'../resources/{video_list[0]}')
# print(job_id)
job_id = '4c768b2a1b8e6bcdc49bd9c35caae24a7e054d496f7e472cbf0daaea0f81bb9e'
process_results(job_id, f'../resources/{video_list[0]}')

