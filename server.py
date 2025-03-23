from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def Emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_data = emotion_detector(text_to_analyze)
    # Extract the scores from the response
    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']
    # Determine the dominant emotion
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]
   
    # Return a formatted string with all the scores and the dominant emotion
    return (
        "For the given statement,the system response is "
        "'Anger': {}, 'Disgust': {}, 'Fear': {}, 'Joy': {}, 'Sadness': {}. "
        "The dominant emotion is <b> {}<b>."
        .format(anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion, dominant_score)
    )

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000)