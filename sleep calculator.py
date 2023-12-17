def main():
    total_hours = 0
    print("This program will calculate your sleep-debt over 5 days.")

    for sleep_hours in range(1, 6):
        sleep_hours = int(input("Please enter Day " + str(sleep_hours) + " sleep:"))
        while sleep_hours > 8 or sleep_hours < 0:
            print("Invalid number")
            sleep_hours = int(input("Please enter Day " + str(sleep_hours) + " sleep:"))
        else:
            print(sleep_hours)
        total_hours = total_hours + sleep_hours
        
    print("Your total hours of sleep were:")
    print(total_hours)
    sleep_debt = 40 - total_hours

    if sleep_debt > 0:
        print("Your sleep debt over this time is:")
        print(str(sleep_debt) + " hours")
        print("You need more sleep!")
    else:
        print("Your sleep debt over this time is:")
        print(str(sleep_debt) + " hours")
        print("You are lucky you slept enough.")


main()
