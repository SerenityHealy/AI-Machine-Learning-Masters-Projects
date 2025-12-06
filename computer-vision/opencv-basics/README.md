# OpenCV Image Viewer

A simple OpenCV-based image viewer and file operation utility for displaying and copying images.

## Overview

This project demonstrates basic OpenCV functionality including image loading, display, and file operations. It's designed as an introduction to computer vision with OpenCV.

## Features

- **Image Display**: Opens and displays images in a window
- **Keyboard Control**: Close with any key press
- **Automatic Saving**: Copies image to Desktop
- **Error Handling**: Validates file existence
- **Cross-Platform**: Works on Windows, Mac, Linux

## Installation

```bash
# Install OpenCV
pip install opencv-python
```

## Usage

### Setup

1. Place `brain.jpg` (or your image) in the same folder as the script
2. Run the script:

```bash
python brain_image_viewer.py
```

### Expected Behavior

1. Image window opens with title "Neural Image Viewer"
2. Press any key to close the window
3. Copy of image automatically saved to Desktop
4. Console shows save location

### Using Different Images

Edit the script to use a different image:

```python
source_file = 'your_image.jpg'
```

Or modify to accept command-line arguments.

## Code Walkthrough

### 1. Import Libraries

```python
import cv2  # OpenCV for image operations
import os   # File path operations
```

### 2. Load Image

```python
source_file = 'brain.jpg'
image_data = cv2.imread(source_file)
```

### 3. Error Checking

```python
if image_data is None:
    print(f"Error: Could not read the image file '{source_file}'.")
```

### 4. Display Image

```python
cv2.imshow("Neural Image Viewer", image_data)
cv2.waitKey(0)  # Wait for any key press
cv2.destroyAllWindows()  # Clean up
```

### 5. Save Copy

```python
desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
saved_file = os.path.join(desktop_dir, "copied_brain_image.jpg")
cv2.imwrite(saved_file, image_data)
```

## File Structure

```
opencv-basics/
├── brain_image_viewer.py    # Main script
├── brain.jpg                # Sample image (not included)
└── README.md               # This file
```

## Output

```
# Successful run:
A copy of the image has been saved to: /Users/yourname/Desktop/copied_brain_image.jpg

# Error (missing file):
Error: Could not read the image file 'brain.jpg'.
```

## Technical Details

**OpenCV Functions Used**:
- `cv2.imread()`: Load image from file
- `cv2.imshow()`: Display image in window
- `cv2.waitKey()`: Wait for keyboard input
- `cv2.destroyAllWindows()`: Close all windows
- `cv2.imwrite()`: Save image to file

**Image Format**: BGR color format (OpenCV default)

## Extending the Project

### Add Command-Line Arguments

```python
import sys

if len(sys.argv) > 1:
    source_file = sys.argv[1]
```

### Add Image Transformations

```python
# Grayscale conversion
gray = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

# Resize
resized = cv2.resize(image_data, (640, 480))

# Blur
blurred = cv2.GaussianBlur(image_data, (15, 15), 0)
```

### Save Multiple Formats

```python
cv2.imwrite("output.png", image_data)
cv2.imwrite("output.bmp", image_data)
cv2.imwrite("output.tiff", image_data)
```

## Common Issues

### Issue: Image Window Opens and Closes Immediately
**Solution**: `cv2.waitKey(0)` is required to keep window open

### Issue: File Not Found Error
**Solution**: Ensure image is in same directory or use absolute path

### Issue: Image Display is Too Large
**Solution**: Resize before displaying:
```python
image_data = cv2.resize(image_data, (800, 600))
```

## Learning Outcomes

- OpenCV installation and setup
- Image I/O operations
- Window management
- File path manipulation with os module
- Error handling for missing files
- Cross-platform path handling

## Next Steps

After mastering this, try:
1. Image filtering and transformations
2. Video capture and processing
3. Face detection with Haar cascades
4. Feature detection (corners, edges)
5. Image segmentation
6. Object tracking
