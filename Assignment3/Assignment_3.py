#Importing
import cv2
import numpy as np

#Sobel Edge Detection
def sobel_edge_detection(image_path, save_path="sobel_edges.jpg"):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    #Applying Gaussian Blur
    blurred = cv2.GaussianBlur(image, (3, 3), 0)

    # Actual Sobel edge detection
    sobel = cv2.Sobel(blurred, cv2.CV_64F, 1, 1, ksize=1)
    sobel = cv2.convertScaleAbs(sobel)

    cv2.imwrite(save_path, sobel)

#Canny Edge Detection
def canny_edge_detection(image_path, threshold_1=50, threshold_2=50, save_path="canny_edges.jpg"):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Applyingn Gaussian Blur
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    #Actual Canny edge detection
    edges = cv2.Canny(blurred, threshold_1, threshold_2)

    cv2.imwrite(save_path, edges)



# Template Matching
def template_match(image_path, template_path, save_path="template_match.jpg", threshold=0.9):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    # Matching
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    #Marking matches
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_color, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    cv2.imwrite(save_path, img_color)


#Image Resizing with Pyramids
def resize(image_path, scale_factor=2, up_or_down="up", save_path="resized.jpg"):
    img = cv2.imread(image_path)

    if up_or_down.lower() == "up":
        for _ in range(scale_factor):
            img = cv2.pyrUp(img)
    elif up_or_down.lower() == "down":
        for _ in range(scale_factor):
            img = cv2.pyrDown(img)
    else:
        raise ValueError("must enter only 'up' or 'down'")

    cv2.imwrite(save_path, img)


if __name__ == "__main__":
    lambo_img = "C:/Users/adity/Downloads/lambo.png"
    shapes_img = "C:/Users/adity/Downloads/shapes-1.png"
    template_img = "C:/Users/adity/Downloads/shapes_template.jpg"

    #Calling
    sobel_edge_detection(lambo_img, "output_sobel.jpg")
    canny_edge_detection(lambo_img, 50, 50, "output_canny.jpg")
    template_match(shapes_img, template_img, "output_template_match.jpg")
    resize(lambo_img, scale_factor=2, up_or_down="up", save_path="output_resize_up.jpg")
    resize(lambo_img, scale_factor=2, up_or_down="down", save_path="output_resize_down.jpg")

