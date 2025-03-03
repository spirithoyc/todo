from flask import Flask, request, jsonify, render_template
import os
import json
from datetime import datetime

app = Flask(__name__)
data_file = 'todos.json'  # Change this to your EC2 attached storage path

def load_todos():
    return [{"id": 123, "task": "test", "state": "todo"}]

@app.route('/')
def index():
    todos = load_todos()
    print("TTTTTT")
    return "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Todo List</title><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\"></head><body><div class=\"container mt-5\"><h1>Todo List</h1></div></body></html>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')