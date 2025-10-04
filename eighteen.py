#inputs : correct answers, wrong answers,unattempted. marking scheme: +4 for correct,-1 for wrong, 0 for 
#unattempted score>=180 -"excellent" 120-179-"good" 60-119-"average" below 60-"fail" also if wrong answers>correct answers ,
#show: "improve accuracy!
def evaluate_performance(correct, wrong, unattempted):
    score = (correct * 4) - wrong
    if score >= 180:
        result = "Excellent"
    elif score >= 120:
        result = "Good"
    elif score >= 60:
        result = "Average"
    else:
        result = "Fail"
    
    if wrong > correct:
        result += " | Improve accuracy!"
    
    return f"Score: {score} | Performance: {result}"
