from flask import Flask
import time

app = Flask(__name__)


@app.route("/timestamp")
def time():

  # ts stores the time in seconds
  ts = time.time()
  return ts

if __name__ == '__main__':
    app.run()
