# カメラ故障のため、不使用
from fer import FER
import matplotlib.pyplot as plt


test_image_one = plt.imread(
    "/home/banban/minipupper_control/src/mini_mini/mini_mini/images/greatshot.png")
emo_detector = FER(mtcnn=True)
# Capture all the emotions on the image
captured_emotions = emo_detector.detect_emotions(test_image_one)
# Print all captured emotions with the image
print(captured_emotions)
plt.imshow(test_image_one)

# Use the top Emotion() function to call for the dominant emotion in the image
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
print(dominant_emotion, emotion_score)
