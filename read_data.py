from flask import Flask, request

app2 = Flask(__name__)


@app.route("/readdata",  methods = ['POST'])
def read_data():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        return json

if __name__ == '__main__':
    app2.run()
