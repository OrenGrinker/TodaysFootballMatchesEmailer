# Today's Football Matches Emailer

This project fetches today's football matches from the Live Score API and sends the details via email using SendGrid.

## Features

- Fetch today's football matches based on competition.
- Send an email with the matches using SendGrid.

## Getting Started

### Prerequisites

- Python 3.6+
- SendGrid account
- Live Score API account

### Installation

1. Clone the repository:
git clone https://github.com/OrenGrinker/todays-football-matches-emailer.git

2. Install required packages:
pip install requests sendgrid

### Configuration

- Create API keys at [SendGrid](https://sendgrid.com/) and [Live Score API](https://live-score-api.com/).
- Navigate to [Live Score API Competitions](https://live-score-api.com/competitions) to find `COMPETITION_ID` for your league.
- Update `config.py` with your API keys, email addresses, and `COMPETITION_ID`.

### Usage

Run the script:
python main.py


## License

This project is open source and available under the MIT License.
