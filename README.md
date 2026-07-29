# Histogram Equalization Using OpenCV (Grayscale & Color Images)

## Aim

To develop a Python program using OpenCV to perform histogram equalization on both grayscale and color images in order to enhance image contrast and improve overall visual quality.

---

## Features

The program performs the following operations:

- Reads and displays a grayscale image.
- Plots the histogram of the grayscale image.
- Applies histogram equalization to the grayscale image.
- Reads and displays a color image.
- Plots the histograms of the Blue, Green, and Red channels.
- Converts the image from BGR to HSV color space.
- Applies histogram equalization to the Value (V) channel.
- Converts the enhanced image back to BGR format.
- Displays the original and enhanced images along with their histograms.

---

## Software Used

- Python 3.x
- OpenCV (`cv2`)
- Matplotlib
- NumPy
- Jupyter Notebook / VS Code
- Anaconda

---

## Algorithm

1. Import the required libraries: OpenCV, NumPy, and Matplotlib.
2. Read the input image in grayscale format.
3. Display the grayscale image and plot its histogram.
4. Apply histogram equalization using `cv2.equalizeHist()`.
5. Display the original grayscale image, equalized image, and their histograms.
6. Read the same image in color format.
7. Plot the histograms of the Blue, Green, and Red channels.
8. Convert the image from BGR to HSV color space.
9. Apply histogram equalization to the Value (V) channel.
10. Merge the HSV channels and convert the image back to BGR.
11. Display the original and enhanced color images along with their histograms.

---

## Developed By

**Name:** SHUBNUM FATHIMA AB

**Register Number:** 212225240147

---

## Program

```
import cv2
import matplotlib.pyplot as plt

# ----------------------------
# Grayscale Histogram Equalization
# ----------------------------

# Read image in grayscale
gray = cv2.imread("parrot.jpg", 0)

# Apply histogram equalization
gray_eq = cv2.equalizeHist(gray)

# Display grayscale images and histograms
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

plt.subplot(2,2,2)
plt.hist(gray.ravel(), 256, [0,256], color='black')
plt.title("Original Histogram")

plt.subplot(2,2,3)
plt.imshow(gray_eq, cmap="gray")
plt.title("Equalized Grayscale")
plt.axis("off")

plt.subplot(2,2,4)
plt.hist(gray_eq.ravel(), 256, [0,256], color='black')
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()

# ----------------------------
# Color Histogram Equalization
# ----------------------------

# Read color image
img = cv2.imread("parrot.jpg")

# Convert BGR to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Plot original color histograms
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title("Original Color Image")
plt.axis("off")

plt.subplot(2,2,2)
colors = ('b','g','r')
for i, c in enumerate(colors):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color=c)
plt.title("Original BGR Histogram")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Equalize V channel
h, s, v = cv2.split(hsv)
v = cv2.equalizeHist(v)
hsv_eq = cv2.merge((h, s, v))

# Convert back to BGR
img_eq = cv2.cvtColor(hsv_eq, cv2.COLOR_HSV2BGR)
img_eq_rgb = cv2.cvtColor(img_eq, cv2.COLOR_BGR2RGB)

plt.subplot(2,2,3)
plt.imshow(img_eq_rgb)
plt.title("Enhanced Color Image")
plt.axis("off")

plt.subplot(2,2,4)
for i, c in enumerate(colors):
    hist = cv2.calcHist([img_eq],[i],None,[256],[0,256])
    plt.plot(hist, color=c)
plt.title("Enhanced BGR Histogram")

plt.tight_layout()
plt.show()
```

---

## Output
<img width="1062" height="492" alt="s1" src="https://github.com/user-attachments/assets/d112f264-73b3-4e09-b2a1-9d84820f99cc" />

<img width="1057" height="497" alt="s2" src="https://github.com/user-attachments/assets/1b0e453c-e14d-4ca5-8b07-0749f20c19b7" />

<img width="1087" height="495" alt="s3" src="https://github.com/user-attachments/assets/8dd9e99c-6618-476c-8884-93aa85911bc8" />

<img width="1060" height="497" alt="s4" src="https://github.com/user-attachments/assets/ef7db870-5888-4c60-8319-16893d01e6e7" />

---

## Result

Histogram equalization was successfully implemented using OpenCV for both grayscale and color images. The enhanced images exhibited improved contrast and better intensity distribution, demonstrating the effectiveness of histogram equalization in image enhancement.
