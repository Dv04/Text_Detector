import cv2
import easyocr

def detect_red_box(frame):
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the red color in HSV
    lower_red = (0, 120, 70)
    upper_red = (10, 255, 255)

    # Create a mask to extract only the red regions in the frame
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contours are found
    if len(contours) > 0:
        # Get the bounding box of the largest contour (red region)
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        # Read text from the red box
        cropped_image = frame[y:y+h, x:x+w]
        reader = easyocr.Reader(['en'])
        text = reader.readtext(cropped_image, detail=0)
        
        # Return the bounding box coordinates [x, y, width, height]
        return [x, y, w, h], text

    return [], "Nothing Detected"

# Test the red box detection on a single image
if __name__ == "__main__":
    image_path = "/Users/apple/Desktop/Trial.png"  # Replace with the path to your test image
    frame = cv2.imread(image_path)

    red_box_coords, text = detect_red_box(frame)

    print("Text in the red box:", text)
    
    if red_box_coords is not None:
        print("Red Box Coordinates:", red_box_coords)
    else:
        print("Red Box not detected.")
