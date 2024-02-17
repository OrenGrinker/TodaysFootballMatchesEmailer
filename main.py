from fetch_matches import fetch_todays_games
from emailer import send_email

def format_email_content(data):
    if not data or not data['data']['fixtures']:
        return "No games found for today."
    fixtures = data['data']['fixtures']
    email_content = "Today's Games:\n\n"
    for fixture in fixtures:
        email_content += f"{fixture['home_name']} vs {fixture['away_name']} at {fixture['time']} - {fixture['competition']['name']}\n"
    return email_content

def main():
    data = fetch_todays_games()
    email_body = format_email_content(data)
    send_email("Today's Football Matches", email_body)

if __name__ == "__main__":
    main()
