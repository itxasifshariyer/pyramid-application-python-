def check_numbers_and_years():
    print("=== Even/Odd & Leap Year Checker ===")
    
    # ---------------------------------------------------------
    # PART 1: Even or Odd Checker
    # ---------------------------------------------------------
    try:
        num = int(input("Enter an integer to check if it's Even or Odd: "))
        
        # The % (modulo) operator returns the remainder of a division.
        # If a number divided by 2 has a remainder of 0, it's even.
        if num % 2 == 0:
            print(f"-> {num} is an EVEN number.")
        else:
            print(f"-> {num} is an ODD number.")
            
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    print("\n---------------------------------------------------------")

    # ---------------------------------------------------------
    # PART 2: Leap Year Checker
    # ---------------------------------------------------------
    try:
        year = int(input("Enter a year to check if it's a Leap Year: "))
        
        # Leap Year Logic:
        # 1. A year is a leap year if it is divisible by 4...
        # 2. EXCEPT if it is divisible by 100, then it is NOT a leap year...
        # 3. UNLESS it is also divisible by 400, then it IS a leap year!
        
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f"-> {year} is a Leap Year! (Divisible by 4, 100, and 400)")
                else:
                    print(f"-> {year} is NOT a Leap Year. (Centurial year not divisible by 400)")
            else:
                print(f"-> {year} is a Leap Year! (Divisible by 4 but not 100)")
        else:
            print(f"-> {year} is NOT a Leap Year. (Not divisible by 4)")
            
    except ValueError:
        print("Error: Please enter a valid year.")

# Run the program
check_numbers_and_years()