from flask import Flask, send_file, request, jsonify
from flask_cors import CORS
import anthropic
import os
from dotenv import load_dotenv

load_dotenv('/Users/pallavi/AlgoSphere/.env')

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_file('/Users/pallavi/AlgoSphere/dashboard.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    context = data.get('context', '')

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"""You are a DeFi AI assistant inside AlgoSphere,
a risk monitoring platform on Algorand blockchain.
Be concise, specific and actionable. Max 80 words.

{context}

Question: {message}"""
        }]
    )
    return jsonify({"reply": response.content[0].text})

if __name__ == '__main__':
    app.run(debug=True, port=5000)