from random import randint
from os import remove, rename

#get user's score by name
def getUserScore(userName):
    try:
        users = open('userScores.txt', 'r')
        for line in users:
            #split to name and score
            keyValue = line.split(',')
            #when name = userName, close file, return userScore
            if keyValue[0] == userName:
                users.close()
                return keyValue[1]
        users.close()
        return '-1'
    except IOError:
        print('\nFile userScore.txt not found and it\'ll be created.')
        users = open('userScores.txt', 'w')
        users.close()
        return '-1'

#updateScores
def updateUserPoints(newUser, userName, score):
    if newUser == False:
        userTemp = open('userScores.tmp', 'w')
        users = open('userScores.txt', 'r')
        for nameAndgrades in users:
            keyValue = nameAndgrades
            keyValue = keyValue.split(',')
            #change score while the name is the same
            if keyValue[0] == userName:
                keyValue[1] = str(score)
                userTemp.write(keyValue[0] + ', ' + keyValue[1] + '\n')
            else:
                userTemp.write(nameAndgrades)
        userTemp.close()
        users.close()
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
            
    else:
        users = open('userScores.txt', 'a')
        users.write('\n' + userName + ', ' + str(score))
        users.close()

    #math generate
def generateQuestion(score):
    operandList = [0, 0, 0, 0, 0]
    operatorList = ['', '', '', '']
    operatorDict = {
        1:'+',
        2:'-',
        3:'*',
        4:'/',
        5:'**'
    }
    result = 50001
    
    while result > 50000 or result < -50000:
        for i in range(0, 5):
            operandList[i] = randint(1, 9)

        #insure that there won't be a '**' nearing another 
        for i in range(0, 4):
            if i > 0 and operatorList[i-1] != '**':
                operatorList[i] = operatorDict[randint(1, 5)]
            else:
                operatorList[i] = operatorDict[randint(1, 4)]

        #Add bracket
        openBracket = randint(0, 3)
        closeBracket = randint(openBracket + 1, 4)

        if openBracket == 0:
            questionString = '(' + str(operandList[0])
        else:
            questionString = str(operandList[0])

        for i in range(1, 5):
            if i == openBracket:
                questionString = questionString + operatorList[i-1] + '(' + str(operandList[i])
            elif i == closeBracket:
                questionString = questionString + operatorList[i-1] + str(operandList[i]) + ')'
            else:
                questionString = questionString + operatorList[i-1] + str(operandList[i])
                
        result = round(eval(questionString), 2)
 
    questionString = questionString.replace('**', '^')
    print('Question: '+ questionString)
    
    while True:
        try:
            if float(input('Answer: ')) == result:
                score += 1
                print('You are right! Your score: '+ str(score))
                return score
            else:
                print('You are wrong! The right answer is: ' + str(result) + '\nYour score: '+ str(score))
                return score
        except ValueError:
            print('Wrong! Please enter the answer again:')
