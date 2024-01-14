import cv2
import numpy as np
image_file = "sample_botol/botol_slant.bmp"
std_h = 20
std_w = 5
batas_atas = 14
batas_bawah = 40
def detect_botol(image_path):
    image = cv2.imread(image_path)
    adjusted_image = cv2.convertScaleAbs(image, alpha=1, beta=0)
    gray_image = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(gray_image, 254, 255, cv2.THRESH_BINARY) 
    inverted_thresholded = cv2.bitwise_not(thresholded_image)
    contours, _ = cv2.findContours(inverted_thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_image = image.copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(contour_image, (cX, cY), 5, (0, 0, 255), -1)  
        # print(f"cX: {cX}, cY: {cY}")
        
    return contour_image, cX, cY, x, y, w, h



images, cX, cY, x, y, w, h = detect_botol(image_file)


cv2.line(images, (cX-160, y), (cX+150, y), (255, 0, ), 1)
cv2.line(images, (cX-200, batas_atas), (cX+190, batas_atas), (0, 0, 255), 2)
cv2.line(images, (cX-200, batas_bawah), (cX+190, batas_bawah), (0, 0, 255), 2)
if y < batas_atas or y > batas_bawah:
    print("Reject > botol height not OK")
    
contrast = 10
threshold = 80
x1, x2 = cX-120, cX+110
y1, y2 = cY-180, cY-130
img = cv2.convertScaleAbs(images, alpha=1.0 + contrast / 100.0, beta=0)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY) 
cv2.rectangle(images, (x1, y1), (x2, y2), (0, 255, 255), 2)
roi_img = threshold_img[y1:y2, x1:x2]
contours, _ = cv2.findContours(roi_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    contour_offset = (cX-120, cY-180)
    cv2.drawContours(images, [contour + contour_offset], -1, (0, 0, 255), 2)
    x, y, w, h = cv2.boundingRect(contour)
    if h > std_h or w > std_w:
        print("Reject > Bridge Putus")
        
    

x1, x2 = cX-100, cX-50
y1, y2 = cY-140, cY-187 
cv2.rectangle(images, (x1, y1), (x2, y2), (0, 255, 255), 2)
roi_img = threshold_img[y1:y2, x1:x2]
contours, _ = cv2.findContours(roi_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    contour_offset = (cX-120, cY-180)
    cv2.drawContours(images, [contour + contour_offset], -1, (0, 0, 255), 2)
    x, y, w, h = cv2.boundingRect(contour)
    if h > std_h or w > std_w:
        print("Bridge Putus")
        break
    
    
# cv2.imshow("show1",roi_img)
cv2.imshow("show2",images)


cv2.waitKey(0)
cv2.destroyAllWindows()