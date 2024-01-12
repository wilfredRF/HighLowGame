#Wilfred Robert-Fajimi
#CSCI 180 Program 1 Assignment
#HighLow Dice game 
#October 14, 2023

#Introduce user to game program
print("Hello user, this is a game that tests your guessing abilities!\n")
print("You will be prompted to enter five values of your imaginary die that you will roll 5 times. \n")
print("The computer will then roll its own die 5 times and you will guess if the sum of your roll values is higher or lower than the computer's. \n")

#Assign 'choice' variable
choice = "y"

#Confirm if user wants to continue to the game or not
choice = input("Ready to put your intuition to test? Enter 'y' for yes and 'n' for no:  ")

#Proceed to game if user wishes to continue
while choice.lower() == "y":
    print("\nOkay, let's go!")
    print("Make sure all your roll values are in the range of 1 to 6!")
    
    #Assign variables for user inputs for rolls of the die
    die_1 = int(input("\nEnter 1st roll value: "))
    die_2 = int(input("Enter 2nd roll value: "))
    die_3 = int(input("Enter 3rd roll value: "))
    die_4 = int(input("Enter 4th roll value: "))
    die_5 = int(input("Enter 5th roll value: "))
    print("\nWell done!")
    
    sum1_of_rolls = die_1 + die_2 + die_3 + die_4 + die_5
    
    #Introduce random module to program
    import random
    
    #Assign variables for the random die roll values from the computer
    die_01 = random.randint(1,6)
    die_02 = random.randint(1,6)
    die_03 = random.randint(1,6)
    die_04 = random.randint(1,6)
    die_05 = random.randint(1,6)
    
    sum01_of_rolls = die_01 + die_02 + die_03 + die_04 + die_05
    print("\nThe computer has also rolled 5 times. Time for you to guess!")
    print("Do you think the sum of your five rolls is greater than or lower than the computer's? ")
    die_choice = input("Enter 'H' for higher and 'L' for lower:  ")
        
        
    #Program game conditions
    if die_choice.upper() == "H":
        if sum01_of_rolls > sum1_of_rolls:
            print("\nYou were almost there!\nThe computer rolled the folowing:")
            print("First roll: ", die_01)
            print("Second roll: ", die_02)
            print("Third roll: ", die_03)
            print("Fourth roll: ", die_04)
            print("Fifth roll: ", die_05)        
            print("Your total was ", sum1_of_rolls , " which was actually LOWER than the computer's total of ", sum01_of_rolls)
        
        elif sum01_of_rolls < sum1_of_rolls:
            print("\nBravo! You're correct!\nThe computer rolled the following:")
            print("First roll: ", die_01)
            print("Second roll: ", die_02)
            print("Third roll: ", die_03)
            print("Fourth roll: ", die_04)
            print("Fifth roll: ", die_05)        
            print("Your total was ", sum1_of_rolls , " which was, in fact, HIGHER than the computer's total of ", sum01_of_rolls)
        else:
            print("\nHmm...Seems like your total was the same with the computer's!\nThe computer rolled the following:")
            print("First roll: ", die_01)
            print("Second roll: ", die_02)
            print("Third roll: ", die_03)
            print("Fourth roll: ", die_04)
            print("Fifth roll: ", die_05)        
            print("Your total was ", sum1_of_rolls , " which was exactly the same as the computer's total of also ", sum01_of_rolls)
    
    elif die_choice.upper() == "L":
        if sum01_of_rolls > sum1_of_rolls:
            print("\nBravo! You're correct!\nThe computer rolled the following:")
            print("First roll: ", die_01)
            print("Second roll: ", die_02)
            print("Third roll: ", die_03)
            print("Fourth roll: ", die_04)
            print("Fifth roll: ", die_05)        
            print("Your total was ", sum1_of_rolls , " which was, in fact, LOWER than the computer's total of ", sum01_of_rolls)
        elif sum01_of_rolls < sum1_of_rolls:
            print("\nYou were almost there!\nThe computer rolled the folowing:")
            print("First roll: ", die_01)
            print("Second roll: ", die_02)
            print("Third roll: ", die_03)
            print("Fourth roll: ", die_04)
            print("Fifth roll: ", die_05)        
            print("Your total was ", sum1_of_rolls , " which was actually HIGHER than the computer's total of ", sum01_of_rolls)
        else:
            print("\nHmm...Seems like your total was the same with the computer's!\nThe computer rolled the following:")
            print("First roll: ", die_01)
            print("Second roll: ", die_02)
            print("Third roll: ", die_03)
            print("Fourth roll: ", die_04)
            print("Fifth roll: ", die_05)        
        
            print("Your total was ", sum1_of_rolls , " which was exactly the same as the computer's total of also ", sum01_of_rolls)
    else:
        print("\nInvalid response :(")
        
            
            
    #Ask if user wants to play again        
    choice = input("\nReady to put your intuition to test again? Enter 'y' for yes and 'n' for no:  ")
    
    
    
  
#End program    
print("\nOkay, till next time!")
print("Program ending...")
