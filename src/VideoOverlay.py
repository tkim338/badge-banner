import cv2


class VideoOverlay:
    def __init__(
            self,
            video_path: str,
            rekognition_tracking_results: dict
    ):
        self.video_path = video_path
        self.rekognition_tracking_results = rekognition_tracking_results

    def display(self):
        video_capture = cv2.VideoCapture(self.video_path)

        # Check if camera opened successfully
        if not video_capture.isOpened():
            print("Error opening video file")

        # Read until video is completed
        while video_capture.isOpened():

            # Capture frame-by-frame
            ret, frame = video_capture.read()
            if ret:
                # Display the resulting frame
                cv2.imshow('Frame', frame)

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
