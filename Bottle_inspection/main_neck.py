import cv2
import numpy as np

def detect_cracks(image_path):
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
        print(f"cX: {cX}, cY: {cY}")
        
        
    # Cap Height Detection
    batas_atas = 15
    batas_bawah = 40
    cv2.line(contour_image, (cX-160, y), (cX+150, y), (255, 0, ), 1)
    cv2.putText(contour_image, f"cap heigth: {y}", (cX-200, batas_bawah+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.line(contour_image, (cX-200, batas_atas), (cX+190, batas_atas), (0, 0, 255), 2)
    cv2.line(contour_image, (cX-200, batas_bawah), (cX+190, batas_bawah), (0, 0, 255), 2)
    print(f"Cap Height: {y}")
        
    
    # BP_detection
    cv2.rectangle(contour_image, (cX-120, cY-180), (cX+110, cY-130), (0, 255, 255), 2)
    contrast_value = 10
    threshold_bp = 70
    adjusted_image_bp = cv2.convertScaleAbs(image, alpha=1.0 + contrast_value / 100.0, beta=0)
    gray_image_bp = cv2.cvtColor(adjusted_image_bp, cv2.COLOR_BGR2GRAY)
    _, thresholded_image_bp = cv2.threshold(gray_image_bp, threshold_bp, 255, cv2.THRESH_BINARY) 
    image_roi_bp = thresholded_image_bp[cY-180:cY-130, cX-120:cX+110]
    cv2.imshow("image_roi_bp",image_roi_bp)
    contours_bp, _ = cv2.findContours(image_roi_bp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_bp:
        x, y, w, h = cv2.boundingRect(contour)
        contour_offset = (cX-120, cY-180)
        cv2.drawContours(contour_image, [contour + contour_offset], -1, (0, 0, 255), 1)
        print(f"Lebar dan Tinggi Bridge: {h} x {w}")
    cv2.putText(contour_image, f"Bridge: {h} x {w}", (cX-120, cY-190), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
    
    # # slant cap detection
    # x1 = cX - (cX-68)
    # x2 = cX - (cX-100)
    # y1 = cY - (cY-140)
    # y2 = cY - (cY-187)
    # cv2.rectangle(contour_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    # contrast_slant = 5
    # threshold_slant = 180
    # adjusted_image = cv2.convertScaleAbs(image, alpha=1.0 + contrast_slant / 100.0, beta=0)
    # gray_image_slant = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2GRAY)
    # _, thresholded_image_slant = cv2.threshold(gray_image_slant, threshold_slant, 255, cv2.THRESH_BINARY)
    # inverted_thresholded_slant = cv2.bitwise_not(thresholded_image_slant)
    # image_roi_slant = inverted_thresholded_slant[y1:y2, x1:x2]
    # cv2.imshow("image_roi_slant_kiri",image_roi_slant)
    # contours_slant, _ = cv2.findContours(image_roi_slant, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # total_arc_length = 0
    # for contour in contours_slant:
    #     contour_offset = (x1, y1)
    #     arc_length = cv2.arcLength(contour, closed=True)
    #     total_arc_length += arc_length
    #     cv2.drawContours(contour_image, [contour + contour_offset], -1, (0, 0, 255), 2)
    # print(f"Total Panjang Lengkungan Kiri: {total_arc_length}")
    
    
    # slant cap detection
    # x1 = cX + (341 - cX)
    # x2 = cX + (371 - cX)
    # cv2.rectangle(contour_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    # contrast_slant = 5
    # threshold_slant = 180
    # adjusted_image = cv2.convertScaleAbs(image, alpha=1.0 + contrast_slant / 100.0, beta=0)
    # gray_image_slant = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2GRAY)
    # _, thresholded_image_slant = cv2.threshold(gray_image_slant, threshold_slant, 255, cv2.THRESH_BINARY) 
    # inverted_thresholded_slant = cv2.bitwise_not(thresholded_image_slant)
    # image_roi_slant = inverted_thresholded_slant[y1:y2, x1:x2]
    # cv2.imshow("image_roi_slant_kanan",image_roi_slant)
    # contours_slant, _ = cv2.findContours(image_roi_slant, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # total_arc_length = 0
    # for contour in contours_slant:
    #     contour_offset = (x1, y1)
    #     arc_length = cv2.arcLength(contour, closed=True)
    #     total_arc_length += arc_length
    #     cv2.drawContours(contour_image, [contour + contour_offset], -1, (0, 0, 255), 2)
    # print(f"Total Panjang Lengkungan Kanan: {total_arc_length}")
    
    
    return contour_image

    
def update_image():
    crack_detection_image= detect_cracks(image_file)
    cv2.imshow("Crack Detection", crack_detection_image)

if __name__ == "__main__":
    image_file = "sample_botol/botol_slant.bmp"
    rect_x = 346
    rect_y = 1
    rect_width = 1
    rect_height = 1
    
    crack_detection_image= detect_cracks(image_file)

    cv2.namedWindow("Crack Detection")

    update_image()

    while True:
        key = cv2.waitKey(1)
        if key == 27:  # Tekan tombol 'Esc' untuk keluar dari program
            break
        
        

    cv2.destroyAllWindows()
