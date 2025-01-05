def ProgressBar(value, fullBar):
    print("[ ", end="")
    for i in range(0, fullBar+1):
        if i <= value:
            print("#", end="")
        else:
            print("-", end="")
    print(" ]", end="")