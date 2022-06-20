from threading import Thread
from flask import Flask , render_template, request
import model as m
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 80)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

@app.route("/")
def index():
    param = 'Hello Everyone. We help you to find if you are suffering from Anxiety/Stress/Depression and suggest measures to control it or manage it.'
    thr = Thread(target=speak, args=[param])
    thr.start()
    return render_template("index.html")

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/form", methods = ["GET","POST"])
def model():
    if request.method == "POST":
        ##Anxiety Questions
        ans1 = request.form['q1']
        ans4 = request.form['q4']
        ans7 = request.form['q7']
        ans10 = request.form['q10']
        ans13 = request.form['q13']
        ans16 = request.form['q16']
        ans19 = request.form['q19']

        ##Depression Questions
        ans2 = request.form['q2']
        ans5 = request.form['q5']
        ans8 = request.form['q8']
        ans11 = request.form['q11']
        ans14 = request.form['q14']
        ans17 = request.form['q17']
        ans20 = request.form['q20']

        ##Stress Questions
        ans3 = request.form['q3']
        ans6 = request.form['q6']
        ans9 = request.form['q9']
        ans12 = request.form['q12']
        ans15 = request.form['q15']
        ans18 = request.form['q18']
        ans21 = request.form['q21']
    
        try:
            ans1 = float(ans1)
            ans2 = float(ans2)
            ans3 = float(ans3)
            ans4 = float(ans4)
            ans5 = float(ans5)
            ans6 = float(ans6)
            ans7 = float(ans7)
            ans8 = float(ans8)
            ans9 = float(ans9)
            ans10 = float(ans10)
            ans11 = float(ans11)
            ans12 = float(ans12)
            ans13 = float(ans13)
            ans14 = float(ans14)
            ans15 = float(ans15)
            ans16 = float(ans16)
            ans17 = float(ans17)
            ans18 = float(ans18)
            ans19 = float(ans19)
            ans20 = float(ans20)
            ans21 = float(ans21)
            global anxietyscore, stressscore, depressionscore
            anxietyscore = (ans1 + ans4 + ans7 + ans10 + ans13 + ans16 + ans19)*2
            depressionscore = (ans2 + ans5 + ans8 + ans11 + ans14 + ans17 + ans20)*2
            stressscore = (ans3 + ans6 + ans9 + ans12 + ans15 + ans18 + ans21)*2
            return render_template('result.html', result = anxietyscore, result1 = depressionscore, result2 = stressscore, calculation_success = True)
            
        except ValueError:
            return render_template(
                'form.html',
                result = "Bad Input",
                result1 = "Bad Input",
                result2 = "Bad Input",
                calculation_success = False,
                error = "Cannot perform the required calculation"
            )
    return render_template("form.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form1", methods = ["GET","POST"])
def model1():
    if request.method == "POST":
        in1 = request.form['x1']
        in2 = request.form['x2']
        in3 = request.form['x3']
        in4 = request.form['x4']
        in5 = request.form['x5']
        in6 = request.form['x6']
        in7 = request.form['x7']
        in8 = request.form['x8']
        in9 = request.form['x9']
        in10 = request.form['x10']
        in11 = request.form['x11']
        in12 = request.form['x12']
        in13 = request.form['x13']

        try:
            in1 = float(in1)
            in2 = float(in2)
            in3 = float(in3)
            in4 = float(in4)
            in5 = float(in5)
            in6 = float(in6)
            in7 = float(in7)
            in8 = float(in8)
            in9 = float(in9)
            in10 = float(in10)
            in11 = float(in11)
            in12 = float(in12)
            in13 = float(in13)
            answer = m.anxiety_pred(in1, in2, in3, in4, in5, in6, in7, in8, in9, in10, in11, in12, in13, anxietyscore)
            answer1 = m.stress_pred(in1, in2, in3, in4, in5, in6, in7, in8, in9, in10, in11, in12, in13, stressscore)
            answer2 = m.depression_pred(in1, in2, in3, in4, in5, in6, in7, in8, in9, in10, in11, in12, in13, depressionscore)
            print(answer)
            print(answer1)
            print(answer2)
            return render_template("result1.html", my_answer = answer, my_answer1 = answer1, my_answer2 = answer2, calculation_success = True)
        except ValueError:
            return render_template("form1.html",
            my_answer = "Bad Input",
            calculation_success=False)
    return render_template("form1.html")


if __name__ == "__main__":
    app.run(debug=True)