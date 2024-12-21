
def mul(num1, num2):
    return num1 * num2


def part_one():
    f = open("Day3Input.txt", "r")
    data = f.readlines()
    valid_input = "mul(), 1234567890"
    total = 0
    for i in data:
        index = 0
        to_mul = ""
        while index < len(i):
            if i[index] in valid_input:
                to_mul += i[index]
                if to_mul[-1] == ")" and "mul(" in to_mul:
                    start_index = to_mul.index("m")
                    num1 = ""
                    num2 = ""
                    is_diff = ","
                    print(to_mul)
                    for j in range(start_index + 4, len(to_mul)):
                        if to_mul[j].isdigit() and is_diff == ",":
                            num1 += to_mul[j]
                        elif to_mul[j].isdigit() and is_diff == "x":
                            num2 += to_mul[j]
                        elif to_mul[j] == ",":
                            is_diff = "x"
                    print(f"num1: {num1}, num2: {num2}")
                    total += mul(int(num1), int(num2))
                    to_mul = ""
                elif to_mul[-1] == ")" and to_mul[0:4] != "mul(":
                    to_mul = ""
            else:
                to_mul = ""
            index += 1
    f.close()
    print("Total is: ", total)


def  part_two():
    # f = open("Day3InputPart2.txt", "r")
    f = open("Day3Input.txt", "r")
    data = f.readlines()
    valid_input = "mul(), 1234567890do()don't()"
    total = 0
    for i in data:
        index = 0
        command = ""
        is_do = True
        while index < len(i):
            if i[index] in valid_input:
                command += i[index]
                if command[-1] == ")" and "mul(" in command and is_do:
                    start_index = command.index("m")
                    num1 = ""
                    num2 = ""
                    is_diff = ","
                    print(command)
                    for j in range(start_index + 4, len(command)):
                        if command[j].isdigit() and is_diff == ",":
                            num1 += command[j]
                        elif command[j].isdigit() and is_diff == "x":
                            num2 += command[j]
                        elif command[j] == ",":
                            is_diff = "x"
                    # print(f"num1: {num1}, num2: {num2}")
                    total += mul(int(num1), int(num2))
                    command = ""
                elif command[-1] == ")" and command[0:4] != "mul(":
                    if "do()" in command:
                        is_do = True
                    elif "don't()" in command:
                        is_do = False
                    command = ""
            else:
                command = ""
            index += 1
    f.close()
    print("Total is: ", total)
            




def main():
    # part_one()
    part_two()

if __name__ == "__main__":
    main()
