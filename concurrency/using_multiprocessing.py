import multiprocessing
import time

def worker(name, delay):
    for i in range(5):
        time.sleep(delay)
        print(f"Worker {name}: {i}")

if __name__ == '__main__':
    # Create processes
    process1 = multiprocessing.Process(target=worker, args=("A", 1))
    process2 = multiprocessing.Process(target=worker, args=("B", 1.5))

    # Start processes
    process1.start()
    process2.start()

    # Wait for processes to complete
    process1.join()
    process2.join()

    print("All processes completed")
