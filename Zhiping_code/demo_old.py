import time
import basic 
MATRIX_WIDTH = 32
MATRIX_HEIGHT = 32

def run_quadrant_fill_animation(delay_t=0.3):
    """
    Runs an animation that fills quadrants of the matrix in sequence.

    Args:
        delay_t (float): The delay between each quadrant fill.
    """
    half_w, half_h = MATRIX_WIDTH // 2, MATRIX_HEIGHT // 2

    # Pattern 0: Right Half Fill (Red)
    basic.clear() # Using basic.clear()
    for x in range(half_w, MATRIX_WIDTH):
        for y in range(MATRIX_HEIGHT):
            basic.set_pixel(x, y, 255, 0, 0)  # Using basic.set_pixel()
    time.sleep(delay_t)

    # Pattern 1: Bottom Half Fill (Red)
    basic.clear()
    for x in range(MATRIX_WIDTH):
        for y in range(half_h, MATRIX_HEIGHT):
            basic.set_pixel(x, y, 255, 0, 0)
    time.sleep(delay_t)

    # Pattern 2: Left Half Fill (Red)
    basic.clear()
    for x in range(0, half_w):
        for y in range(MATRIX_HEIGHT):
            basic.set_pixel(x, y, 255, 0, 0)
    time.sleep(delay_t)

    # Pattern 3: Top Half Fill (Red)
    basic.clear()
    for x in range(MATRIX_WIDTH):
        for y in range(0, half_h):
            basic.set_pixel(x, y, 255, 0, 0)
    time.sleep(delay_t)


# ==== Example Usage when run directly ====
if __name__ == "__main__":
    print("Running basic_patterns.py directly for testing...")
    
    # Initialize serial connection through the basic module
    basic._initialize_serial() # Using basic._initialize_serial()

    if basic.ser: # Check if serial connection was successful, using basic.ser
        basic.clear()
        basic.set_brightness(255)
        print("Display cleared and brightness set to 255.")
        time.sleep(2)

        basic.clear()
        print("Initial test pixels cleared. Starting pattern loop...")

        # Start the pattern loop
        while True:
            run_quadrant_fill_animation(delay_t=0.3)
    else:
        print("Serial connection could not be established. Skipping pattern execution.")

    # Ensure the serial connection is closed when the script finishes or is interrupted
    basic.close_connection() # Using basic.close_connection()