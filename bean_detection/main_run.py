import subprocess
import cv2
import os
import serial
import time
import threading
   
capture = False   
def task1():
    global capture
    ser.write("2".encode())
    time.sleep(0.5)
    ser.write("b".encode())
    ser.write("1".encode())
    time.sleep(0.5)
    ser.write("a".encode())
    time.sleep(3)
    capture = True
    time.sleep(2)
    output = subprocess.check_output(['python', 'editDetect.py','--source', file_name])
    ser.write("1".encode())
    if "bijirusak" in output.decode('utf-8'):
        ser.write("e".encode())
        print('rusak')
        
    elif 'bijibagus' in output.decode('utf-8'):
        ser.write("f".encode())
        print('biji bagus')
    else:
        ser.write("g".encode())
        print('tidak terdeteksi')

    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Gambar {file_name} berhasil dihapus.")
    else:
        print("Tidak ada gambar yang dapat dihapus.")
        
    time.sleep(3)
    ser.write("a".encode())
    ser.write("b".encode())
    ser.write("c".encode())
    ser.write("d".encode())
    print("selesai thread")

file_name = 'detection/captured_image.jpg'
ser = serial.Serial('COM12', 9600)
time.sleep(2)
ser.write("a".encode())
ser.write("b".encode())
ser.write("c".encode())
ser.write("d".encode())

thread1 = threading.Thread(target=task1)
cap = cv2.VideoCapture('http://192.168.137.93:4747/video')

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 640))
    cv2.imshow("Real-time Camera", frame)

    key = cv2.waitKey(1) & 0xFF
    
    if capture == True:
        captured_image = cv2.resize(frame, (640, 640))
        cv2.imwrite(file_name, captured_image)
        print("capture")
        capture = False

    if key == ord('r'):  
        print("Thread start")
        if thread1.is_alive():
            print("paksa Thread stop")
            thread1._stop()
        thread1 = threading.Thread(target=task1)
        thread1.start()        
    

ser.close()
cap.release()
cv2.destroyAllWindows()

