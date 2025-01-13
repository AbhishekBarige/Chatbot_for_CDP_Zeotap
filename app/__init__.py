from flask import Flask, render_template, request, jsonify
from app.chatbot import handle_query

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/query')
    def query():
        user_query = request.args.get('text')
        response = handle_query(user_query)
        return jsonify({"answer": response})

    return app

