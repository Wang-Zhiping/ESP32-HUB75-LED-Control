import time
import basic  # Your custom hardware control module

# ---
# Spiral Animation: Expanding from Center Outward in a Fixed Square Region
# ---
def draw_spiral_center_out(center_x=16, center_y=16, size=7, color=(255, 0, 0), delay=0.05):
    """
    Draws a spiral animation that expands from a central point outward within a fixed square region.

    Args:
        center_x (int): X-coordinate of the spiral center.
        center_y (int): Y-coordinate of the spiral center.
        size (int): Side length of the square spiral area (e.g. 15 for a 15x15 grid).
        color (tuple): RGB color for the spiral (e.g. (255, 0, 0) for red).
        delay (float): Time delay (in seconds) between each animation step.
    """
    all_spiral_coords = []

    # Calculate region bounds
    half = size // 2
    min_x, max_x = center_x - half, center_x + half
    min_y, max_y = center_y - half, center_y + half

    # Spiral generation parameters
    x, y = 0, 0               # Offset from center
    dx, dy = 0, 1             # Initial direction: upward
    segment_length = 1
    steps_in_segment = 0
    turns = 0

    # Build coordinate list within square area
    while len(all_spiral_coords) < size * size:
        current_x = center_x + x
        current_y = center_y + y

        # Only include coordinates within bounds
        if min_x <= current_x <= max_x and min_y <= current_y <= max_y:
            all_spiral_coords.append((current_x, current_y))

        # Move to next coordinate
        x += dx
        y += dy
        steps_in_segment += 1

        if steps_in_segment == segment_length:
            steps_in_segment = 0
            turns += 1
            dx, dy = -dy, dx  # Rotate 90 degrees clockwise
            if turns % 2 == 0:
                segment_length += 1

    # Animate the spiral
    prev_pixel = None
    for x_coord, y_coord in all_spiral_coords:
        basic.set_pixel(x_coord, y_coord, *color)  # Turn on current pixel
        if prev_pixel:
            basic.set_pixel(prev_pixel[0], prev_pixel[1], 0, 0, 0)  # Turn off previous pixel
        prev_pixel = (x_coord, y_coord)
        time.sleep(delay)

    # Turn off final pixel
    if prev_pixel:
        time.sleep(delay)
        basic.set_pixel(prev_pixel[0], prev_pixel[1], 0, 0, 0)

# ---
# Main Execution
# ---
if __name__ == "__main__":
    # Initialize serial connection to LED matrix or controller
    basic._initialize_serial()

    if basic.ser:
        basic.clear()
        basic.set_brightness(255)
        time.sleep(0.5)

        while True:
            draw_spiral_center_out(center_x=16, center_y=16, size=30, color=(255, 0, 0), delay=0.1)
            time.sleep(0.5)
    else:
        print("Skipping spiral animation as serial connection could not be established.")

    # Close the serial connection when done
    basic.close_connection()
