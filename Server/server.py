import time
import pyautogui
import bettercam
import numpy as np
import threading
import queue

# Target color
TARGET_COLOR = np.array([75, 219, 106], dtype=np.uint8)

# Initialize BetterCam instance
camera = bettercam.create()

def is_target_green(frame):
    """
    Check if the captured frame contains the target green color.
    """
    return np.array_equal(frame[0, 0], TARGET_COLOR)

def frame_capture_worker(camera, frame_queue, region):
    """
    Continuously capture frames and push them into the queue.
    """
    camera.start(region=region, target_fps=240)
    while True:
        frame = camera.get_latest_frame()
        if frame is not None:
            frame_queue.put(frame)

def find_green_screen(camera, region):
    """
    Use a threaded frame capture loop for detecting the target green color.
    """
    frame_queue = queue.Queue(maxsize=1)  # Single frame buffer
    thread = threading.Thread(target=frame_capture_worker, args=(camera, frame_queue, region))
    thread.daemon = True
    thread.start()

    print("Waiting for the screen to turn green...")
    while True:
        frame = frame_queue.get()
        if is_target_green(frame):
            camera.stop()
            return True

def click_on_screen(click_coords):
    """
    Simulate a mouse click at the specified coordinates.
    """
    print("Green detected! Clicking...")
    pyautogui.click(x=click_coords[0], y=click_coords[1])

def main():
    # Define monitoring region and click location
    region = (700, 400, 701, 401)  # Single-pixel region
    click_coords = (960, 540)      # Clickable area

    input("Position your browser and press Enter to start...")
    try:
        while True:
            find_green_screen(camera, region)
            click_on_screen(click_coords)
            time.sleep(0.1)  # Short delay for the next round
    except KeyboardInterrupt:
        print("\nExiting...")
        camera.release()  # Free resources

if __name__ == "__main__":
    main()
