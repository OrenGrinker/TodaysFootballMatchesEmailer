import requests
from datetime import datetime
from config import LIVESCORE_API_KEY, LIVESCORE_API_SECRET, COMPETITION_ID

def fetch_todays_games():
    DATE = datetime.now().strftime('%Y-%m-%d')
    url = f'https://livescore-api.com/api-client/fixtures/matches.json?key={LIVESCORE_API_KEY}&secret={LIVESCORE_API_SECRET}&date={DATE}&competition_id={COMPETITION_ID}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
