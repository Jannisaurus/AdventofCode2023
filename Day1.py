import re


filename = "input1.txt"

pattern = r'\b(one|two|three|four|five|six|seven|eight|nine)\b'


# Define a function to get text from file
def get_text_from_file(filename):
    # Define a pattern

    with open(filename) as f:
        lines = f.readlines()

    stringWords = []

    for line in lines:
        # Find the first match in each line
        match = re.search(pattern, line, re.IGNORECASE)
        print(match)

        if match:
            stringWords.append(match.group())

        # Do something if a match is found
        # if match:
        #     print("Match found in line:", line.strip())
        #     # Add your code here to perform the desired action
    
    print(stringWords)

# Call the function to get text from file

def main():
    get_text_from_file(filename)

if __name__ == "__main__": 
    main()




# # Find the first match
# match = re.search(pattern, text)

# # Do something if a match is found
# if match:
#     print("Match found:", match.group())
#     # Add your code here to perform the desired action


def get_text_from_file(filename):
    sum = 0
    numbersArray = []


    with open(filename) as f:
        lines = f.readlines()
#       lines = [line.strip() for line in lines]

    for line in lines:
        number = []

        for char in line:
            if char.isdigit():
                number.append(char)
        
        numbersArray.append(number[0] + number[-1])

    for num in numbersArray:
        sum += int(num)
    
    print(sum)

    # for line in lines:
    #         # Process each line here
    #     for char in line:
    #         if char.isdigit():
    #             if len(number) <= 1:
    #                 number.append(char)
    #                 print(number)
    #             elif number == 2:
    #                 number = int(number[0] + number[1])
    #                 sum += number
    #                 number = []
    #                 print(sum)
    #         else:
    #             pass
            
# def main():
#     # get_text_from_file(filename)

# if __name__ == "__main__": 
#     main()