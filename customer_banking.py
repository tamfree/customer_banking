# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import savings_account as sa

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("+"* 56)
    print("\nPlease enter the following *Savings* account information: ")
    savings_balance = float(input("What is your account balance? "))
    savings_interest = float(input("What is the annual interest rate (as a percent)? "))
    savings_maturity = int(input("What is the duration of time in months that this balance has or will accure interest? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = sa.create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"""\nYour savings account gains are as follows: 
          Interest earned: ${interest_earned:,.2f}
          Updated balance: ${updated_savings_balance:,.2f}
          """)

"""
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("+"* 51)
    print("\nPlease enter the following *CD* account information: ")
    savings_balance = float(input("What is your account balance? "))
    savings_interest = float(input("What is the annual interest rate (as a percent)? "))
    savings_maturity = int(input("What is the duration of time in months that this balance has or will accure interest? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
"""

if __name__ == "__main__":
    # Call the main function.
    main()