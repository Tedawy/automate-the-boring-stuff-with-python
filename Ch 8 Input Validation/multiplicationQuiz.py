import pyinputplus as pyip
import random, time

numberOfQuestion = 10
correctAnswer = 0

for questionNumber in range(numberOfQuestion):
    #pick two random numbers:
    num1 = random.randint(0,9) 
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = %(questionNumber, num1, num2)'

    try:
        #Right answers are handled by allowregexes
        # Wrong answers are handled by blockregexes
        pyip.inputStr(prompt, allowRegexes=['^\s%' % (num1,num2)],blockRegexes=[('.*','Incorrect')], timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        #This block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswer +=1
    time.sleep(1) 

print(f'Score: {correctAnswer} / {numberOfQuestion}')