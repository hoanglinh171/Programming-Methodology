"""
File: compute_interest.py
-------------------------
The program starts by asking the user for an initial account balance,
which is entered as a float (you can assume a positive real-value is entered).
The program then asks the user for a starting year and month as well as an ending year and month, all entered as integers.
The program then asks the user for a monthly interest rate.
The program should print out the monthly balance in the account from the starting year/month up to
and including the ending year/month with interest accruing monthly.

After printing the monthly balance projection, your program should then repeat the process of asking the user
for a new interest rate and printing the monthly balance in the account using the same starting account balance,
starting year/month, and ending year/month as the user initially entered in the program.
The program should end if the user specifies a monthly interest rate of 0%.
"""


# input start month, year and balance
# input ending month, year
# input interest, calculate the balance in the following months
# end program if interest is 0


def main():
    # take user input for initial balance, starting and ending time
    initial_balance = float(input("Initial balance: "))
    start_month = int(input("Starting month: "))
    start_year = int(input("Starting year: "))
    end_month = int(input("Ending month: "))
    end_year = int(input("Ending year: "))
    # evaluate validity of time
    if (end_year < start_year) or (end_year == start_year and end_month < start_month):
        print("Starting date needs to be before the ending date.")
    else:
        while True:
            interest_rate = float(input("Monthly interest rate (0 to quit): "))
            if interest_rate == 0:
                break
            # calculate and print monthly balance
            else:
                calculate_interest(initial_balance, start_month, start_year, end_month, end_year, interest_rate)


def calculate_interest(ib, sm, sy, em, ey, rate):
    balance = ib
    in_month = sm
    in_year = sy
    total_month = calculate_time(sm, sy, em, ey)  # total numbers of month
    for i in range(total_month):
        balance *= (1 + rate)
        if in_month > 11:  # next of month 12 is month 1 next year
            in_year += 1
            in_month = (in_month + 1) % 12
        else:
            in_month += 1
        print("Year", in_year, "month", in_month, "balance:", balance)


def calculate_time(sm, sy, em, ey):
    if ey > sy:
        total_month = (ey - sy) * 12 + (em - sm)
    return total_month


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
