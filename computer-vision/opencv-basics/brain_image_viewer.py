#Portfolio option 1- Serenity Healy
#The script displays and imports an image "brain.jpg"
#after the image appears you can close the image with a wait key "0"
# the script automatically saves a copy of the image to the users Desktop
#
# Required for running script:
# OpenCV must be used and installed in your python IDE use command: -pip install opencv-python in your terminal
# download brain.jpg and save to the same folder as this python script
#
# Instructions to run the script from terminal:
# 1. Open the terminal
# 2. If you are using a virtual environment activate the virtual environment
# 3. Navigate to the folder on the computer that both files are saved using this command: -cd/Users/serenityhealy/PycharmProjects/ComputerVision
# 5. Run the script with the command: -python3 Module1_Portfolio_Option.py

#The image will automatically pop up and can be closed using any key.
# the script automatically saves a copy of the image "brain_copy.jpg" to the users Desktop


import cv2
import os


source_file = 'brain.jpg'
image_data = cv2.imread(source_file)


if image_data is None:
    print(f"File could not be read - Error '{source_file}'.")
else:

    cv2.imshow("Neural Image Viewer", image_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    saved_file = os.path.join(desktop_dir, "copied_brain_image.jpg")
    cv2.imwrite(saved_file, image_data)

    print(f"The copied image is saved to {saved_file}")