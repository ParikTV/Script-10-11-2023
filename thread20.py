import threading
import time


def download_data():
    """Simulate downloading data."""
    print("Starting data download...")
    for i in range(1, 6):  # Simulate a 5-step download
        print(f"Downloading {i * 20}%")
        time.sleep(0.5)  # Simulate time taken to download each part
    print("Download completed!")


# Create a thread to handle the data download
t = threading.Thread(target=download_data)

# Start the download thread
t.start()

# We'll join with a timeout, meaning we'll wait for the thread to finish for up to 1 second.
# Since the download will take 2.5 seconds, our main thread will move on after the timeout.
t.join(timeout=1.0)

print("Main thread continues its work (perhaps some unrelated task).")
