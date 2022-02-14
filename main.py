import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw"
    elif computer_score == 0:
        return 'dealer has blackjack, you lose'
    elif user_score == 0:
        return "Blackjack, You Win"
    elif user_score > 21:
        return 'You lose'
    elif computer_score > 21:
        return 'Computer went over, you win'
    elif user_score > computer_score:
        return 'You Win'
    else:
        return "You lose"


def game():
    print(logo)
    user_cards = []
    computer_cards = []

    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(user_cards)
    print(computer_cards)

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f'  Your cards: {user_cards}, current score: {user_score}')
        print(
            f'  Computer Cards: {computer_cards[0]}, current score: {computer_score}')

        if user_score > 21 or computer_score == 0 or user_score == 0:
            game_over = True
        else:
            user_draw = input(
                'Type "y" to draw another card, type "n" to pass: ').lower()
            if user_draw == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your Hand: {user_cards}, Your Score: {user_score}")
    print(
        f"  Computer Hand: {computer_cards}, Computer Score: {computer_score}")

    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type 'Y' or 'N': ").lower() == "y":
    game()
