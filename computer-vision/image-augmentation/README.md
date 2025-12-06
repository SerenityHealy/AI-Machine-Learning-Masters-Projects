# Image Augmentation Tool

A batch image augmentation utility for expanding image datasets with various transformations.

## Overview

This tool performs folder-wide image augmentation, applying random transformations to create additional training data for machine learning models. It preserves directory structure and generates detailed reports.

## Features

- **Multiple Augmentation Types**: Flip, rotate, brightness, contrast
- **Batch Processing**: Processes entire folders recursively
- **Configurable**: Control number of augmentations per image
- **Directory Preservation**: Maintains original folder structure
- **Format Support**: JPG, PNG, BMP, TIFF, WebP
- **Automatic Reporting**: Generates JSON metadata
- **Original Preservation**: Keeps copy of original images

## Installation

```bash
# Install Pillow (PIL)
pip install pillow
```

## Usage

### Basic Usage

```bash
# Augment all images in a folder
python augment_images.py /path/to/images
```

This creates an output directory: `/path/to/images_aug`

### Custom Output Directory

```bash
# Specify custom output location
python augment_images.py /path/to/images /path/to/output
```

### Control Augmentation Count

```bash
# Generate 5 random augmentations per image
python augment_images.py /path/to/images --per-image 5

# Generate only 1 augmentation per image
python augment_images.py /path/to/images --per-image 1
```

## Augmentation Types

### 1. Flip (Horizontal)
- Mirrors image left-to-right
- Useful for symmetrical objects
- Filename suffix: `__flip`

### 2. Rotate
- Random rotation: -10° to +10°
- Bicubic interpolation for quality
- Expands image to show full rotated content
- Filename suffix: `__rotate`

### 3. Brightness
- Random factor: 0.8 to 1.2 (80%-120%)
- Makes images darker or brighter
- Filename suffix: `__bright`

### 4. Contrast
- Random factor: 0.8 to 1.2
- Adjusts difference between light and dark
- Filename suffix: `__contrast`

## Output Structure

```
output_directory/
├── README.txt              # Augmentation report
├── image1__orig.jpg        # Original copy
├── image1__flip.jpg        # Flipped version
├── image1__rotate.jpg      # Rotated version
├── image1__bright.jpg      # Brightness adjusted
├── subfolder/
│   ├── image2__orig.png
│   ├── image2__contrast.png
│   └── ...
```

## Supported Formats

- JPEG/JPG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- WebP (.webp)

## README.txt Report

The tool generates a report with:
```json
{
  "source_dir": "/path/to/images",
  "output_dir": "/path/to/images_aug",
  "images": 100,
  "generated": 300,
  "ops": ["flip", "rotate", "bright", "contrast"]
}
```

## Examples

### Example 1: Expand Dataset for Training

```bash
# Create 3 augmentations per image for ML training
python augment_images.py ./training_data ./augmented_data --per-image 3
```

Result: If you had 100 images, you now have 400 (100 originals + 300 augmented)

### Example 2: Minimal Augmentation

```bash
# Just one random augmentation per image
python augment_images.py ./photos --per-image 1
```

### Example 3: Maximum Diversity

```bash
# All 4 augmentation types per image
python augment_images.py ./dataset --per-image 4
```

## Technical Details

**Image Processing**: Pillow (PIL)
**Resampling**: BICUBIC for rotations
**Color Handling**: Auto-converts to RGB for JPEG
**Error Handling**: Skips corrupted/unreadable images

### Code Structure

- `augment_one()`: Applies single augmentation type
- `safe_open()`: Loads image with error handling
- `prepare_for_save()`: Handles format conversion
- `main()`: Orchestrates batch processing

## Use Cases

1. **Machine Learning**: Expand training datasets
2. **Data Augmentation**: Improve model generalization
3. **Testing**: Create variations for robustness testing
4. **Preprocessing**: Prepare images for CV pipelines

## Best Practices

- **Start Small**: Test with `--per-image 1` first
- **Backup Originals**: Tool preserves originals, but keep source safe
- **Disk Space**: Each augmentation creates a new file
- **Quality**: Use high-quality source images

## Limitations

- Random augmentations (not deterministic without seed)
- Fixed rotation range (-10° to +10°)
- Fixed brightness/contrast ranges
- No advanced augmentations (shear, zoom, etc.)

## Learning Outcomes

- Image processing with Pillow
- Batch file operations
- Directory traversal and preservation
- Command-line argument parsing
- Data augmentation techniques
- Error handling in file I/O
