out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()

name_textfile = open("name.txt", "r")
print(f"Your name is {name_textfile.read()}")
name_textfile.close()

out_file = open("numbers.txt", "w")
print("17\n42\n400", file=out_file)
out_file.close()

numbers_textfile = open("numbers.txt", "r")
numbers = numbers_textfile.readlines()
print(int(numbers[0]) + int(numbers[1]))

result = 0
for i in range(0, len(numbers)):
    result += int(numbers[i])
print(result)
