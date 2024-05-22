import cv2
import random


class VideoOverlay:
    def __init__(
            self,
            video_path: str,
            rekognition_tracking_results: dict
    ):
        self.video_path = video_path
        self.rekognition_tracking_results = rekognition_tracking_results

        self.color_map = dict()

    def display(self):
        video_capture = cv2.VideoCapture(self.video_path)

        # Check if camera opened successfully
        if not video_capture.isOpened():
            print("Error opening video file")

        i = 0
        # Read until video is completed
        while video_capture.isOpened():

            # Capture frame-by-frame
            ret, frame = video_capture.read()
            if ret:

                while (i < len(self.rekognition_tracking_results['Persons'])
                       and self.rekognition_tracking_results['Persons'][i]['Timestamp'] <= video_capture.get(cv2.CAP_PROP_POS_MSEC)):
                    bounding_box = self.rekognition_tracking_results['Persons'][i]['Person']['BoundingBox']
                    top_left_point = (
                        int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH) * bounding_box['Left']),
                        int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT) * bounding_box['Top'])

                    )
                    bottom_right_point = (
                        int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH) * (bounding_box['Left'] + bounding_box['Width'])),
                        int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT) * (bounding_box['Top'] + bounding_box['Height']))
                    )

                    person_index = self.rekognition_tracking_results['Persons'][i]['Person']['Index']
                    if person_index in self.color_map:
                        person_color = self.color_map[person_index]
                    else:
                        person_color = (
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255)
                        )
                        self.color_map[person_index] = person_color

                    frame = cv2.rectangle(
                        frame,
                        top_left_point,
                        bottom_right_point,
                        person_color,
                        10
                    )

                    frame = cv2.putText(
                        frame,
                        str(person_index),
                        top_left_point,
                        fontFace=cv2.FONT_HERSHEY_PLAIN,
                        fontScale=10,
                        color=person_color,
                        thickness=10
                    )

                    i += 1

                # Display the resulting frame
                cv2.imshow('Frame', frame)

                # input("Press Enter to continue...")

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Break the loop
            else:
                break

        # When everything done, release the video capture object
        video_capture.release()

        # Closes all the frames
        # cv2.destroyAllWindows()

        print(self.color_map.keys)
