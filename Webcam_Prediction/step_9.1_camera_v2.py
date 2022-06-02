# Outputs multiple windows for easy testing

import cv2
import numpy as np
import onnxruntime as ort


def center_crop(frame):
    h, w, _ = frame.shape
    start = abs(h - w) // 2
    if h > w:
        return frame[start: start + w]
    return frame[:, start: start + h]


def main():
    # constants
    index_to_letter = list('ABCDEFGHIKLMNOPQRSTUVWXY')
    mean = 0.485 * 255.
    std = 0.229 * 255.

    # create runnable session with exported model
    ort_session = ort.InferenceSession("signlanguage.onnx")

    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # preprocess data
        # frame = center_crop(frame)

        #----------------- CROPPING THE VIDEO FEED
        
        start_point = (700, 275)
        end_point = (950, 525)
        color = (0, 0, 0)
        thickness = 2
        image = cv2.rectangle(frame, start_point, end_point, color, thickness)
        clone = image.copy()
        # crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
        crop_img = clone[275:525, 700:950]
        
        #-------------------

        frame = cv2.cvtColor(crop_img, cv2.COLOR_RGB2GRAY)
        x = cv2.resize(frame, (28, 28))
        x2 = (x - mean) / std

        x3 = x2.reshape(1, 1, 28, 28).astype(np.float32)
        y = ort_session.run(None, {'input': x3})[0]

        index = np.argmax(y, axis=1)
        letter = index_to_letter[int(index)]

        cv2.putText(image, letter, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), thickness=2)
        cv2.imshow("Sign Language Translator Image", image)
        cv2.imshow("Sign Language Translator x2", x2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
