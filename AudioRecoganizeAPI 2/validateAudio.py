from pydub import AudioSegment
from io import BytesIO

def convert_m4a_to_wav(audio_content, outputfile):
    audio = AudioSegment.from_file(audio_content, format="m4a")
    return audio.export(outputfile, format="wav")

def ValidateAudio(audio_content):
    file_obj = BytesIO(audio_content)
    
    # Write the BytesIO content to a temporary file
    with open("temp.m4a", "wb") as f:
        f.write(audio_content)

    filename = "temp.m4a"
    outputfile = "outputfile.wav"

    if filename.endswith(".m4a"):
        x = convert_m4a_to_wav(filename, outputfile)
        print(x)
        return x
