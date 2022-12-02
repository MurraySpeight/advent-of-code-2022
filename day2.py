R_ID = ("A", "X")
P_ID = ("B", "Y")
S_ID = ("C", "Z")
R = {"id": R_ID, "score": 1, "lose": P_ID}
P = {"id": P_ID, "score": 2, "lose": S_ID}
S = {"id": S_ID, "score": 3, "lose": R_ID}


def main():
    with open('day2.txt', 'r') as f:
        score = 0
        for line in f:
            score += game(line[0], line[2])
        print(f"Final score {score}")
        return score


def game(left, right):
    if right in R["id"]:
        return game_score(left, R)
    elif right in P["id"]:
        return game_score(left, P)
    else:  # left in S["id"]:
        return game_score(left, S)


def game_score(left, d):
    draw = 3
    win = 6
    if left in d["lose"]:
        return d["score"]
    elif left in d["id"]:
        return d["score"] + draw
    else:
        return d["score"] + win


if __name__ == '__main__':
    main()
