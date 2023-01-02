from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/')
def index():
    incoming_data = request.json
    print(incoming_data, flush=True)
    data = incoming_data

    with open('data.json', 'w') as f:
        json.dump(incoming_data, f)
        print("line12", flush=True)
        print(data, flush=True)

    
    return {
        "message": "success"
    }
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)    
