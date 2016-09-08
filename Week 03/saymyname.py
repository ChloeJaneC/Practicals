write_file = open('name.txt', mode='w')
name = str(input("Please enter your name: "))
write_file.write(name)
write_file.close()