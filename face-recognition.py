import dlib
import cv2
import matplotlib.pyplot as plt
# Load the image
image_path = 'arif.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale (Dlib works with grayscale images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detector = dlib.get_frontal_face_detector()
faces = detector(gray)
for face in faces:
    x, y, w, h = (face.left(), face.top(), face.width(), face.height())
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

import face_recognition
known_image = face_recognition.load_image_file("arif.jpg")
unknown_image = face_recognition.load_image_file("Abdullah.jpg")

known_encodings = face_recognition.face_encodings(known_image)
unknown_encodings = face_recognition.face_encodings(unknown_image)

if known_encodings and unknown_encodings:
    results = face_recognition.compare_faces([known_encodings[0]], unknown_encodings[0])
    if results[0]:
        print("Yes, Picture Matched")
    else:
        print("No, Picture did not match")
else:
    print("Face encoding failed for one or both images.")


plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()