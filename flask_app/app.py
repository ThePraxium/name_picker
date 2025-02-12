from flask import Flask, render_template, jsonify, request
import students  # Import students.py for local student selection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choose_student', methods=['POST'])
def choose_student():
    try:
        chosen_student = students.choose_student()  # Calls students.py function
        if chosen_student is None:
            return jsonify({'message': "No students available to choose."})  # Handle empty case
        return jsonify({'student': chosen_student})  # Return the chosen student
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reset_list', methods=['POST'])
def reset_list():
    try:
        students.reset_list()  # Calls reset function from students.py
        return jsonify({'message': "Student answered list has been reset."})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)