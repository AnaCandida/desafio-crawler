import calendar
import re
from loguru import logger

def display_days_of_week():
    """
    Display a list of days of the week and return the list.
    """
    days_of_week = list(calendar.day_name)
    for i, day in enumerate(days_of_week, start=1):
        print(f"{i}. {day}")
    return days_of_week

def get_user_day_choice(prompt, options):
    """
    Get user choice from the provided day options.

    Parameters:
    - prompt (str): Prompt message for user input.
    - options (list): List of day options for the user to choose from.

    Returns:
    - User's choice from the options.
    """
    while True:
        choice = input(prompt)
        try:
            index = int(choice) - 1
            return options[index]
        except (ValueError, IndexError):
            logger.error("Invalid choice. Make sure to choose a valid number.")

def get_user_hour_input(prompt, validation_function):
    """
    Get user hour input with validation.

    Parameters:
    - prompt (str): Prompt message for user input.
    - validation_function (function): Function to validate the hour user input.

    Returns:
    - Validated user input.
    """
    while True:
        user_input = input(prompt)
        if validation_function(user_input):
            return user_input
        else:
            logger.error("Invalid input. Make sure to enter the correct format.")

def validate_hour_format(hour):
    """
    Validate the format of the input hour.

    Parameters:
    - hour (str): Input hour string.

    Returns:
    - True if the hour format is valid, False otherwise.
    """
    if not hour:
        return False
    hour_format_regex = re.compile(r"^([01]\d|2[0-3]):([0-5]\d)$")
    return bool(hour_format_regex.match(hour))
