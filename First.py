import cv2 as cv
import mediapipe as mp
import handGestures as HG
import time
import pyautogui as pg
# Initialize Mediapipe Hands module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
h = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)

# Open video capture
cap = cv.VideoCapture(0)
handPos = {}
pressed = False
rHand=False
lHand=False
last_press_time = 0

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

        current_time = time.time() #current
        if pressed and (current_time - last_press_time) >= 2:
            pressed = False

        if res.multi_hand_landmarks:
            for lm,hand_handedness in zip(res.multi_hand_landmarks,res.multi_handedness):
                myHand = res.multi_hand_landmarks[0]
                handedness = hand_handedness.classification[0].label
                if handedness=='right': rHand = True
                elif handedness=='left': lHand = True
                for id, point in enumerate(myHand.landmark):
                    height, width, _ = frame.shape
                    cx, cy = int(point.x * width), int(point.y * height)  # Convert coordinates
                    handPos[id] = (cx, cy)

                if HG.pressSpace(handPos,handedness) and not pressed:
                    print('space pressed')
                    pg.press('space')
                    pressed = True
                    last_press_time = current_time

                if HG.pressLeft(handPos,handedness) and not pressed:
                    print('left pressed')
                    pg.press('left')
                    pressed = True
                    last_press_time = current_time
                if HG.pressRight(handPos,handedness) and not pressed:
                    print('right pressed')
                    pg.press('right')
                    pressed=True
                    last_press_time = current_time
                mp_drawing.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

        cv.imshow('frame', frame)

        # Exit if 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv.destroyAllWindows()
