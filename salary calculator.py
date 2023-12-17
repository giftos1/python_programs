def main():
    total_salary = 0
    print("Welcome to the Salary Calculator")
    get_name = input("Please enter your name:")
    while not get_name:
        print("error in getting name")
        get_name = input("Please enter your name")
    print(get_name)
    get_beg_salary = int(input("Please enter your beginning salary:"))
    while get_beg_salary < 10000:
        print("Sorry, your beginning salary must be at least 10000")
        get_beg_salary = int(input("Please enter your beginning salary:"))
    print(get_beg_salary)
    years_worked = int(input("Please enter the years worked:"))
    while years_worked < 1 or years_worked > 10:
        print("Incorrect years")
        years_worked = int(input("Please enter the years worked:"))
    print(years_worked)
    print("Thank you.")
    print("Your salary will be")
    for years in range(1, years_worked + 1):
        if years == 1:
            print("Year " + str(years) + ": " + "{:.2f}".format(get_beg_salary))
        else:
            get_beg_salary = get_beg_salary * 1.02
            print("Year " + str(years) + ": " + "{:.2f}".format(get_beg_salary))
        total_salary = total_salary + get_beg_salary
    print("Your total lifetime salary is " + "{:.2f}".format(total_salary))


main()
