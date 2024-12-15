import cv2
import easyocr

# Load image
img = cv2.imread('Abdullah.jpg', 0)

# Apply Gaussian blur
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Create an EasyOCR reader for English language
reader = easyocr.Reader(['en'])

# Read text from the image
result = reader.readtext(blur)

# Ask the user for input text
search_text = input("Enter the text you want to search for: ")

# Loop through the result and print matched text
matched_found = False
for (bbox, text, prob) in result:
    if search_text.lower() in text.lower():  # Case-insensitive match
        matched_found = True
        print(f'Matched Text: {text}, Probability: {prob}')
        
# If no match is found
if not matched_found:
    print("No match found.")