import random
class Mastermind:
    def __init__(self):
        self.secret_number=None
    def set_secret_number(self):
        self.secret_number=str(random.randint(1000, 9999))
    def get_hints(self,guess):
        hints=[]
        for i,digit in enumerate(guess):
            if digit==self.secret_number[i]:
                hints.append(digit)
            elif digit in self.secret_number:
                hints.append('*')
            else:
                hints.append('-')
        return hints

    def play(self):
        self.set_secret_number()
        attempts=0

        while True:
            attempts+=1
            guess=input("Make your guess: ")

            if guess==self.secret_number:
                print("Congratulations! You guessed the secret number {} in {} attempts !!".format(self.secret_number,attempts))
                play_again=input("Do you want to play again? (yes/no): ").lower()
                if play_again=='yes':
                    print("\nLet's play again!\n")
                    Mastermind()
                elif play_again=='no':
                      print("Thanks for playing. Goodbye!")
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                break
            else:
                hints=self.get_hints(guess)
                print("Hints:",' '.join(hints))

if __name__=="__main__":
    game=Mastermind()
    game.play()
