# \n
x = input("Enter text to write to the file: ")
file1 = open("output.txt", "w")
writing = file1.write(x)
file1.close()
print("Data Successfully written to output.txt")


y = input("Enter additional text to append: ")
file1 = open("output.txt", "a")
append = file1.write(y)
file1.close()
print("Data successfully appended")


file1 = open("output.txt", "r")
read = file1.read()
file1.close()

print("Final content of output.txt: " + str(read))
