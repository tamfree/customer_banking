# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
import savings_account as sa
import cd_account as cd

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("+"* 56)
    print("\nPlease enter the following *Savings* account information: ")
    savings_balance = float(input("What is your account balance? "))
    savings_interest = float(input("What is the annual interest rate (as a percent)? "))
    savings_maturity = int(input("What is the savings length of time in months? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = sa.create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"""\nYour savings account gains are as follows: 
          Interest earned: ${interest_earned:,.2f}
          Interest earned (in thousandths): ${interest_earned:,.3f}
          Updated balance: ${updated_savings_balance:,.2f}
          Updated balance: (in thousandths) ${updated_savings_balance:,.3f}
          """)


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print("+"* 51)
    print("\nPlease enter the following *CD* account information: ")
    cd_balance = float(input("What is your account balance? "))
    cd_interest = float(input("What is the annual interest rate (as a percent)? "))
    cd_maturity = int(input("What is the maturation time in months? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = cd.create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"""\nYour CD account gains are as follows: 
        Interest earned: ${cd_interest_earned:,.2f}
        Interest earned (in thousandths): ${cd_interest_earned:,.3f}
        Updated balance: ${updated_cd_balance:,.2f}
        Updated balance: (in thousandths) ${updated_cd_balance:,.3f}
        """)

if __name__ == "__main__":
    # Call the main function.
    main()