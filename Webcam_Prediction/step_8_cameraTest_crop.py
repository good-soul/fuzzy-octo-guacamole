# Python program to explain cv2.rectangle() method 
   
# importing cv2 
import cv2 

vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    start_point = (700, 275)
    end_point = (950, 525)
    color = (0, 0, 0)
    thickness = 2
    image = cv2.rectangle(frame, start_point, end_point, color, thickness)
    clone = image.copy()
    # crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
    crop_img = clone[275:525, 700:950]

    # Display the resulting frame
    # cv2.imshow('frame', image)
    cv2.imshow('frame', crop_img)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()