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
    param = request.form.get('name')
    print(param)

    q1 = request.form.get('q1')
    print(len(q1))
    print(request.form)
    q1 = request.form.to_dict(flat=False).get('q1')
    print(q1)
    
    answers = ['F', 'j', 'c', 'Q']
    incorrect = []
    for i in range(len(q1)):
        if q1[i] != answers[i]:
            incorrect.append(i)

    if len(incorrect) == 0:
        result = "Well done - all correct!"
    else:
        correct = len(answers) - len(incorrect)
        total = len(answers)
        result = f"You got {correct} out of {total}. You got questions {incorrect} wrong."

    if(q1):
        return jsonify({
                "Result": result
                "METHOD": "POST"
            })
    
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {param} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
