#!/usr/bin/python3
# https://github.com/spmallick/learnopencv/blob/master/BlobDetector/blob.py
# From https://dev.to/simarpreetsingh019/detecting-geometrical-shapes-in-an-image-using-opencv-4g72

import cv2


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200

# Filter by Area.
params.filterByArea = True
params.minArea = 150

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)


def detect_blobs(thrash):
    # Detect blobs.
    keypoints = detector.detect(thrash)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob

    # im_with_keypoints = cv2.drawKeypoints(thrash, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show blobs
    # cv2.imshow("Keypoints", im_with_keypoints)

    return keypoints


def rectangle_detector(thrash):
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    out_approx = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

        # cv2.drawContours(thrash, [approx], 0, (0, 0, 0), 5)

        # x = approx.ravel()[0]
        # y = approx.ravel()[1] - 5
        # Requirements to be bounding rectangle
        if len(approx) == 4:
            _, _, width, height = cv2.boundingRect(approx)
            aspect = float(width)/height
            if (width > 500) and (height > 300) and (1.5 < aspect < 1.8):
                # return approx, thrash
                out_approx = approx

    return out_approx


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, img = cap.read()

        approx, _ = rectangle_detector(img)

        if approx is not None:
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 5)
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h
            print(aspectRatio, x, y, w, h, approx)
            if 0.95 <= aspectRatio < 1.05:
                cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))

            else:
                cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))

        cv2.imshow('shapes', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
