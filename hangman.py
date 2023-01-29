import random
from words import words
def get_word():
    word=random.choice(words)
    return word.upper()
def play(word):
    full_word="_"*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6
    print("Let's play Hangman")
    print(hangman_tries(tries))
    print(full_word)
    print("Length of word:"+str(len(word)))
    print("\n")
    while not guessed and tries>0:
        guess=input("Please Enter a letter or word:").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter")
            elif guess not in word:
                print("Ohh! You guessed wrong letter :(")
                guessed_letters.append(guess)
                tries-=1
            else:
                print("Good Job :)")
                guessed_letters.append(guess)
                word_as_list=list(full_word)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for i in indices:
                    word_as_list[i]=guess
                full_word="".join(word_as_list)
                if '_' not in full_word:
                    guessed=True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed this word");
            elif guess!=word:
                print("Ohh! You guessed wrong word :(")
                tries-=1
                guessed_words.append(guess)
            else:
                print("****")
                guessed=True
                full_word=word;
        else:
            print("Not a valid guess :(")
        print(hangman_tries(tries))
        print(full_word)
        print("\n")
    if guessed:
        print("Hurray! You won the game")
    else:
        print("Ohh! You lost the game. The word was "+word)


def hangman_tries(tries):
    body=[
        """
            ---------------
            |        |
            |        O
            |       \|/
            |         |
            |       / \\
            |
            |

        """,
        """
            ---------------
            |        |
            |        O
            |       \|/
            |         |
            |       / 
            |
            |
        """,
        """
             ---------------
            |        |
            |        O
            |       \|/
            |        |
            |       
            |
        """,
        """
             ---------------
            |        |
            |        O
            |       \|
            |        |
            |      
            |
        """,
        """
             ---------------
            |        |
            |        O
            |        |
            |        |
            |      
            |
        """,
        """
             ---------------
            |        |
            |        O
            |     
            |     
            |    
            |
            |
        """,
        """
             ---------------
            |        |
            |       
            |       
            |       
            |       
            |
        """
    ]
    return body[tries]
def main():
    print("-----")
    word_input=get_word()
    play(word_input)
    while input("You want to play Again:(Y/N)").upper()=="Y":
        word=get_word()
        play(word_input)
if __name__ =="__main__":
    main()
