n = 52
deck = []

def not_high(list):
    for item in list:
        if item in ["king", "queen", "jack", "ace"]:
            return False
    return True

for i in range(n):
    deck.append(input())

score_a = 0
score_b = 0
player = "A"

for i in range(n):
    card = deck[i]
    points = 0
    remaining = n - i - 1
    if card == "ace" and remaining >= 4 and not_high(deck[i+1:i+5]):
        points = 4
    elif card == "king" and remaining >= 3 and not_high(deck[i+1:i+4]):
        points = 3
    elif card == "queen" and remaining >= 2 and not_high(deck[i+1:i+3]):
        points = 2
    elif card == "jack" and remaining >= 1 and not_high(deck[i+1:i+2]):
        points = 1  

    if points > 0:
        print(f"Player {player} scores {points} point(s).")
    if player == "A":
        score_a = score_a + points
        player = "B"
    else:
        score_b = score_b + points
        player = "A"

print(f"Player A: {score_a} point(s).")
print(f"Player B: {score_b} point(s).")


                                                     
                                                     

