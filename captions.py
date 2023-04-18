from flask import Flask, request, json
import random
import requests
import time
import pdb
from captioner import generate_caption

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/caption', methods=['POST', 'GET'])
def caption():
    if request.method == 'GET':
        words = ['octopus', 'dog', 'deadmau5', 'bed', 'computer', 'laptop', 'window', 'music']
        print("USING FAKE CAPTION")
        caption = random.choice(words) + " and " + random.choice(words)
    else:
        print(request.json)
        url = request.json['url']
        print("DOWNLOADING IMAGE")
        img_data = requests.get(url).content
        file_name = "images/" + time.strftime('%Y-%m-%dT%H:%M:%S.jpg', time.localtime())
        with open(file_name, 'wb') as handler:
            handler.write(img_data)

        print("GENERATING CAPTION")
        caption = generate_caption(file_name)

    print("CAPTION: " + caption)
    data = { "caption": caption }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    print(data)
    print(response)
    return response
