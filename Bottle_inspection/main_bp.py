import cv2
import numpy as np

def detect_cracks(image_path, rect_x, rect_y, rect_width, rect_height):
    image = cv2.imread(image_path)
    
    adjusted_image = cv2.convertScaleAbs(image, alpha=1, beta=0)
    gray_image = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(gray_image, 254, 255, cv2.THRESH_BINARY) 
    inverted_thresholded = cv2.bitwise_not(thresholded_image)
    contours, _ = cv2.findContours(inverted_thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_image = image.copy()
    for contour in contours:
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        # print(f"cX: {cX}, cY: {cY}")
        
    
    # BP_detection
    cv2.rectangle(contour_image, (cX-120, cY-180), (cX+110, cY-130), (0, 255, 255), 1) #bridge
    # cv2.rectangle(contour_image, (rect_x, rect_y), (rect_x2, rect_y2), (0, 255, 0), 2)
    contrast_value = 10
    threshold_bp = 70
    adjusted_image_bp = cv2.convertScaleAbs(image, alpha=1.0 + contrast_value / 100.0, beta=0)
    gray_image_bp = cv2.cvtColor(adjusted_image_bp, cv2.COLOR_BGR2GRAY)
    _, thresholded_image_bp = cv2.threshold(gray_image_bp, threshold_bp, 255, cv2.THRESH_BINARY) 
    image_roi_bp = thresholded_image_bp[cY-180:cY-130, cX-120:cX+110]
    # image_roi = thresholded_image[rect_y:rect_y2, rect_x:rect_x2]
    cv2.imshow("image_roi",image_roi_bp)
    contours_bp, _ = cv2.findContours(image_roi_bp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total_cracks = 0
    total_area = 0
    for contour in contours_bp:
        x, y, w, h = cv2.boundingRect(contour)
        contour_offset = (cX-120, cY-180)
        cv2.drawContours(contour_image, [contour + contour_offset], -1, (0, 0, 255), 1)
        area = cv2.contourArea(contour)
        total_cracks += 1
        total_area += area
        print(f"X: {x} | Y: {y}")
        print(f"Height: {h} | Width: {w}")
    
    # contrast_value = 10
    # threshold_bp = 70
    # adjusted_image = cv2.convertScaleAbs(image, alpha=1.0 + contrast_value / 100.0, beta=0)
    # gray_image = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2GRAY)
    # _, thresholded_image = cv2.threshold(gray_image, threshold_bp, 255, cv2.THRESH_BINARY)
    # cv2.imshow("thresholded_image", thresholded_image)
    # rect_x2 = rect_x + rect_width
    # rect_y2 = rect_y + rect_height
    # image_roi = thresholded_image[rect_y:rect_y2, rect_x:rect_x2]
    # contours, _ = cv2.findContours(image_roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # contour_image = image.copy()
    # cv2.imshow("image_roi", image_roi)
    # cv2.rectangle(contour_image, (rect_x, rect_y), (rect_x2, rect_y2), (0, 255, 0), 2)

    # total_cracks = 0
    # total_area = 0
    # for contour in contours:
    #     contour_offset = (rect_x, rect_y)
    #     cv2.drawContours(contour_image, [contour + contour_offset], -1, (0, 0, 255), 1)
    #     area = cv2.contourArea(contour)
    #     total_cracks += 1
    #     total_area += area
    #     print(f"Crack {total_cracks}:")
    
    return contour_image

    
def update_image():
    crack_detection_image= detect_cracks(image_file, rect_x, rect_y, rect_width, rect_height)
    cv2.imshow("Crack Detection", crack_detection_image)

if __name__ == "__main__":
    image_file = "sample_botol/botol_kiri.bmp"
    rect_x = 346
    rect_y = 1
    rect_width = 1
    rect_height = 1
    
    crack_detection_image= detect_cracks(image_file, rect_x, rect_y, rect_width, rect_height)

    cv2.namedWindow("Crack Detection")

    update_image()

    while True:
        key = cv2.waitKey(1)
        if key == 27:  # Tekan tombol 'Esc' untuk keluar dari program
            break
        
        

    cv2.destroyAllWindows()
