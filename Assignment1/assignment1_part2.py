import cv2
import os

def save_camera_information(output_path):
    # Open the default webcam (device 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Get webcam properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Make sure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to text file
    with open(output_path, "w") as f:
        f.write(f"fps: {int(fps)}\n")
        f.write(f"height: {int(height)}\n")
        f.write(f"width: {int(width)}\n")

    print(f"Camera information saved to {output_path}")

    cap.release()

def main():
    output_path = os.path.expanduser("~/IKT213_lastname/assignment_1/solutions/camera_outputs.txt")
    save_camera_information(output_path)

if __name__ == "__main__":
    main()
