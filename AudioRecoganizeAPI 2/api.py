from flask import Flask,request
from flask_restful import Resource,Api

import speech_recognition as sr
from pydub import AudioSegment

from CheckTheText import IsDataThere
# from validateAudio import ValidateAudio


app=Flask(__name__)
api=Api(app)
    
    
class AudioRecoganize(Resource):
    # def get(self,userId):
    #     return {'data':'Hello pemmi userid5'}
    def post(self,userId):
        r = sr.Recognizer()
        audio_file = request.files.get('audio_file')

        if not audio_file:
            return {'message': 'No file uploaded'}, 400
        # sound=ValidateAudio(audio_file)
        # print(sound,'--------------')
        with sr.AudioFile(audio_file) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text=r.recognize_google(audio)
                response=IsDataThere(text)
                
                return response ,200

            except Exception as e:
                print(e)
        return {'message':"success"}
# api.add_resource(HelloWorld,'/helloworld')
api.add_resource(AudioRecoganize,'/audio_recoganize/<int:userId>')
if __name__=="__main__":
    app.run(debug=True)
