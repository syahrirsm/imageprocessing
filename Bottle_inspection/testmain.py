import cv2
import numpy as np

# Inisialisasi variabel global
dragging = False
x_start, y_start, x_end, y_end = -1, -1, -1, -1

# Callback fungsi untuk mouse event
def draw_rectangle(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, dragging

    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        dragging = True
    elif event == cv2.EVENT_MOUSEMOVE and dragging:
        x_end, y_end = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        x_end, y_end = x, y
        dragging = False

# Baca gambar
image = cv2.imread("sample_botol/botol_kanan.bmp")  # Ganti 'gambar.jpg' dengan nama gambar Anda

# Buat jendela dan tetapkan callback fungsi
cv2.namedWindow('Select ROI')
cv2.setMouseCallback('Select ROI', draw_rectangle)

while True:
    # Gambar kotak seleksi
    roi_image = image.copy()
    if not dragging:
        cv2.imshow('Select ROI', roi_image)
    else:
        cv2.rectangle(roi_image, (x_start, y_start), (x_end, y_end), (0, 0, 255), 2)
        cv2.imshow('Select ROI', roi_image)

    # Tekan 'r' untuk mereset seleksi
    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        x_start, y_start, x_end, y_end = -1, -1, -1, -1
        dragging = False

    # Tekan 'q' untuk keluar dan mengambil koordinat
    elif key == ord('q'):
        if x_start != -1 and y_start != -1 and x_end != -1 and y_end != -1:
            print(f'Koordinat Titik Awal: ({x_start}, {y_start})')
            print(f'Koordinat Titik Akhir: ({x_end}, {y_end})')
        # break

cv2.destroyAllWindows()
