![haxed](../assets/haxed.png)

GETTING HAXED
---------------

**Title:** ops-401d1: Challenge 06

**Author:** Jake Overall

**Date:** 10/12/2020

**Purpose:** A ransomware tool... designed to encrypt a directory structure and prompt the user to buy the fix 😱

---
```py
import webbrowser
webbrowser.open('http://net-informations.com', new=1)

import cv2 
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


```
