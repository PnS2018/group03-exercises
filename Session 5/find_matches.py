import cv2
from matplotlib import pyplot as plt
from draw_matches import draw_matches

# read images in gray scale
img1 = cv2.imread('Lenna.png', 0)
img2 = cv2.imread('Lenna_and_objects.jpg', 0)

# Initiate SIFT detector
sift = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# initialize brute-force matcher
#bf = cv2.BFMatcher_create()
# if on raspberry pi, use
bf = cv2.BFMatcher()

# matching with KNN matcher, find k=2 best matches for each descriptors.
matches = bf.knnMatch(des1, des2, k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m, n in matches:
    # only preserve the matches are close enough to each other
    if m.distance < 0.8*n.distance:
        good.append(m)

# draw matches on the image
#img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, flags=2)
# for raspberry pi
img3 = draw_matches(img1, kp1, img2, kp2, good)

# display the result
plt.imshow(img3, 'gray'), plt.show()








