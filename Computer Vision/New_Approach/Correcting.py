import json

def show_image_and_get_correction(image_path, recognized_text):
   
    corrected_text = input(f"File name: {image_path}, Recognized Text: {recognized_text}\nPlease enter the corrected text: ")
    return corrected_text.strip()

def update_json(json_file, data_list):
    with open(json_file, 'w') as json_file:
        json.dump(data_list, json_file, indent=4)

def main():
    json_file = "/Users/apple/TextDetector/correction_data.json"  
    with open(json_file, 'r') as f:
        data_list = json.load(f)

    for data in data_list:
        image_name = data["image_name"]
        recognized_text = data["recognized_text"]

        corrected_text = show_image_and_get_correction(image_name, recognized_text)
        data["corrected_text"] = corrected_text

    update_json(json_file, data_list)

if __name__ == "__main__":
    main()
