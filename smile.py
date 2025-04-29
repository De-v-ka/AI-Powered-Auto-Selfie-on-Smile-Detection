import cv2
import mediapipe as mp
import pyautogui
import winsound
x1=0
y1=0
x2=0
y2=0
img_counter = 0
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
camera = cv2.VideoCapture(0)
while True:
    _,img = camera.read()
    img = cv2.flip(img,1)
    fh, fw, _ = img.shape
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_img)
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks):
            x = int(landmark.x * fw)
            y = int(landmark.y * fh)
            if id == 43:
                x1=x
                y1=y
            if id == 287:
                x2 = x
                y2 = y
               
        print(x,y)
        dist = int((x2-x1)**2 + (y2-y1)**2)**(0.5)
        print(dist)
        if dist > 88:
            filename = f"selfie_{img_counter}.png"
            cv2.imwrite(filename,img)
            winsound.PlaySound("sound.wav",winsound.SND_FILENAME)
            img_counter +=1
            cv2.waitKey(1000)
    cv2.imshow("Smiling Faced",img)
    key = cv2.waitKey(100)
    if key == 27:   #esc 
        break
camera.release()
cv2.destroyAllWindows()

