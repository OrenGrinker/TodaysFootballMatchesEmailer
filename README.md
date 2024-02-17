# Today's Football Matches Emailer

This project fetches today's football matches from the Live Score API and sends the details via email using SendGrid. It is designed to run as an AWS Lambda function, enabling serverless execution and scheduling.

## Features

- Fetch today's football matches based on competition.
- Send an email with the matches using SendGrid.
- Serverless execution with AWS Lambda.
- Scheduled fetching and emailing with Amazon CloudWatch Events.

## Getting Started

### Prerequisites

- Python 3.6+
- SendGrid account
- Live Score API account
- AWS account with access to AWS Lambda, Amazon CloudWatch, and optionally AWS Secrets Manager

### Installation

1. **Clone the repository:**
git clone https://github.com/OrenGrinker/todays-football-matches-emailer.git

2. **Install required packages:**
pip install requests sendgrid

Note: When deploying to AWS Lambda, package your application with dependencies unless using AWS Lambda Layers for dependencies.

### Configuration

- Create API keys at [SendGrid](https://sendgrid.com/) and [Live Score API](https://live-score-api.com/).
- Navigate to [Live Score API Competitions](https://live-score-api.com/competitions) to find `COMPETITION_ID` for your league.
- Update `config.py` with your API keys, email addresses, and `COMPETITION_ID`.
- (Optional) For enhanced security, store your API keys and secrets in AWS Secrets Manager.

### Deploying to AWS Lambda

1. **Package your application:** Zip your code and dependencies.
2. **Create a new AWS Lambda function:** Upload your ZIP file and set the runtime to Python 3.8 or newer. Use `main.lambda_handler` as the handler.
3. **Schedule execution with Amazon CloudWatch Events:** Create a new rule to trigger your Lambda function on a schedule.
4. **Update IAM permissions:** Ensure your Lambda function has permissions to access necessary AWS services, including Secrets Manager if used.

### AWS Lambda Environment Variables

- Instead of hardcoding sensitive information, use environment variables in the AWS Lambda console to store API keys, email addresses, and `COMPETITION_ID`.

### Usage

Once deployed and scheduled, the AWS Lambda function will run according to the schedule you set in CloudWatch Events, fetching today's football matches and sending an email without manual intervention.

## License

This project is open source and available under the MIT License.
