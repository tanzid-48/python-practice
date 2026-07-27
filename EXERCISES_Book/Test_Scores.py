highest = eval(input("Enter score 1: "))
lowest = highest
total = highest

for i in range(9):
    score = eval(input("Enter score " + str(i + 2) + ": "))
    total = total + score
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

average = total / 10
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)
