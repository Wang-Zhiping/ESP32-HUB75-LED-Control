import serial
import time

# --- Configuration ---
# Set the correct serial port for your ESP32 (e.g., 'COM3' on Windows, '/dev/ttyACM0' on Linux)
SERIAL_PORT = '/dev/ttyACM3'
BAUD_RATE = 115200

# Global serial connection object
# It's good practice to encapsulate this if you have many functions,
# but for simple cases, a global variable is fine.
ser = None

def _initialize_serial():
    """Initializes the serial connection. Call this once before using display functions."""
    global ser
    if ser is None:
        try:
            ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
            time.sleep(2)  # Wait for the ESP32 to initialize
            print(f"Serial connection established on {SERIAL_PORT}")
        except serial.SerialException as e:
            print(f"Error opening serial port {SERIAL_PORT}: {e}")
            print("Please ensure the ESP32 is connected and the port is correct.")
            ser = None # Ensure ser is None if connection fails
            # You might want to exit or handle this error more gracefully in a real application

def set_pixel(x, y, r, g, b):
    """
    Set the color of a specific pixel on the display.
    Ensures serial connection is open before sending.
    """
    if ser is None:
        _initialize_serial() # Attempt to initialize if not already
        if ser is None: # If initialization still failed
            print("Serial connection not active. Cannot set pixel.")
            return

    cmd = f"PIXEL {x} {y} {r} {g} {b}\n"
    try:
        ser.write(cmd.encode())
    except serial.SerialException as e:
        print(f"Error writing to serial port: {e}")
        # Optionally, try to re-initialize or handle the error

def set_brightness(level):
    """
    Set the global brightness level (0-255).
    Ensures serial connection is open before sending.
    """
    if ser is None:
        _initialize_serial()
        if ser is None:
            print("Serial connection not active. Cannot set brightness.")
            return

    cmd = f"BRIGHTNESS {level}\n"
    try:
        ser.write(cmd.encode())
    except serial.SerialException as e:
        print(f"Error writing to serial port: {e}")

def clear():
    """
    Clear the display.
    Ensures serial connection is open before sending.
    """
    if ser is None:
        _initialize_serial()
        if ser is None:
            print("Serial connection not active. Cannot clear display.")
            return

    try:
        ser.write(b"CLEAR\n")
    except serial.SerialException as e:
        print(f"Error writing to serial port: {e}")

def close_connection():
    """Closes the serial connection."""
    global ser
    if ser is not None:
        ser.close()
        print("Serial connection closed.")
        ser = None

# --- Example Usage when run directly ---
# The code inside `if __name__ == "__main__":` will only run when this file
# is executed directly (e.g., `python display_controller.py`).
# It will NOT run when this file is imported into another script.
if __name__ == "__main__":
    print("Running display_controller.py directly for testing...")
    _initialize_serial() # Initialize serial only when run directly

    if ser: # Only proceed if serial connection was successful
        clear()
        set_brightness(255)
        print("Display cleared and brightness set to 255.")
        time.sleep(0.5)

        # Light up some test pixels
        print("Lighting up test pixels...")
        set_pixel(5, 5, 255, 0, 0)  # Red
        set_pixel(6, 6, 0, 255, 0)  # Green
        set_pixel(7, 7, 0, 0, 255)  # Blue
        time.sleep(3) # Keep them on for a bit
        
        clear() # Clear them again
        print("Test pixels cleared.")
        close_connection() # Close connection when done with direct testing
    else:
        print("Could not initialize serial connection. Skipping direct test.")