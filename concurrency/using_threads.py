import threading
import time

def worker(name, delay):
    for i in range(5):
        time.sleep(delay)
        print(f"Worker {name}: {i}")

# Create threads
thread1 = threading.Thread(target=worker, args=("A", 1))
thread2 = threading.Thread(target=worker, args=("B", 1.5))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads completed")
