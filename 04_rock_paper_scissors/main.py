import secrets

CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def result(user, computer):
    if user == computer: return "tie"
    return "win" if BEATS[user] == computer else "lose"

def main():
    user_score = computer_score = 0
    while True:
        user = input("Rock, paper or scissors (or quit): ").strip().lower()
        if user == "quit": break
        if user not in CHOICES:
            print("Choose rock, paper or scissors."); continue
        computer = secrets.choice(CHOICES)
        outcome = result(user, computer)
        print(f"You: {user}; computer: {computer}. You {outcome}.")
        if outcome == "win": user_score += 1
        elif outcome == "lose": computer_score += 1
        print(f"Score: you {user_score}, computer {computer_score}")
        if input("Play again? (y/n): ").strip().lower() != "y": break

if __name__ == "__main__": main()
