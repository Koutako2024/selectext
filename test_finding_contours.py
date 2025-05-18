import cv2
import os

joined_path: str = os.path.join(os.path.dirname(__file__), "test_images/proconhp.png")
print(joined_path)
img: cv2.typing.MatLike = cv2.imread(joined_path)
cv2.imshow("in", img)
gray: cv2.typing.MatLike = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# sizes: dict[int, int] = {}

for i, contour in enumerate(contours):
    # if contour.size in sizes:
    #     sizes[contour.size] += 1
    # else:
    #     sizes[contour.size] = 1
    # if contour.size < 0:
    #     continue

    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        ((i * 10 % 256), ((i + 8) * 10 % 256), ((i + 16) * 10 % 256)),
        2,
    )

# print(sizes)

cv2.imshow("out", img)
# cv2.waitKey(0)
# cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.imwrite("out.png", img)
