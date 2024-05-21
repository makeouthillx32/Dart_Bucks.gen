import os
from PIL import Image

# Define the size of an A4 sheet in pixels at 300 DPI
A4_WIDTH, A4_HEIGHT = 2480, 3508

# Size of each DartBuck in pixels
DARTBUCK_WIDTH, DARTBUCK_HEIGHT = 1200, 469

def create_composite_images():
    # Directory to save the composite images
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Directory of individual DartBucks images
    individual_output_dir = "individual_output"

    # Ensure the individual_output directory exists
    if not os.path.exists(individual_output_dir):
        raise FileNotFoundError(f"The directory '{individual_output_dir}' does not exist. Please run 'generate_individual_dartbucks.py' first.")

    # Define the grid layout for DartBucks on an A4 sheet
    cols = 2
    rows = 7

    # Calculate margins and spacing with a 10-pixel gap
    margin_x = (A4_WIDTH - (cols * DARTBUCK_WIDTH) - ((cols - 1) * 10)) // 2
    margin_y = (A4_HEIGHT - (rows * DARTBUCK_HEIGHT) - ((rows - 1) * 10)) // 2

    # List all individual DartBucks images in order
    individual_images = sorted(os.listdir(individual_output_dir))

    # Create composite images for printing
    page_number = 1
    pages = []
    for i in range(0, len(individual_images), cols * rows):
        sheet = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), (255, 255, 255))  # Create a blank A4 page
        for j in range(cols * rows):
            if i + j >= len(individual_images):
                break
            dartbuck_path = os.path.join(individual_output_dir, individual_images[i + j])
            dartbuck = Image.open(dartbuck_path)
            x = margin_x + (j % cols) * (DARTBUCK_WIDTH + 10)
            y = margin_y + (j // cols) * (DARTBUCK_HEIGHT + 10)
            sheet.paste(dartbuck, (x, y))
        output_path = os.path.join(output_dir, f"DartBucks_Page_{page_number}.png")
        sheet.save(output_path)
        pages.append(sheet)
        print(f"Saved: {output_path}")
        page_number += 1

    # Save all pages to a single PDF file
    pdf_path = os.path.join(output_dir, "DartBucks.pdf")
    pages[0].save(pdf_path, save_all=True, append_images=pages[1:])
    print(f"PDF saved: {pdf_path}")

    print("Composite DartBucks generation complete!")

if __name__ == "__main__":
    create_composite_images()