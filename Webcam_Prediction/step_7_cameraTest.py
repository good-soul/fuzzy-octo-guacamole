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

    # Display the resulting frame
    cv2.imshow('frame', image)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

# path 
# path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
   
# Reading an image in default mode
# image = cv2.imread(path)
   
# # Window name in which image is displayed
# window_name = 'Image'
  
# # Start coordinate, here (5, 5)
# # represents the top left corner of rectangle
# start_point = (5, 5)
  
# # Ending coordinate, here (220, 220)
# # represents the bottom right corner of rectangle
# end_point = (220, 220)
  
# # Blue color in BGR
# color = (255, 0, 0)
  
# # Line thickness of 2 px
# thickness = 2
  
# # Using cv2.rectangle() method
# # Draw a rectangle with blue line borders of thickness of 2 px
# image = cv2.rectangle(image, start_point, end_point, color, thickness)
  
# # Displaying the image 
# cv2.imshow(window_name, image)