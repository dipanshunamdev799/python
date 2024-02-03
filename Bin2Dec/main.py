binary_number = input("Type a 8 bit binary number: ")
try:
    output = open("output.txt",mode="w")
    result = int(binary_number,2)
    print("Decimal Output: %d"%result)
    output.write(str(result))
    print("The result is also stored in an output file in the current directory😃.")
except Exception as e:
    logs = open("log.txt",mode="w")
    print("Some error occured! \nCheck the log file for more info")
    logs.write(str(e))