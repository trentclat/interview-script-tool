from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

class InterviewSession:
    def __init__(self):
        self.responses = []
        self.questions = self.load_questions()
        self.current_category = None
        self.current_question_index = 0
        self.current_question = self.get_first_question()

    def load_questions(self):
        questions = []
        with open('interview_questions.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    if line.startswith('[') and line.endswith(']'):
                        current_category = line[1:-1]
                    elif current_category:
                        questions.append({
                            'category': current_category,
                            'question': line
                        })
        return questions

    def get_first_question(self):
        if self.questions:
            self.current_category = self.questions[0]['category']
            return self.questions[0]['question']
        return "No questions available"

    def get_next_question(self, current_answer):
        # Store the current response
        if self.current_question_index < len(self.questions):
            self.responses.append({
                "question": self.questions[self.current_question_index]['question'],
                "answer": current_answer,
                "category": self.questions[self.current_question_index]['category'],
                "timestamp": datetime.now().isoformat()
            })
        
        # Move to next question
        self.current_question_index += 1
        
        # If we have more questions, return the next one
        if self.current_question_index < len(self.questions):
            self.current_category = self.questions[self.current_question_index]['category']
            return self.questions[self.current_question_index]['question']
        
        # If we're done with all questions
        return "Thank you for completing the interview! Would you like to add any final thoughts?"

    def generate_markdown(self):
        markdown = "# Technology Interview Transcript\n\n"
        markdown += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Group responses by category
        current_category = None
        for response in self.responses:
            if response['category'] != current_category:
                current_category = response['category']
                markdown += f"## {current_category.replace('_', ' ')}\n\n"
            markdown += f"### Q: {response['question']}\n"
            markdown += f"A: {response['answer']}\n\n"
        
        return markdown

# Store active interview sessions
sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_interview', methods=['POST'])
def start_interview():
    session_id = datetime.now().strftime('%Y%m%d%H%M%S')
    sessions[session_id] = InterviewSession()
    return jsonify({
        'session_id': session_id,
        'first_question': sessions[session_id].current_question
    })

@app.route('/process_response', methods=['POST'])
def process_response():
    data = request.json
    session_id = data['session_id']
    answer = data['answer']
    
    session = sessions.get(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404
    
    next_question = session.get_next_question(answer)
    
    return jsonify({
        'next_question': next_question
    })

@app.route('/get_transcript', methods=['POST'])
def get_transcript():
    data = request.json
    session_id = data['session_id']
    
    session = sessions.get(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404
    
    markdown_content = session.generate_markdown()
    return jsonify({
        'markdown': markdown_content
    })

if __name__ == '__main__':
    app.run(debug=True)