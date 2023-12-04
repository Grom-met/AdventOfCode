numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
result = 0
numberWordLength = range(3,6)

### Open today's file ###
input = open("../input/Day1", "r")

### Read the input and split lines into list elements ###
data = input.read().split("\n")
input.close()

for line in data:
    lineLen = len(line)
    i = 0
    j = lineLen - 1
    fwdIt, bwdIt = True

    while fwdIt:
        if line[i].isnumeric():
            result += int(line[i]) * 10
            fwdIt = False
        else:
            for wordLen in numberWordLength:
                checkRange = i + wordLen
                if checkRange <= lineLen:
                    try:
                        result += numbers.index(line[i:checkRange]) * 10
                        fwdIt = False
                    except ValueError:  # Have _index_ do the heavy lifting >:)
                        pass  # Bad to the bone
                else:
                    break
        i += 1
    while bwdIt:
        if line[j].isnumeric():
            result += int(line[j])
            bwdIt = False
        else:
            for wordLen in numberWordLength:
                checkRange = j + wordLen
                if checkRange <= lineLen:
                    try:
                        result += numbers.index(line[j:checkRange])
                        bwdIt = False
                    except ValueError:
                        pass  # B-b-b-b-b-b-baaaad
                else:
                    break
        j -= 1

print("The result for today's advent is: " + str(result))
