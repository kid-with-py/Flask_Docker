from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    incoming_data = request.json
    print(incoming_data, flush=True)


    import requests
    import json

    url = "http://app-2:5003"

    payload = json.dumps(incoming_data)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text, flush=True)
    return {
        "message": "success"
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)    