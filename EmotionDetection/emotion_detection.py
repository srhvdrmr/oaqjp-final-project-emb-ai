import requests
import json


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    formatted_response = json.loads(response.text)

    emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})

    emotion_scores = {
        "anger": emotions.get("anger", 0.0),
        "disgust": emotions.get("disgust", 0.0),
        "fear": emotions.get("fear", 0.0),
        "joy": emotions.get("joy", 0.0),
        "sadness": emotions.get("sadness", 0.0),
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores
