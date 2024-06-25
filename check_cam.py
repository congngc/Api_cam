import cv2

# Hàm này sẽ kiểm tra và hiển thị danh sách các camera có sẵn
def check_available_cameras(max_tests=10):
    available_cameras = []
    for i in range(max_tests):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

# Gọi hàm và in ra danh sách các camera có thể mở được
cameras = check_available_cameras()
print("Các camera có thể mở được ở các vị trí sau:", cameras)
