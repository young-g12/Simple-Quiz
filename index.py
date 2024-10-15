def loop()
  while True
    questionNumberOne = "What is the name for a fear of spiders?"
    answerOne = {
      "A": "Aquaphobia",
      "B": "Mysophobia",
      "C": "Claustrophobia",
      "D": "Arachnophobia"
    }
    print(answerOne)
    if input(questionNumberOne).lower() == "d":
        print("correct")
    else:
        print("incorrect")
    
    
    questionNumberTwo = "Who is the first person to step on the moon?"
    answerTwo = {
      "A": "Neil Armstrong",
      "B": "Yuri Gagarin",
      "C": "Alan Shepard",
      "D": "John Glen"
    }
    print(answerTwo)
    if input(questionNumberTwo).lower() == "a":
        print("correct")
    else:
        print("incorrect")
    
    
    questionNumberThree = "Who is the first person to sail around the world?"
    answerThree = {
      "A": "Christopher Columbus",
      "B": "Zheng He",
      "C": "Ferdinand Magellan",
      "D": "John Cabot"
    }
    print(answerThree)
    if input(questionNumberThree).lower() == "c":
        print("correct")
    else:
        print("incorrect")
    
    
    questionNumberFour = "How many days are in a leap year?"
    answerFour = {
      "A": "1000",
      "B": "275",
      "C": "365",
      "D": "366"
    }
    print(answerFour)
    if input(questionNumberFour).lower() == "d":
        print("correct")
    else:
        print("incorrect")
    
    
    questionNumberFive = "What mammal lays eggs?"
    answerFive = {
      "A": "Platypuses",
      "B": "Sharks",
      "C": "Humans",
      "D": "Dolphins"
    }
    print(answerFive)
    if input(questionNumberFive).lower() == "a":
        print("correct")
    else:
        print("incorrect")

playAgain = input("If you would like to play again, please type 'yes'. Otherwise, type 'no':")

if playAgain.lower() != "yes":
  print("Good Job, keep studying!")
  break

loop()
