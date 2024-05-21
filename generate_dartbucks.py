import os
import subprocess
import sys

def main():
    # Ask the user how many DartBucks they want to generate
    num_dartbucks = int(input("How many DartBucks do you want to generate? "))

    # Generate individual DartBucks
    result = subprocess.run([sys.executable, "generate_individual_dartbucks.py", str(num_dartbucks)])
    if result.returncode != 0:
        print("Error generating individual DartBucks.")
        return

    # Create composite images for printing
    result = subprocess.run([sys.executable, "create_composit_image.py"])
    if result.returncode != 0:
        print("Error creating composite images.")
        return

if __name__ == "__main__":
    main()