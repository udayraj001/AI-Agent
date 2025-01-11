from flask import Flask, request, jsonify
from .utils import search_wikipedia, fetch_real_time_data
from .agent import ask_ai

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    if not question:
        return jsonify({"error": "No question provided."}), 400

    # Fetch Wikipedia Summary
    wiki_summary = search_wikipedia(question)
    real_time_data = fetch_real_time_data(question)
    ai_answer = ask_ai(question, context=wiki_summary)

    return jsonify({
        "question": question,
        "wikipedia": wiki_summary,
        "real_time_data": real_time_data,
        "ai_answer": ai_answer
    })
