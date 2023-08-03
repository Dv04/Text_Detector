import cv2
import easyocr
from ImageVision import detect_red_box

def extract_text_from_video(video_path, output_file):
    video_capture = cv2.VideoCapture(video_path)
    stringResult = " "
    with open(output_file, 'w') as text_file:
        while True:
            ret, frame = video_capture.read()

            if not ret:
                break

            # Detect the red box in the frame
            red_box_coords, text = detect_red_box(frame)
            print(red_box_coords, text)
            # Write the extracted text to the output file
            listToStr = ' '.join([str(elem) for elem in text])
            text_file.write(listToStr + "\n")
            stringResult += listToStr + "\n"
    video_capture.release()
    return stringResult

if __name__ == "__main__":
    video_file_path = "/Users/apple/Downloads/ocr/5.mp4"
    output_text_file = "text.txt"

    text = extract_text_from_video(video_file_path, output_text_file)
    print(text)