import time
import basic # control code

# ---
## Spiral Animation: From Center Point Outward
# ---
def draw_spiral_center_out(center_x=16, center_y=16, size=15, color=(255, 0, 0), delay=0.05):
    """
    Draws a spiral animation that expands from a central point outwards.

    Args:
        center_x (int): The X-coordinate of the spiral's center.
        center_y (int): The Y-coordinate of the spiral's center.
        size (int): The side length of the square grid the spiral fills (e.g., 7 for a 7x7 area).
        color (tuple): The RGB color of the spiral (e.g., (255, 0, 0) for red).
        delay (float): The delay between lighting/unlighting each pixel.
    """
    all_spiral_coords = []

    x, y = 0, 0
    dx, dy = 0, 1 # Initial direction: (0, 1) means moving "up" (or increasing Y)
    segment_length = 1
    steps_in_segment = 0
    turns = 0

    max_pixels = size * size # Total pixels in a size x size grid

    for _ in range(max_pixels):
        current_x = center_x + x
        current_y = center_y + y

        # Optional: Add boundary checks if your matrix has strict limits (e.g., 0-31)
        # if not (0 <= current_x < 32 and 0 <= current_y < 32):
        #     break

        all_spiral_coords.append((current_x, current_y))

        x += dx
        y += dy
        steps_in_segment += 1

        if steps_in_segment == segment_length:
            steps_in_segment = 0
            turns += 1
            
            # Rotate direction 90 degrees clockwise (e.g., (0,1) -> (-1,0) -> (0,-1) -> (1,0) -> (0,1))
            dx, dy = -dy, dx

            if turns % 2 == 0:
                segment_length += 1
    
    # Print first 5 coordinates to confirm the path (for debugging)
    print(f"Generated spiral path (first 5 coordinates): {all_spiral_coords[:5]}")

    prev_pixel = None

    for x_coord, y_coord in all_spiral_coords:
        basic.set_pixel(x_coord, y_coord, *color) # Use imported function

        if prev_pixel:
            basic.set_pixel(prev_pixel[0], prev_pixel[1], 0, 0, 0) # Use imported function

        prev_pixel = (x_coord, y_coord)
        time.sleep(delay)

    if prev_pixel:
        time.sleep(delay)
        basic.set_pixel(prev_pixel[0], prev_pixel[1], 0, 0, 0) # Use imported function

# ---
## Main Execution for Spiral Animation
# ---
if __name__ == "__main__":
    # Initialize the serial connection once at the start of the main script
    # This calls _initialize_serial() inside basic.py
    basic._initialize_serial() 

    if basic.ser: # Check if serial connection was successfully established
        basic.clear()
        basic.set_brightness(255)
        time.sleep(0.5)

        while True:
            draw_spiral_center_out(center_x=16, center_y=16, size=7, color=(255, 0, 0), delay=0.05)
            time.sleep(0.5)
    else:
        print("Skipping spiral animation as serial connection could not be established.")

    # Important: Close the serial connection when the script finishes or is interrupted
    basic.close_connection()