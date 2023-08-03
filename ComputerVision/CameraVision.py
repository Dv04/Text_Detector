import cv2
import os
from ImageVision import detect_red_box

def empty_frames_folder(output_folder):
    # Get a list of all files in the frames folder
    file_list = os.listdir(output_folder)

    # Remove each file in the frames folder
    for filename in file_list:
        file_path = os.path.join(output_folder, filename)
        os.remove(file_path)

def extract_frames_with_timestamp(video_path, output_folder):
    # Empty the frames folder before starting extraction


    video_capture = cv2.VideoCapture(video_path)
    frame_count = 1

    while True:
        success, frame = video_capture.read()
        if not success:
            break

        frame_count += 1
        if frame_count % 21 == 1:
            frame_filename = f"{int((frame_count-1)/21):03d}.jpg"
            frame_filepath = os.path.join(output_folder, frame_filename)

            # Get the timestamp of the current frame (in milliseconds)
            timestamp_ms = video_capture.get(cv2.CAP_PROP_POS_MSEC)

            # Convert the timestamp to a more human-readable format (optional)
            timestamp_sec = timestamp_ms / 1000.0

            # Save the frame with the timestamp information
            cv2.imwrite(frame_filepath, frame)
            # _, text = detect_red_box(frame)
            # print(frame_filename, text)

    video_capture.release()

if __name__ == "__main__":
    output_folder = "/Users/apple/Downloads/Frames"

    empty_frames_folder(output_folder)
    # for i in range(1,10):
    video_file_path = f"/Users/apple/Downloads/ocr/1.mp4" 
    extract_frames_with_timestamp(video_file_path, output_folder)