import threading
import time
def task1():
    # Tugas pertama
    print("Tugas pertama selesai")
    time.sleep(1)
    print("Tugas pertama selesai")
    time.sleep(1)
    print("Tugas pertama selesai")
    time.sleep(1)
    

def task2():
    # Tugas kedua
    print("Tugas kedua selesai")
    time.sleep(3)
    print("Tugas kedua selesai")
    time.sleep(3)
    print("Tugas kedua selesai")
    time.sleep(3)


while (True):
# Membuat dua thread untuk menjalankan tugas-tugas secara simultan
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    # Memulai thread
    thread1.start()
    thread2.start()


    
# Menunggu kedua thread selesai
    thread1.join()
    thread2.join()
    if thread1.is_alive():
        print("nyla")

print("Semua tugas selesai")
