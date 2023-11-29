def choice(round_score, my_score, opponent_score):
    if round_score > 19 +11000*opponent_score/100000 or my_score + round_score >= 100:
        return False
    else:
        return True
#yes, i just took russell's code and tweaked the numbers. no, i am not ashamed.
