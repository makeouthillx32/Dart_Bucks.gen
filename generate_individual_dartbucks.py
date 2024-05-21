import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Size of each DartBuck in pixels
DARTBUCK_WIDTH, DARTBUCK_HEIGHT = 1200, 469

def generate_individual_dartbucks(num_dartbucks):
    # Directory to save the individual DartBucks images
    individual_output_dir = "individual_output"
    os.makedirs(individual_output_dir, exist_ok=True)

    # Load base image
    image_folder = "images"
    os.makedirs(image_folder, exist_ok=True)
    base_image_path = os.path.join(image_folder, "base_dartbuck.png")
    base_image = Image.open(base_image_path)

    # Resize the base image to the specified dimensions
    base_image = base_image.resize((DARTBUCK_WIDTH, DARTBUCK_HEIGHT), Image.ANTIALIAS)

    # Font settings
    font_size = 150  # Large font size
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()  # Using default PIL font if arial.ttf is not available
    text_color = (0, 0, 0)  # Black

    def draw_text(draw, text, position, font, fill):
        """Draw text at the specified position."""
        text_width, text_height = draw.textsize(text, font=font)
        text_x, text_y = position
        text_x -= text_width // 2
        text_y -= text_height // 2
        draw.text((text_x, text_y), text, font=font, fill=fill)

    # Generate DartBucks with unique serial numbers and save as individual images
    for serial_number in range(1, num_dartbucks + 1):  # Generate the specified number of DartBucks
        dartbuck = base_image.copy()
        draw = ImageDraw.Draw(dartbuck)
        text = f"No. {serial_number:04d}"  # Format serial number with leading zeros

        # Position the text at the bottom center of the DartBuck
        text_position = (DARTBUCK_WIDTH // 2, DARTBUCK_HEIGHT - 20)  # Move the text lower
        draw_text(draw, text, text_position, font, text_color)

        output_path = os.path.join(individual_output_dir, f"DartBuck_{serial_number:04d}.png")
        dartbuck.save(output_path)
        print(f"Saved: {output_path}")

    print("Individual DartBucks generation complete!")

if __name__ == "__main__":
    num_dartbucks = int(sys.argv[1])
    generate_individual_dartbucks(num_dartbucks)