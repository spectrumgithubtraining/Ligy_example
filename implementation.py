import time
import threading

# Decorator to measure and print the time taken by a function
def timing_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.2f} seconds to execute.")

    return wrapper

# Function to simulate some work
@timing_decorator
def simulate_work():
    print("Working...")
    time.sleep(2)
    print("Work complete!")

# Using threading to run the function concurrently
if __name__ == "__main__":
    # Create two threads
    thread1 = threading.Thread(target=simulate_work)
    thread2 = threading.Thread(target=simulate_work)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("All threads have finished.")