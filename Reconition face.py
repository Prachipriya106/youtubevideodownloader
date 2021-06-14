import cv2
print("package import")
img = cv2.imread("jenyy.jpeg", -1)
print(img)
cv2.imshow("image", img)
cv2.waitKey(0)