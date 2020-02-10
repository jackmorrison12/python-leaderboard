# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():

    q1 = request.form.to_dict(flat=False).get('q1')
    
    if q1:
        q1_answers = ['F', 'j', 'c', 'Q']
        result = calculate_result(q1_answers, q1)
        return jsonify({
            "Result" : result,
            "METHOD" : "POST"
        })

    else:
        return jsonify({
            "ERROR": "Nothing found"
        })

def calculate_result(actual_answers, student_answers):
    incorrect = []
    for i in range(len(student_answers)):
        if student_answers[i] != actual_answers[i]:
            incorrect.append(i + 1)

    if len(incorrect) == 0:
        return "Well done - all correct!"
    else:
        correct = len(actual_answers) - len(incorrect)
        total = len(actual_answers)
        return f"You got {correct} out of {total}. You got the following tests wrong: {incorrect}."

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
