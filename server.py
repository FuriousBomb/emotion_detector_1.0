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
    inp = resp 
    del resp["dominant_emotion"] 
    return (("For the given statement, the system response is {}.".format(resp), "The dominant emotion is {}".format(inp.get("dominant_emotion"))))

if __name__ == "__main__":
    app.run()
