from flask import *
import requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def welcome_page():
    return render_template("index.html")

@app.route('/emotionDetector')
def detect(): 
    req = request.args.get("textToAnalyze") 
    resp = emotion_detector(req) 
    inp = resp["dominant_emotion"]
    del resp["dominant_emotion"] 
    return (("For the given statement, the system response is {}. The dominant emotion is <b>{}</b>".format((resp), inp)))

if __name__ == "__main__":
    app.run()
