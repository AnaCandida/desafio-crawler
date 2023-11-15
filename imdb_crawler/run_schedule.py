import sys
import time

import schedule
from loguru import logger
from run_spider import execute_spider
from schedule_utils import (
    display_days_of_week,
    get_user_day_choice,
    get_user_hour_input,
    validate_hour_format,
)


def schedule_task(selected_day, hour):
    schedule_expression = f"schedule.every().{selected_day.lower()}.at('{hour}').do(execute_spider).tag('user_scheduled')"
    exec(schedule_expression)
    logger.info(f"Spider scheduled for {selected_day} at {hour} successfully.")
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "run_once":
        logger.info("Running spider once")
        execute_spider()
    else:
        logger.info("Starting the scheduling for the IMDB spider")
        days_of_week = display_days_of_week()

        selected_day = get_user_day_choice(
            prompt="Choose the number corresponding to the desired day: ", options=days_of_week
        )
        hour = get_user_hour_input(
            prompt="Enter the scheduled time (in 24-hour format, for example, '14:50'): ",
            validation_function=validate_hour_format,
        )

        schedule_task(selected_day, hour)


if __name__ == "__main__":
    main()
