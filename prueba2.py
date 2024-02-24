def get_birthdate():
    """
    Asks the user for their birthdate and returns it.
    """
    year = int(input("Enter your birth year (e.g., 1990): "))
    month = int(input("Enter your birth month (1-12): "))
    day = int(input("Enter your birth day (1-31): "))
    return year, month, day

def calculate_days_alive(birthdate):
    """
    Calculates the number of days the user has been alive.
    """
    from datetime import datetime

    today = datetime.today()
    birthdate_dt = datetime(*birthdate)
    days_alive = (today - birthdate_dt).days
    return days_alive

def main():
    print("Welcome! Let's calculate the number of days you've been alive.")
    birthdate = get_birthdate()
    days_alive = calculate_days_alive(birthdate)
    print(f"You've been alive for approximately {days_alive} days.")

if __name__ == "__main__":
    main()
