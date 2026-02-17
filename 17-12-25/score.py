# score

def score_cal(marks, total):  #userdefined function
    if total == 0:
        return "Error: Total zero!"
    perc = (marks / total) * 100
    
    if perc >= 90: return f"{perc:.1f}% - A+"
    if perc >= 80: return f"{perc:.1f}% - A"
    if perc >= 70: return f"{perc:.1f}% - B"
    if perc >= 60: return f"{perc:.1f}% - C"
    if perc >= 50: return f"{perc:.1f}% - D"
    return f"{perc:.1f}% - F"

def main():
    print("Score Calculator")
    marks = float(input("Marks: "))
    total = float(input("Total: "))
    print(score_cal(marks, total))

main()
