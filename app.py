from flask import Flask, request
import requests
import time
from rembg import remove, new_session

app = Flask(__name__)

@app.route('/')
def hello():
    return 'API is working!'
    
@app.route('/remove', methods=['POST'])
def remove_bg():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        now = str(time.time())
        url = json['url']
        data = requests.get(url).content
        f = open(now + '.jpg','wb')
        f.write(data)
        f.close()

        input_path = './' + now + '.jpg'
        output_path = './static/' + now + '.png'

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                model_name = "u2net_human_seg"
                session = new_session(model_name)
                output = remove(input, session=session)
                o.write(output)
        return now + '.png'
    else:
        return 'Content-Type not supported!'