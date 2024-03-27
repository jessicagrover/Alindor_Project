# from flask import Flask, render_template, request
# import openai

# app = Flask(__name__)
# openai.api_key = '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'

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/summarize', methods=['POST'])
# def summarize_dialogue():
#     if 'file' not in request.files:
#         return render_template('index.html', error='No file uploaded')

#     file = request.files['file']

#     if file.filename == '':
#         return render_template('index.html', error='No file selected')

#     if file:
#         dialogues = file.read().decode('utf-8')

#         try:
#             response = openai.Completion.create(
#                 engine="davinci-002",
#                 prompt=dialogues,
#                 temperature=0.6,
#                 max_tokens=150
#             )
#             result = response.choices[0].text.strip()
#             return render_template('index.html', result=result)
#         except Exception as e:
#             return render_template('index.html', error=f'Error processing dialogue: {str(e)}')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import openai
import requests

app = Flask(__name__)
openai.api_key = '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'
deepgram_api_key = 'your_deepgram_api_key'

@app.route('/')
def home():
    return render_template('index.html')

def transcribe_audio(audio_file):
    url = 'https://api.deepgram.com/v1/listen'
    headers = {'Authorization': f'Token {deepgram_api_key}'}
    files = {'content': audio_file}
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        result = response.json()
        if result.get('status') == 'success':
            return result['results'][0]['alternatives'][0]['transcript']
    raise Exception('Failed to transcribe audio')

@app.route('/summarize', methods=['POST'])
def summarize_dialogue():
    if 'file' not in request.files:
        return render_template('index.html', error='No file uploaded')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No file selected')

    if file.filename.endswith(('.wav', '.mp3')):
        try:
            dialogues = transcribe_audio(file)
        except Exception as e:
            return render_template('index.html', error=f'Error processing audio: {str(e)}')
    else:
        dialogues = file.read().decode('utf-8')

    try:
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=dialogues,
            temperature=0.6,
            max_tokens=150
        )
        result = response.choices[0].text.strip()
        return render_template('index.html', result=result)
    except Exception as e:
        return render_template('index.html', error=f'Error processing dialogue: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
