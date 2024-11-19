import requests
from datetime import datetime, timedelta
import json

input_file = "user_input.txt"
output_file = "output.txt"


def increment_day(string_date):
    """Takes a string date in YYYY/MM/DD format and returns the date with one day added to it."""
    string_date = datetime.strptime(string_date, "%Y-%m-%d")
    string_date += timedelta(days=1)
    return string_date.strftime("%Y-%m-%d")


def date_formatter(date):
    """Takes MM/DD/YYYY string date and returns it in YYYY/MM/DD format"""
    # Parse the date string into a datetime object
    date_object = datetime.strptime(date, "%m/%d/%Y")

    # Format the datetime object into YYYY-MM-DD format
    return date_object.strftime("%Y-%m-%d")


while True:
    filtered_games = []

    # Assuming the user input is in the format "MM/DD/YYYY MM/DD/YYYY TEAM_CODE" or "MM/DD/YYYY TEAM_CODE"
    with open(input_file, "r") as f:
        user_input = f.read()

    if user_input != "":
        # Separate date(s) and team code
        split_user_input = user_input.split(" ")

        # If split_user_input has 2 elements, the user inputted one dates, meaning we only get games on one day
        if len(split_user_input) == 2:
            date_str = split_user_input[0]
            team_code = split_user_input[1]

            formatted_start_date = date_formatter(date_str)

        # If split_user_input has 3 elements, the user inputted two dates, meaning we have a date range
        elif len(split_user_input) == 3:
            start_date_str = split_user_input[0]
            end_date_str = split_user_input[1]
            team_code = split_user_input[2]

            formatted_start_date = date_formatter(start_date_str)
            formatted_end_date = date_formatter(end_date_str)

        # NHL API URL for getting schedules using dates
        base_url = "https://api-web.nhle.com/v1/schedule/{}"

        # Start and end date are equal if only one date was provided by the user
        if len(split_user_input) == 2:
            formatted_end_date = formatted_start_date

        # We get the games on each day, whilst incrementing the start date until it reaches the end date
        while formatted_start_date <= formatted_end_date:
            # Format the date into the URL
            url = base_url.format(*formatted_start_date.split('/'))

            try:
                response = requests.get(url)
                if response.status_code != 200:
                    print(f"Failed to fetch schedule for {formatted_start_date} (HTTP {response.status_code})")
                    increment_day(formatted_start_date)

                # Load the JSON data
                data = json.loads(response.text)

                games = data["gameWeek"][0]["games"]

                for game in games:
                    # Get start date and time
                    start_date_and_time = game['startTimeUTC']

                    # Separate the time from the date using the .split() method
                    start_time = start_date_and_time.split("T")[1]

                    # Parse the time string into a datetime object
                    time_obj = datetime.strptime(start_time, "%H:%M:%SZ")
                    # Format the datetime object as 'HH:MM'
                    formatted_time = time_obj.strftime("%H:%M")

                    # If our team is included in the match, append the details to the output text file
                    if game["awayTeam"]["abbrev"] == team_code or game["homeTeam"]["abbrev"] == team_code:
                        # Gather opposing teams
                        teams = [game["awayTeam"]["commonName"]["default"],
                                 game["homeTeam"]["commonName"]["default"]]
                        venue = game['venue']['default']

                        # Write match details to output file
                        with open(output_file, "a") as f:
                            f.write(f"Games on {formatted_start_date}: ({teams[0]} vs {teams[1]}) at {formatted_time} "
                                    f"UTC time at {venue}\n")
            except Exception as e:
                print(f"Error fetching data for {formatted_start_date}: {e}")

            # Move to the next date
            formatted_start_date = increment_day(formatted_start_date)
    with open("user_input.txt", "w") as f:
        pass
