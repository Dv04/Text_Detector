import cv2
import pytesseract
import os
import json

def detect_text_tesseract(image_path):
    # Read the image from file
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(gray_image)

    return text.strip()

def process_images_in_folder(folder_path):
    data_list = []
    
    # Loop through all images in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(folder_path, filename)
            recognized_text = detect_text_tesseract(image_path)
            # print("Image:", filename)
            # Create a dictionary to store the data for each image
            image_data = {
                "image_name": filename,
                "recognized_text": recognized_text,
                "corrected_text": ""  # Initialize corrected text as an empty string
            }

            data_list.append(image_data)
    sorted_data_list = sorted(data_list, key=lambda k: int(k['image_name'][0:3]))
    # print(sorted_data_list)
    # Save the data_list to a JSON file
    output_file = "/Users/apple/TextDetector/correction_data.json"
    with open(output_file, 'w') as json_file:
        json.dump(sorted_data_list, json_file, indent=4)

# Example usage:
if __name__ == "__main__":
    folder_path = "/Users/apple/Downloads/Frames"  # Replace with the path to your images folder
    process_images_in_folder(folder_path)
