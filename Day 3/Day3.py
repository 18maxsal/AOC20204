
def mul(num1, num2):
    return num1 * num2

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
            # if to_mul[-1] == ")" and to_mul[0:4] == "mul(":
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

print("Total is: ", total)


