from flask import Blueprint, request, jsonify, render_template
from .rag_utils import query_rag, MODEL_READY

main = Blueprint('main', __name__)

AUTHORIZED_STUDENTS = {
    f"student{str(i).zfill(2)}": f"pass{i:02d}" for i in range(1, 51)
}

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/api/daily_directive', methods=['GET'])
def daily_directive():
    if not MODEL_READY:
        return jsonify({"error": "Model backend not available"}), 503
    student_id = request.args.get('student_id', default=None, type=str)
    token = request.args.get('token', default=None, type=str)
    if not student_id or not token:
        return jsonify({"error": "Missing student_id or token"}), 400
    if student_id not in AUTHORIZED_STUDENTS or AUTHORIZED_STUDENTS[student_id] != token:
        return jsonify({"error": "Unauthorized access"}), 403

    user_query = f"Generate a daily directive for Artemis DSAI student {student_id}. Include 1 mission goal and 1 reminder."
    try:
        answer, context = query_rag(user_query)
        return jsonify({
            "student_id": student_id,
            "directive": answer.strip(),
            "context_snippet": context[:300]
        })
    except Exception as e:
        return jsonify({"error": "Model query failed", "details": str(e)}), 500

@main.route('/api/ask', methods=['GET'])
def ask_anything():
    if not MODEL_READY:
        return jsonify({"error": "Model backend not available"}), 503
    student_id = request.args.get('student_id', default=None, type=str)
    token = request.args.get('token', default=None, type=str)
    user_query = request.args.get('q', default="What is the camp about?", type=str)
    if not student_id or not token:
        return jsonify({"error": "Missing student_id or token"}), 400
    if student_id not in AUTHORIZED_STUDENTS or AUTHORIZED_STUDENTS[student_id] != token:
        return jsonify({"error": "Unauthorized access"}), 403

    prompt = f"Student ID: {student_id}\nQuestion: {user_query}"
    try:
        answer, context = query_rag(prompt)
        return jsonify({
            "student_id": student_id,
            "question": user_query,
            "answer": answer.strip(),
            "context_snippet": context[:300]
        })
    except Exception as e:
        return jsonify({"error": "Model query failed", "details": str(e)}), 500
