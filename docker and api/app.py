from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def get_current_time_and_text():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = {
        "current_time": current_time,
        "Message": "Automate, All The Things!"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
