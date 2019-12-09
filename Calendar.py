import datetime

displayBuffer = [["MON", 30, 31], ["TUE"], ["WEN"], ["THU"], ["FRI"], ["SAT"], ["SUN"]]
dictOfMon = {1: "Januar", 2: "Februar", 3: "März", 4: "April", 5: "Mai", 6: "Juni",
             7: "Juli", 8: "August", 9: "September", 10: "Oktober", 11: "November", 12: "Dezember"}
longMonths = [1, 3, 5, 7, 8, 10, 12, 14]


def prettiefybuffer(buffer):
    lines = [[], [], [], [], [], []]
    hasbeenone = False

    for weekdayCollumn in buffer:
        lines[0].append(weekdayCollumn[0])
        lines[2].append(weekdayCollumn[2])
        lines[3].append(weekdayCollumn[3])
        lines[4].append(weekdayCollumn[4])
        try:
            if int(weekdayCollumn[1]) > 1 and not hasbeenone:
                lines[1].append("")
            else:
                hasbeenone = True
            if hasbeenone: lines[1].append(weekdayCollumn[1])
            lines[5].append(weekdayCollumn[5])
        except IndexError as e:
            pass
    return lines


def printbuffer(buffer):
    for CurrentLine in buffer:
        for CurrenSym in CurrentLine:
            print(CurrenSym, end="\t")
        print("")
    print("\n")


for month in dictOfMon:
    mlen = 29 if dictOfMon[month] == "Februar" else 31 if month in longMonths else 30
    for day in range(mlen):
        day += 1
        displayBuffer[datetime.datetime(2020, month, day).isocalendar()[-1] - 1].append(str(day))

    print(dictOfMon[month] + ":")
    printbuffer(prettiefybuffer(displayBuffer))
    displayBuffer = [["MON"], ["TUE"], ["WEN"], ["THU"], ["FRI"], ["SAT"], ["SUN"]]
