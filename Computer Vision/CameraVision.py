import cv2
import os

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
            # Create a folder with the same name as the video
            video_name = os.path.splitext(os.path.basename(video_path))[0]
            video_folder = os.path.join(output_folder, video_name)
            if not os.path.exists(video_folder):
                os.mkdir(video_folder)

            frame_filename = f"{int((frame_count-1)/21):03d}.jpg"
            frame_filepath = os.path.join(video_folder, frame_filename)

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
    video_folder = "/Users/apple/Downloads/ocr" 
    video_files = os.listdir(video_folder)
    for video_file in video_files:
        video_file_path = os.path.join(video_folder, video_file)
        extract_frames_with_timestamp(video_file_path, output_folder)