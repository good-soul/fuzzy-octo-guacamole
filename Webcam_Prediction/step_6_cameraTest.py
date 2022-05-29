# import cv2
# import numpy as np
# import onnxruntime as ort

# def center_crop(frame):
#     h, w, _ = frame.shape
#     start = abs(h - w) // 2
#     if h > w:
#         return frame[start: start + w]
#     return frame[:, start: start + h]

# cam = cv2.VideoCapture(0)

# while True:
#     result, image = cam.read()
#     cv2.imshow("GeeksForGeeks", image)
# # cv2.imwrite("GeeksForGeeks.png", image)
# # image_cut = center_crop(image)
# # cv2.imwrite("cut_image.png", image_cut)


import cv2
  
def center_crop(frame):
    h, w, _ = frame.shape
    start = abs(h - w) // 2
    if h > w:
        return frame[start: start + w]
    return frame[:, start: start + h]


# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()