import time
import basic  # Your ESP32 serial communication module

def generate_spiral(center_x, center_y, size):
    coords = []
    x, y = 0, 0
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
            dx, dy = -dy, dx
            if turns % 2 == 0:
                segment_length += 1

    return coords

if __name__ == "__main__":
    basic._initialize_serial()

    if not basic.ser:
        print("Could not establish serial connection. Exiting.")
        exit()

    # Parameters
    center_x = 16
    center_y = 16
    spiral_size = 15
    spiral = generate_spiral(center_x, center_y, spiral_size)

    # Set brightness and color
    brightness = 255
    basic.set_brightness(brightness)
    color = (255, 0, 0)  # Red

    current_index = 0  # Start from 0

    print(f"\n[Instructions]")
    print(f"Press Enter        → light next pixel")
    print(f"Enter a number     → light the Nth pixel in spiral")
    print(f"Type 'c' then Enter → clear")
    print(f"Type 'q' then Enter → quit\n")

    while True:
        user_input = input(">>> ")

        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'c':
            basic.clear()
            continue
        elif user_input.strip() == '':
            # Just press Enter → light next
            if current_index >= len(spiral):
                print("Spiral finished.")
                continue
            index = current_index
            current_index += 1
        else:
            try:
                n = int(user_input)
                if 1 <= n <= len(spiral):
                    index = n - 1  # Convert 1-based to 0-based
                    current_index = index + 1  # Advance future default index
                else:
                    print("Index out of range.")
                    continue
            except ValueError:
                print("Invalid input. Enter a number, 'c', 'q', or press Enter.")
                continue

        # Light pixel
        basic.clear()
        x, y = spiral[index]
        basic.set_pixel(x, y, *color)

    basic.clear()
    basic.close_connection()
    print("Serial connection closed.")
