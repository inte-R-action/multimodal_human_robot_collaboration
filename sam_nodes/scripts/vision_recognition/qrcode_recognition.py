import cv2
from pyzbar import pyzbar


def read_QR():
    cp = cv2.VideoCapture(0)
    while True:
        _, frame = cp.read()
        if frame is not None:
            cv2.imshow('qr', frame)
            key = cv2.waitKey(1)
            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
            decoded_QR = pyzbar.decode(frame)
            for qr in decoded_QR:
                try:
                    name = qr.data.decode("utf-8")
                    if name == 'James':
                        cv2.destroyWindow("qr")
                        return True, "James"
                    elif name == 'Gorkem':
                        cv2.destroyWindow("qr")
                        return True, "Gorkem"
                    else:
                        cv2.destroyWindow("qr")
                        print(f"unrecognised QR code {name}")
                        return False, "unknown"

                except Exception as e:
                    print(e, qr.data)
                    cv2.destroyWindow("qr")
                    return False, "unknown"


if __name__ == '__main__':
    print(read_QR())
