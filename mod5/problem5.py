#5. Write a program that continuously asks the user to input a number. 
#If the user enters 0, immediately stop asking for more numbers.
#Otherwise, print the number they entered. Sample interaction:

#Enter a number (0 to stop): 4
#You entered 4
#Enter a number (0 to stop): 7
#You entered 7
#Enter a number (0 to stop): 0
#Exiting...



while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:  # This must be inside the loop
        print("Exiting...")
        break  # Correct placement inside the loop
    
    print(f"You entered {num}")  # Correct indentation
