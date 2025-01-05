def ProgressBar(value: int, fullBar: int, showPercent: bool = False):
    print("[ ", end="")
    for i in range(0, fullBar+1):
        if i <= value:
            print("#", end="")
        else:
            print("-", end="")
    print(" ] ", end="")
    if showPercent:
        valuePercent = value/fullBar * 100
        print(str(valuePercent) + "%")