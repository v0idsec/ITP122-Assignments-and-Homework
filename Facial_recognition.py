import face_recognition
import cv2

#load the known image file and encode to face data
known_image = face_recognition.load_image_file("e:/Downloads/Python stuff/known_image.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

#init video capture from the default camera (ind 0)
video_capture = cv2.VideoCapture(0)

while True:
    #Capture single frame from the camera
    ret, frame = video_capture.read()

    #find all faces in the frame
    face_locations = face_recognition.face_locations(frame)

    #encode all faces within the frame
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #Compare the face encoding of the detected face with known_image
        matches = face_recognition.compare_faces([known_encoding], face_encoding)

        #draw rectacngle around face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #label face
        label = "Known Face" if matches[0] else "Unknown Face"
        cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0) if matches[0] else (255, 0, 0), 2)

    #display the frame with detected face/ label
    cv2.imshow('Video', frame)

  #exit loop if q is pressed 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the video capture and close all windows 
video_capture.release()
cv2.destroyAllWindows()

