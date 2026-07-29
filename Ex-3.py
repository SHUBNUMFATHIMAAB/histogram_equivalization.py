#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import matplotlib.pyplot as plt

# Grayscale Histogram Equalization

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


# Color Histogram Equalization

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


# In[ ]:




