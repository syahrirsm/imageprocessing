import cv2

# Muat model deteksi manusia HOG + SVM
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')  # Ganti dengan path file XML yang sesuai

# Buka kamera
cap = cv2.VideoCapture(0)  # Gunakan 0 untuk webcam internal atau ganti dengan path video jika diperlukan

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Konversi frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi manusia dalam frame
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Gambar kotak pembatas di sekitar manusia yang terdeteksi
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Tampilkan frame dengan kotak pembatas manusia
    cv2.imshow('Human Detection', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela OpenCV
cap.release()
cv2.destroyAllWindows()
