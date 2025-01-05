import ProgressBar

full = input("Enter the amount of data to download: ")
value = input("Enter the downloaded data: ")
full = int(full)
value = int(value)

ProgressBar.PercentProgressBar(value, full, True)