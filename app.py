# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

results = {}

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

    name = request.form.to_dict(flat=False).get('name')[0]
    q1 = request.form.to_dict(flat=False).get('q1')
    q2 = request.form.to_dict(flat=False).get('q2')
    q3 = request.form.to_dict(flat=False).get('q3')
    q4 = request.form.to_dict(flat=False).get('q4')
    q5 = request.form.to_dict(flat=False).get('q5')

    if q1:
        q1_answers = ['F', 'j', 'c', 'Q', '1', '!', 'u', 'q', 'V', '5']
        (result, score)  = calculate_result(q1_answers, q1)
        if name:
            try:
                results[name][0] = score
            except:
                results[name] = [0,0,0,0,0,0]
                results[name][0] = score
        return jsonify({
            "Result" : result,
            "METHOD" : "POST"
        })
    elif q2:
        q2_answers = ['V', 'r', 's', 'I', '1', '!', 'e', 'k', 'F', '5']
        (result, score)  = calculate_result(q2_answers, q2)
        if name:
            try:
                results[name][1] = score
            except:
                results[name] = [0,0,0,0,0,0]
                results[name][1] = score
        return jsonify({
            "Result" : result,
            "METHOD" : "POST"
        })
    elif q3:
        q3_answers = ['Khoor', 'Cqrb rb j cnbc bnwcnwln!', "Qjy'x xjj nk ymnx nx ywfsxqfyji htwwjhyqd", '!!!!!', '12345 Nyrk rsflk eldsvij?', 'Dr!c cryevn gybu', 'hJmZ oZnOn', 'q', 'ocz izso ozno dn zhkot', '']
        (result, score) = calculate_result(q3_answers, q3)
        if name:
            try:
                results[name][2] = score
            except:
                results[name] = [0,0,0,0,0,0]
                results[name][2] = score
        return jsonify({
            "Result" : result,
            "METHOD" : "POST"
        })
    elif q4:
        q4_answers = ['Hello', 'This is a test sentence!', "Let's see if this is translated correctly", '!!!!!', '12345 What about numbers?', 'Th!s should work', 'mOrE tEsTs', 'a', 'the next test is empty', '']
        (result, score)  = calculate_result(q4_answers, q4)
        if name:
            try:
                results[name][3] = score
            except:
                results[name] = [0,0,0,0,0,0]
                results[name][3] = score
        return jsonify({
            "Result" : result,
            "METHOD" : "POST"
        })
    elif q5:
        q5_answers = ['This is a much longer message which we want to hide from people who may want to try and see what we are writing to each other!', 'Hello', 'This is a test sentence!', "Let's see if this is translated correctly", "!!!!!","12345 What about numbers?", "Th!s should work", "mOrE tEsTs", "a", "the next test is empty"]
        (result, score)  = calculate_result(q5_answers, q5)
        if name:
            try:
                results[name][4] = score
            except:
                results[name] = [0,0,0,0,0,0]
                results[name][4] = score
        return jsonify({
            "Result" : result,
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "Nothing found"
        })

@app.route('/functions/', methods=['POST'])
def functions():
    global results
    name = request.form.to_dict(flat=False).get('name')[0]
    q1 = request.form.to_dict(flat=False).get('q1')
    q2 = request.form.to_dict(flat=False).get('q2')
    q3 = request.form.to_dict(flat=False).get('q3')
    q4 = request.form.to_dict(flat=False).get('q4')
    q5 = request.form.to_dict(flat=False).get('q5')
    q6 = request.form.to_dict(flat=False).get('q6')
    
    print(name)
    if name == 'RESET_LEADERBOARD':
        print("Resetting leaderboard")
        results = {}
        return jsonify({
            "ERROR": "Leaderboard wiped"
        })
    else:
        if q1:
            q1_answers = ['Hello World']
            (result, score)  = calculate_result(q1_answers, q1)
            if name:
                try:
                    results[name][0] = score
                except:
                    results[name] = [0,0,0,0,0,0]
                    results[name][0] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q2:
            q2_answers = ['14', '0', '4', '56798', '38']
            (result, score)  = calculate_result(q2_answers, q2)
            if name:
                try:
                    results[name][1] = score
                except:
                    results[name] = [0,0,0,0,0,0]
                    results[name][1] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q3:
            q3_answers = ['3', '2', '0', '3', '0']
            (result, score) = calculate_result(q3_answers, q3)
            if name:
                try:
                    results[name][2] = score
                except:
                    results[name] = [0,0,0,0,0,0]
                    results[name][2] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q4:
            q4_answers = ['hll', 'cn y rmv ll f my vwls?', "Wht bt f  dd cptls?", 'R  JST PT N CPS LCK', '12345']
            (result, score)  = calculate_result(q4_answers, q4)
            if name:
                try:
                    results[name][3] = score
                except:
                    results[name] = [0,0,0,0,0,0]
                    results[name][3] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q5:
            q5_answers = ['hll', 'rmv', 'my', 'vwls', 'Wht', 'bt', 'cptls?', 'CPS', 'LCK', '12345']
            (result, score)  = calculate_result(q5_answers, q5)
            if name:
                try:
                    results[name][4] = score
                except:
                    results[name] = [0,0,0,0,0,0]
                    results[name][4] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q6:
            q6_answers = ['1','4','4','0','0']
            (result, score)  = calculate_result(q6_answers, q6)
            if name:
                try:
                    results[name][5] = score
                except:
                    results[name] = [0,0,0,0,0,0]
                    results[name][5] = score
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
        return ("Well done - all correct!", len(actual_answers))
    else:
        correct = len(actual_answers) - len(incorrect)
        total = len(actual_answers)
        return (f"You got {correct} out of {total}.\n You failed the following tests: {incorrect}.",correct)

# A welcome message to test our server
@app.route('/')
def index():
    scores = {}
    for key in results:
        scores[key] = sum(results[key])
    sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
    print(sorted_scores)
    result = "<h1 style=\"width: 50%;text-align: center;\">Python Leaderboard</h1><table  style=\"width: 50%;text-align: center;font-size: 30px;table-layout:fixed;\"><tr><th>Name</th><th>Score</th></tr>"
    for k in sorted_scores:
        result+= f"<tr><td>{k}</td><td>{sorted_scores[k]}</td></tr>"
    result += "</table>"
    return result

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
