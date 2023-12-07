# (b) Spatial warping techniques
import numpy as np
import matplotlib.pyplot as plt


def square_to_disk_mapping(x, y, width, height, bulge_factor):
    # Normalize coordinates to range [-1, 1]
    x_normalized = (2 * x / width) - 1
    y_normalized = (2 * y / height) - 1

    # Calculate polar coordinates
    r = np.sqrt(x_normalized**2 + y_normalized**2)

    # Apply bulge effect using a power function
    r_mapped = r**bulge_factor

    # Discard pixels outside the circular boundary
    if r_mapped > 1:
        return None, None

    theta = np.arctan2(y_normalized, x_normalized)

    # Map polar coordinates to disk
    x_mapped = r_mapped * np.cos(theta)
    y_mapped = r_mapped * np.sin(theta)

    # Denormalize coordinates
    x_mapped = (x_mapped + 1) * 0.5 * width
    y_mapped = (y_mapped + 1) * 0.5 * height

    return x_mapped, y_mapped


def disk_to_square_mapping(x, y, width, height, bulge_factor):
    # Normalize coordinates to range [-1, 1]
    x_normalized = (2 * x / width) - 1
    y_normalized = (2 * y / height) - 1

    # Calculate Cartesian coordinates from polar coordinates
    r = np.sqrt(x_normalized**2 + y_normalized**2)
    theta = np.arctan2(y_normalized, x_normalized)

    # Apply bulge effect using a power function
    r_mapped = r**bulge_factor

    # Map Cartesian coordinates to square
    x_mapped = r_mapped * np.cos(theta)
    y_mapped = r_mapped * np.sin(theta)

    # Denormalize coordinates
    x_mapped = (x_mapped + 1) * 0.5 * width
    y_mapped = (y_mapped + 1) * 0.5 * height

    return x_mapped, y_mapped


# Assuming 'baboon.raw' is the file name
file_path = './Project3_Images/baboon.raw'
width, height = 512, 512  # Adjust these dimensions based on your image size

# Read the raw image file using NumPy
with open(file_path, 'rb') as file:
    raw_data = np.fromfile(file, dtype=np.uint8)
    original_image = raw_data.reshape((height, width))

# Bulge factor controls the strength of the bulging effect
bulge_factor = 1.5

# Forward warping: Square to Disk with Bulging
mapped_image_disk = np.zeros_like(original_image)
for y in range(height):
    for x in range(width):
        x_mapped, y_mapped = square_to_disk_mapping(
            x, y, width, height, bulge_factor)

        if x_mapped is not None and y_mapped is not None:
            x_mapped_int, y_mapped_int = int(x_mapped), int(y_mapped)
            mapped_image_disk[y,
                              x] = original_image[y_mapped_int, x_mapped_int]

# Inverse warping: Disk to Square with Bulging
mapped_image_square = np.zeros_like(original_image)
for y in range(height):
    for x in range(width):
        x_mapped, y_mapped = disk_to_square_mapping(
            x, y, width, height, bulge_factor)
        x_mapped_int, y_mapped_int = int(x_mapped), int(y_mapped)

        if 0 <= x_mapped_int < width and 0 <= y_mapped_int < height:
            mapped_image_square[y,
                                x] = original_image[y_mapped_int, x_mapped_int]

# Display the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(mapped_image_disk, cmap='gray')
plt.title('Warped Disk Image (Bulging)')

plt.subplot(1, 3, 3)
plt.imshow(mapped_image_square, cmap='gray')
plt.title('Inverse Warped Square Image (Bulging)')

plt.show()
