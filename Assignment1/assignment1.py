import cv2


def print_image_information(image):
    # Get height, width, and channels
    height, width = image.shape[:2]
    channels = image.shape[2] if len(image.shape) == 3 else 1

    # Get total size (number of values)
    size = image.size

    # Get data type
    data_type = image.dtype

    # Print all information
    print(f"Height: {height}")
    print(f"Width: {width}")
    print(f"Channels: {channels}")
    print(f"Size (number of values): {size}")
    print(f"Data type: {data_type}")


def main():
    # Load the image
    image = cv2.imread("C:/Users/adity/Downloads/lena.png")

    # Check if image loaded successfully
    if image is None:
        print("Error: Image not found!")
        return

    # Print image information
    print_image_information(image)


if __name__ == "__main__":
    main()
