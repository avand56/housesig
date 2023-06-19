from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def time():

  # ts stores the time in seconds
  ts = time.time()
  return ts
