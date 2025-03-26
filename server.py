"""
server.py
This module contains the Flask application for the emotion detector.
It handles HTTP requests and responses, and integrates with the emotion detection logic.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyzes the given text to determine the dominant emotion"""
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_data = emotion_detector(text_to_analyze)
    # Extract the scores from the response
    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']
    dominant_emotion = emotion_data['dominant_emotion']
    #check if dominant_emotion is None
    if dominant_emotion is None:
        return "<b> Invalid text! Please try again! <b>"
    # Return a formatted string with all the scores and the dominant emotion
    return (
    f"For the given statement, the system response is "
    f"'Anger': {anger_score}, 'Disgust': {disgust_score}, 'Fear': {fear_score}, "
    f"'Joy': {joy_score}, 'Sadness': {sadness_score}. "
    f"The dominant emotion is <b>{dominant_emotion}<b>."
    )
@app.route("/")
def render_index_page():
    """
    Renders the index page of the web application.

    Returns:
    Response: The rendered HTML template for the index page.
    """
    return render_template("index.html")
if __name__ == "__main__":
    app.run(port=5000)
