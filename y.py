import cv2
import numpy as np

def mouse_callback(event, x, y, flags, param):
    global cropping, rectangles
    
    if event == cv2.EVENT_MOUSEMOVE:
        rectangles.append((x, y))
        cropping = True
        process_image()

def process_image():
    global img_front, img_back, output
    
    # Resize images to the same size
    img_front_resized = cv2.resize(img_front, (img_front.shape[1], img_front.shape[0]))
    img_back_resized = cv2.resize(img_back, (img_front.shape[1], img_front.shape[0]))
    
    # Reset the output image
    output = img_front_resized.copy()
    
    # Copy and paste regions from the back image
    for rect in rectangles:
        x, y = rect
        radius = 5  # Set the desired radius of the circular region
        
        # Copy the corresponding region from the back image
        copied_region = img_back_resized[y - radius:y + radius, x - radius:x + radius]
        
        # Paste the copied region into the front image
        output[y - radius:y + radius, x - radius:x + radius] = copied_region
    
    # Display the output image
    cv2.imshow('output', output)

# Read the front and back images
img_front = cv2.imread('result.jpg', -1)
img_back = cv2.imread('frame2.jpg', -1)

# Create an output image
output = np.zeros_like(img_front)

# Resize the images to a common size (e.g., 500x500)
output_size = (500, 500)
img_front = cv2.resize(img_front, output_size)
img_back = cv2.resize(img_back, output_size)

rectangles = []
cropping = False

# Create a window for displaying the output image
cv2.namedWindow('output')

# Set the mouse callback function
cv2.setMouseCallback('output', mouse_callback)

while True:
    cv2.imshow('output', output)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cv2.destroyAllWindows()
