
import cv2

# Open a connection to the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame reading was successful
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) == ord(' '):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()


'''
img=cv2.imread('dart.jpg')
cv2.imshow('image',img)
cv2.waitKey()
'''