def PercentProgressBar(value: int, fullBar: int, showPercent: bool = False):
    print("[ ", end="")
    valuePercent = value/fullBar * 100
    for i in range(0, 100):
        if i <= valuePercent:
            print("#", end="")
        else:
            print("-", end="")
    print(" ] ", end="")
    if showPercent:
        print(str(valuePercent) + "%")