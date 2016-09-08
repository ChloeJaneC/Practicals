def main():
    score = float(input("Enter score: "))
    result = score_check(score)
    print(result)


def score_check(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
