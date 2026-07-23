"""
Flask Backend for AI Text Detection System

Description:
Provides REST API endpoints for AI vs Human text classification,
real-time monitoring, and user feedback.
"""
from flask import Flask, request, jsonify, send_file # Import send_file
import os 
from predictor import *

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    texts = data.get("texts", [])
    prediction_strategy = "default"
    predictions = predict_batch(texts, prediction_strategy)

@app.route("/monitor", methods=["GET"])
def monitor():
    # Returns monitoring information
    return jsonify({
        "summary": dict(monitor_stats),
        "recent_logs": monitor_logs[-50:] # Limit to last 50 logs for performance
    })

# Returns monitoring statistics
@app.route("/get_monitor_stats", methods=["GET"])
def get_monitor_stats():
    return jsonify(dict(monitor_stats))

# Returns monitoring logs
@app.route("/get_monitor_logs", methods=["GET"])
def get_monitor_logs():
    return jsonify(monitor_logs) # Return all logs for table processing on client side

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    text = data.get("text")
    predicted_label = data.get("predicted_label")
    user_feedback = data.get("user_feedback")

    if not all([text, predicted_label, user_feedback]):
        return jsonify({"status": "error", "message": "Missing required feedback data."}), 400

    log_feedback(text, predicted_label, user_feedback)

    return jsonify({"status": "success", "message": "Feedback received!"}), 200

@app.route("/feedback_summary", methods=["GET"])
def feedback_summary():
    return jsonify({"feedback_data": feedback_logs})

@app.route("/download_feedback_logs", methods=["GET"])
def download_feedback_logs():
    if os.path.exists("feedback_logs.json"):
        return send_file("feedback_logs.json", as_attachment=True, download_name="feedback_logs.json", mimetype="application/json")
    return jsonify({"status": "error", "message": "Feedback logs file not found."}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
