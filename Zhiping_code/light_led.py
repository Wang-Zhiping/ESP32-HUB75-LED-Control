import time
import basic  # Your ESP32 serial communication module

def generate_spiral(center_x, center_y, size):
    """
    Generates a spiral coordinate list from the center outward.

    Args:
        center_x (int): Center X coordinate
        center_y (int): Center Y coordinate
        size (int): Size of the spiral area (e.g., 7 for 7x7)

    Returns:
        List of (x, y) tuples in spiral order
    """
    coords = []
    x, y = 15, 15
    dx, dy = 0, 1
    segment_length = 1
    steps_in_segment = 0
    turns = 0

    while len(coords) < size * size:
        px, py = center_x + x, center_y + y
        coords.append((px, py))

        x += dx
        y += dy
        steps_in_segment += 1

        if steps_in_segment == segment_length:
            steps_in_segment = 0
            turns += 1
            dx, dy = -dy, dx  # Rotate direction clockwise
            if turns % 2 == 0:
                segment_length += 1

    return coords

if __name__ == "__main__":
    basic._initialize_serial()

    if not basic.ser:
        print("Could not establish serial connection. Exiting.")
        exit()

    # Parameters
    center_x = 0
    center_y = 0
    spiral_size = 11  # Spiral will cover a 7x7 region
    spiral = generate_spiral(center_x, center_y, spiral_size)

    # Set brightness and color
    basic.clear()
    brightness = int(255)  # Range: 0–255
    basic.set_brightness(brightness)
    r = int(255)  # Red
    g = int(0)    # Green
    b = int(0)    # Blue
    color = (r, g, b)

    while True:
        user_input = input(f"\nEnter spiral index (1 ~ {len(spiral)}) or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        try:
            n = int(user_input)
            if 1 <= n <= len(spiral):
                basic.clear()
                x, y = spiral[n - 1]  # Convert 1-based input to 0-based index
                basic.set_pixel(x, y, *color)
            else:
                print("Index out of range.")
        except ValueError:
            print("Please enter a valid number.")

    basic.clear()
    basic.close_connection()
    print("Serial connection closed.")
