

def average(week):
    average = 0
    total = len(week)
    print(total)

    for day in week:
        num = total / len(day)
        average += num
    return average
week=["monday","tuesday","wednesday","thurday","friday","saturday","sunday"]
print(average(week))

    



