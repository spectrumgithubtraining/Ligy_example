import threading
import time

def print_messages(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{thread_name}: {time.ctime(time.time())}")

# Create threads
thread1 = threading.Thread(target=print_messages, args=("Thread-1", 2))
thread2 = threading.Thread(target=print_messages, args=("Thread-2", 4))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
