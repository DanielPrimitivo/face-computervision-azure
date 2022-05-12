from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from flask import Flask, render_template, request

app = Flask(__name__)

KEY_FACE = "___"
ENDPOINT_FACE = "https://progiaface.cognitiveservices.azure.com/"
KEY_COMPUTER_VISION = "___"
ENDPOINT_COMPUTER_VISION = "https://progiacomputervision.cognitiveservices.azure.com/"

face_client = FaceClient(ENDPOINT_FACE, CognitiveServicesCredentials(KEY_FACE))
vision_client = ComputerVisionClient(ENDPOINT_COMPUTER_VISION, CognitiveServicesCredentials(KEY_COMPUTER_VISION))

def get_emotion(emotion):
    emotions = dict()
    emotions['anger'] = emotion.anger
    emotions['contempt'] = emotion.contempt
    emotions['disgust'] = emotion.disgust
    emotions['fear'] = emotion.fear
    emotions['happiness'] = emotion.happiness
    emotions['neutral'] = emotion.neutral
    emotions['sadness'] = emotion.sadness
    emotions['surprise'] = emotion.surprise
    emotion_name = max(emotions, key=emotions.get)
    emotion_level = emotions[emotion_name]

    return emotion_name, emotion_level
    

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST',])
def get_text():
    if request.method == 'POST':
        urlImage = request.form['url']
        face_attributes = ['age', 'emotion']
        
        detected_faces = face_client.face.detect_with_url(url=urlImage, return_face_attributes=face_attributes, detection_model='detection_01', recognition_model='recognition_04')
        
        if not detected_faces:
            raise Exception('No hay caras detectadas')
        
        emotions = []
        for face in detected_faces:
            emotion_name, emotion_level = get_emotion(face.face_attributes.emotion)
            emotions.append({emotion_name, emotion_level})

        image_analysis = vision_client.analyze_image(urlImage, visual_features=[VisualFeatureTypes.tags, VisualFeatureTypes.color, VisualFeatureTypes.description])

        for caption in image_analysis.description.captions:
            image_description = caption.text

        return render_template('results.html', faces=detected_faces, emotions=emotions, tags=image_analysis.tags, accentColor=image_analysis.color.accent_color, description=image_description)

if __name__ == '__main__':
    app.run(debug = True)
