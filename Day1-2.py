import re

filename = "input1.txt"

def findNumbers():
    tuplesList = []
    sum = 0
    numbersArray = []

    with open(filename) as f:
        lines = f.readlines()


    word_pattern = r'(one|two|three|four|five|six|seven|eight|nine)'
    digit_pattern = r'\d'

    for line in lines:
            # Find words and digits
        matches = re.finditer(word_pattern + '|' + digit_pattern, line, re.IGNORECASE)

        for match in matches:
            word_or_digit = match.group()
            start_index = match.start()

            # Adjust start index

            if word_or_digit.isdigit():
                tuplesList.append((word_or_digit, start_index))
            else:
                word = word_or_digit

                if word == "one":
                    word = "1"
                    if "eight" in line[start_index + 2:]:
                        tuplesList.append(("8", start_index + 2))
                elif word == "two":
                    word = "2"
                    if "one" in line[start_index + 2:]:
                        tuplesList.append(("1", start_index + 2))
                elif word == "three":
                    word = "3"
                    if "eight" in line[start_index + 4:]:
                        tuplesList.append(("8", start_index + 4))
                elif word == "four":
                    word = "4"
                elif word == "five":
                    word = "5"
                    if "eight" in line[start_index + 3:]:
                        tuplesList.append(("8", start_index + 3))
                elif word == "six":
                    word = "6"
                elif word == "seven":
                    word = "7"
                    if "nine" in line[start_index + 4:]:
                        tuplesList.append(("9", start_index + 4))
                elif word == "eight":
                    word = "8"
                    if "two" in line[start_index + 4:]:
                        tuplesList.append(("2", start_index + 4))
                    elif "three" in line[start_index + 4:]:
                        tuplesList.append(("3", start_index + 4))
                elif word == "nine":
                    word = "9"
                    if "eight" in line[start_index + 3:]:
                        tuplesList.append(("8", start_index + 3))

                tuplesList.append((word, start_index))

                # if word == "1":
                #     start_index = start_index + 2
                #     for char in line[start_index:]:
                #         if char[line.index(start_index) + 1] == "i" and line.index(start_index) + 2 == "g" and line.index(start_index) + 3 == "h" and line.index(start_index) + 4 == "t":
                #             tuplesList.append(("8", line.index(char)))
                # elif word == "2":
                #     start_index = start_index + 2
                #     for char in line[start_index:]:
                #         if char[line.index(start_index) + 1] == "n" and line.index(start_index) + 2 == "e":
                #             tuplesList.append(("1", line.index(char)))
                # elif word == "3":
                #     start_index = start_index + 4
                #     for char in line[start_index:]:
                #         if char[line.index(start_index) + 1] == "i" and line.index(start_index) + 2 == "g" and line.index(start_index) + 3 == "h" and line.index(start_index) + 4 == "t":
                #             tuplesList.append(("8", line.index(char)))
                # elif word == "5":
                #     start_index = start_index + 3
                #     for char in line[start_index:]:
                #         if char[line.index(start_index) + 1] == "i" and line.index(start_index) + 2 == "g" and line.index(start_index) + 3 == "h" and line.index(start_index) + 4 == "t":
                #             tuplesList.append(("8", line.index(char)))

                
        # Sort tuplesList by index
        tuplesList = sorted(tuplesList, key=lambda x: x[1])

        print(tuplesList)

        firstNumber = tuplesList[0][0]
        secondNumber = tuplesList[-1][0]

        numbersArray.append(firstNumber + secondNumber)   

        tuplesList.clear()

    for num in numbersArray:
        sum += int(num)

    print(sum)

def main():
    findNumbers()

if __name__ == "__main__": 
    main()
