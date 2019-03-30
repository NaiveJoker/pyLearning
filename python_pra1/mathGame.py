try:
    #get user's name and scores
    import myPythonFunction as m
    userName = input("Please input your name: ")
    userScore = int(m.getUserScore(userName))
    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False

    #input and output
    userChoice = 0
    while userChoice != '0':
        userScore = m.generateQuestion(userScore)
        userChoice = input('Input your choice(1: continue / 0: stop): ')
    m.updateUserPoints(newUser, userName, userScore)
except ValueError:
    print('Wrong input!')
