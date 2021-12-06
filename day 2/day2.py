import sys

'''Part 1
commands = {
    "forward": 0,
    "down": 0,
    "up": 0
}

with open("\\".join(sys.argv[0].split("\\")[:-1]) + "\\day2.txt") as f:
    file = [line.replace("\n", "") for line in f.readlines()]
    for line in file:
        commands[line[:-2]] += int(line[-1:])
    sum_location = {
        "forward": commands["forward"],
        "depth": commands["down"] - commands["up"]
    }
    print(sum_location["forward"] * sum_location["depth"])
Part 1'''

'''Part 2
commands = {
    "forward": 0,
    "depth": 0,
    "aim": 0
}

with open("\\".join(sys.argv[0].split("\\")[:-1]) + "\\day2.txt") as f:
    file = [line.replace("\n", "") for line in f.readlines()]
    for line in file:
        if line[:-2] == "down":
            commands["aim"] += int(line[-1])
        if line[:-2] == "up":
            commands["aim"] -= int(line[-1])
        if line[:-2] == "forward":
            commands["forward"] += int(line[-1])
            commands["depth"] += commands["aim"] * int(line[-1])
    print(commands["forward"] * commands["depth"])
Part 2'''