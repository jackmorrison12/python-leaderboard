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

@app.route('/methods/', methods=['POST'])
def methods():
    global results
    name = request.form.to_dict(flat=False).get('name')[0]
    q1 = request.form.to_dict(flat=False).get('q1')
    q2 = request.form.to_dict(flat=False).get('q2')
    q3 = request.form.to_dict(flat=False).get('q3')
    q4 = request.form.to_dict(flat=False).get('q4')
    q5 = request.form.to_dict(flat=False).get('q5')
    q6 = request.form.to_dict(flat=False).get('q6')
    q7 = request.form.to_dict(flat=False).get('q7')
    q8 = request.form.to_dict(flat=False).get('q8')
    
    print(name)
    if name == 'RESET_LEADERBOARD':
        print("Resetting leaderboard")
        results = {}
        return jsonify({
            "ERROR": "Leaderboard wiped"
        })
    else:
        if q1:
            q1_answers = ['HELLO', 'TEST 2', 'WHAT IF IT\'S ALREADY CAPITALISED?', 'OR BOTH?', '12345']
            (result, score)  = calculate_result(q1_answers, q1)
            if name:
                try:
                    results[name][0] = score
                except:
                    results[name] = [0,0,0,0,0,0,0,0]
                    results[name][0] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q2:
            q2_answers = ['HELLO','hello!', 'WhAt AbOuT tHiS?', '', '12345']
            (result, score)  = calculate_result(q2_answers, q2)
            if name:
                try:
                    results[name][1] = score
                except:
                    results[name] = [0,0,0,0,0,0,0,0]
                    results[name][1] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q3:
            q3_answers = ['1, 2, 3, 4', "'Hi'", "1, 'Test'", '1, 1', "'What about weird indices?'", '1, 2, 3, 4, 2', "1, 'Hi'", "'', ' '", '100, 100', "'Did', 'you get them all right?'"]
            print(q3)
            print(q3_answers)
            (result, score) = calculate_result(q3_answers, q3)
            if name:
                try:
                    results[name][2] = score
                except:
                    results[name] = [0,0,0,0,0,0,0,0]
                    results[name][2] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q4:
            q4_answers =['olleh', 'hello', 'therehello', 'hellothere', '12345', 'h', '', 'b2a1', 'fInAl', 'well done!']
            (result, score)  = calculate_result(q4_answers, q4)
            if name:
                try:
                    results[name][3] = score
                except:
                    results[name] = [0,0,0,0,0,0,0,0]
                    results[name][3] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q5:
            q5_answers = ['True, True, False', 'True, True, True', 'False, False, False', 'False, False', 'False, False, False, False', '', 'False', 'False', 'False', 'True, False', 'True', 'False', 'False', 'True', 'False, True, True, False']
            (result, score)  = calculate_result(q5_answers, q5)
            if name:
                try:
                    results[name][4] = score
                except:
                    results[name] = [0,0,0,0,0,0,0,0]
                    results[name][4] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q6:
            q6_answers = ['329.0', '265.6', '147.0', '0', '239.86046511627907', '250.28571428571428', '366.0', '270.0', '151.5', '189.0', '108.0', '247.02439024390245', '232.0', '246.0', '243.95555555555555']
            (result, score)  = calculate_result(q6_answers, q6)
            if name:
                try:
                    results[name][5] = score
                except:
                    results[name] = [0,0,0,0,0,0,0,0]
                    results[name][5] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q7:
            q7_answers = ['0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', '1, 0, 0, 1, 5, 1, 4, 1, 4, 0, 0, 2, 0, 2, 2, 0, 0, 4, 3, 4, 0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', '2, 1, 3, 1, 5, 0, 2, 1, 2, 0, 1, 2, 0, 3, 3, 0, 0, 1, 1, 3, 2, 0, 0, 0, 1, 0', '0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', '11, 0, 0, 10, 0, 10, 0, 10, 0, 11, 10, 11, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0', '50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', '3, 0, 1, 1, 6, 0, 3, 5, 4, 0, 1, 3, 3, 5, 5, 0, 0, 1, 3, 7, 2, 0, 1, 0, 1, 0', '2, 0, 1, 0, 5, 4, 1, 1, 3, 0, 0, 2, 1, 1, 4, 0, 0, 3, 2, 2, 3, 0, 0, 0, 1, 0', '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0', '1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1', '1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0']
            (result, score)  = calculate_result(q7_answers, q7)
            if name:
                try:
                    results[name][6] = score
                except:
                    results[name] = [0,0,0,0,0,0,0,0]
                    results[name][6] = score
            return jsonify({
                "Result" : result,
                "METHOD" : "POST"
            })
        elif q8:
            q8_answers = ["'t', 'a'", "'t', 'a'", "'a', 'a'", "'a', 'a'", "'e', 'b'", "'h', 'a'", "'z', 'a'", "'z', 'a'", "'a', 'a'", "'a', 'a'", "'a', 'a'", "'e', 'f'", "'e', 'a'", "'a', 'b'", "'a', 'b'", "'t', 'b'", "'e', 'b'", "'a', 'a'", "'a', 'a'", "'a', 'b'"]
            (result, score)  = calculate_result(q8_answers, q8)
            if name:
                try:
                    results[name][7] = score
                except:
                    results[name] = [0,0,0,0,0,0,0,0]
                    results[name][7] = score
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
            print("ERROR")
            print("S:", student_answers[i])
            print("A:", actual_answers[i])
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
