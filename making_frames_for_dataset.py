import cv2
import os
from tqdm import tqdm

video_path = r'D:\DataScience\Work\advertising_blurring\dataset\video\test\1.mp4'
output_dir = r'D:\DataScience\Work\advertising_blurring\dataset\frames\test\v2'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture(video_path)

# Переменная для отслеживания номера кадра
frame_number = 0

pbar = tqdm(total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_number % 10 == 0:
        frame_filename = os.path.join(output_dir, f'frame_{frame_number}.png')
        cv2.imwrite(frame_filename, frame)

    frame_number += 1
    pbar.update(1)

pbar.close()

cap.release()
cv2.destroyAllWindows()