from sklearn.model_selection import train_test_split
import easyocr
import json


def train_easyocr_json(json_path, model_path):
    """Trains an EasyOCR model using the specified JSON dataset."""

    # Initialize the EasyOCR reader.
    reader = easyocr.Reader(["en"])

    # Load the JSON dataset.
    with open(json_path) as json_file:
        data = json.load(json_file)

    # Split the dataset into a training set and a test set.
    train_data, test_data = train_test_split(data, test_size=0.2)

    # Train the model.
    reader.train_from_json(train_data, model_path)

    # Evaluate the model.
    reader.evaluate_from_json(test_data)

if __name__ == "__main__":
    # The path to the JSON.
    dataset_path = "/Users/apple/TextDetector/correction_data.json"

    # The path to the model.
    model_path = "/Users/apple/Downloads/PTH/english_g2.pth"

    # Train the model.
    train_easyocr_json(dataset_path, model_path)
