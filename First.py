import cv2 as cv
import mediapipe as mp

# Initialize Mediapipe Hands module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
h = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)

# Open video capture
cap = cv.VideoCapture(0)
handPos={}
while True:
    r, frame = cap.read()
    if r:
        frame = cv.resize(frame, (500, 500))
        frame = cv.flip(frame, 1)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        frame.flags.writeable = False

        # Process the frame with Mediapipe
        res = h.process(frame)
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

        if res.multi_hand_landmarks:
            for lm in res.multi_hand_landmarks:
                myHand=res.multi_hand_landmarks[0]
                for id, point in enumerate(myHand.landmark):
                    height, width, _ = frame.shape
                    cx, cy = int(point.x * width), int(point.y * height)  # Convert coordinates
                    handPos[id]={cx,cy}
                mp_drawing.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

        cv.imshow('frame', frame)

        # Exit if 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
print(handPos)
# Release resources
cap.release()
cv.destroyAllWindows()
