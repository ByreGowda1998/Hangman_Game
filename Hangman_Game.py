                       #   Project  -  HANGMAN
                      
                      
'''
These Project involves in two persons 
1st person  called as "challenger" one who enters the "word"
and second person  called as "contender" who identifies the word by entering 
characterstics of the word .contender gets chances that are two times 
the no of the characters of the "word" (chances=2* characters of the "word")
within these chances contenders should be identified word 
if contender identifies the word  within given chances he will win else
challengers wins 
'''  


challengers_word=input("enter the word : ").lower()  # taking input from the challenger and convertin all into lower_case

chances=len(challengers_word)*2                 # Creating Total_no of chanches for guessing


word=list(challengers_word)
correct_guess=[]                                    # creating empty list for correctguessing

while chances > 0 :
    users_input=input("Guess the character : ").lower()    # Taking inputs from contender
    if users_input in word :
        word.remove(users_input)
        correct_guess.append(users_input)
        print(f"Good you have enterd correct character :{correct_guess}")
        if len(word) ==0:
            print("Congratulation you won 🤩")
            break
        else:
            print(f"you have left {chances} chances to guess the correct word")
    
    else:
        chances-=1
        print("your wrong")
        print(f"you left these many chnces {chances} for guessing")
        print(f"your correct guesses are {correct_guess}")
        if chances==0:
            print("You lost the game better luck next time 😟")
        