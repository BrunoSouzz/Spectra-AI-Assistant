#Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import logging
import os

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt or len(prompt.strip()) < 5:
        return jsonify({'error': 'Prompt is required and must be at least 5 characters long'}), 400
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        generated_text = response.text
        return jsonify({'generated_text': generated_text})
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)