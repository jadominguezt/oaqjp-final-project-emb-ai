""" 
Import requires libraries
"""
import requests
import json

"""
Function to run the emotion detection analysis
"""
def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers with the required data for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the response from the API
    result_response = json.loads(response.text)
    emotions_dict = result_response['emotionPredictions'][0]['emotion']
    anger   = emotions_dict['anger']
    disgust = emotions_dict['disgust']
    fear    = emotions_dict['fear']
    joy     = emotions_dict['joy']
    sadness = emotions_dict['sadness']
    
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    dominant_emotion_score = emotions_dict[dominant_emotion]
    emotions_dict['dominant_emotion'] = dominant_emotion
    
    # Print the response
    print(emotions_dict)