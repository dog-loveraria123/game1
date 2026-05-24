import pgzrun
Questions=[]
WIDTH=500
HEIGHT=500
TITLE='Quizmaster'
welcomebox=Rect(0,0,500,50)
questionbox=Rect(25,100,450,50)
answerbox1=Rect(25,200,100,100)
answerbox2=Rect(250,200,100,100)
answerbox3=Rect(250,330,100,100)
answerbox4=Rect(25,330,100,100)
timerbox=Rect(400,200,75,75)
skipbox=Rect(400,330,75,75)
def draw():
    screen.draw.filled_rect(skipbox,"red")
    screen.draw.filled_rect(timerbox,'red')
    screen.draw.filled_rect(answerbox4,'blue')
    screen.draw.filled_rect(answerbox3,'blue')
    screen.draw.filled_rect(answerbox2,'blue')
    screen.draw.filled_rect(answerbox1,'blue')
    screen.draw.filled_rect(questionbox,'yellow')
    screen.draw.filled_rect(welcomebox,'blue')
    screen.draw.textbox(str(10),timerbox,color='black')
    screen.draw.textbox('Skip',skipbox,color='black')
    screen.draw.textbox("Welcome to quizmaster!",welcomebox,color='black')
    screen.draw.textbox(question[0],questionbox,color='black')
    screen.draw.textbox(question[1],answerbox1,color='black')
    screen.draw.textbox(question[2],answerbox2,color='black')
    screen.draw.textbox(question[3],answerbox3,color='black')
    screen.draw.textbox(question[4],answerbox4,color='black')
def readquestion():
    global Questions
    rq=open('questions.txt','r',)
    for i in rq:
        Questions.append(i)
    rq.close()
readquestion()
def questionsalone():
    return Questions.pop(0).split('|')
question=questionsalone()
pgzrun.go()