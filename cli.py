import requests
import os
import json
import sys

URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ.get('OPENAI_API_KEY')
    }

def format_message(message):
    if not 'GPT >' in message:
        return '\nGPT > ' + message + '\n\n' + '私 > '
    return '\n' + message + '\n\n' + '私 > '

if __name__ == '__main__':
    prompt = sys.stdin.read()
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1024,
    }
    response = requests.post(URL, headers=HEADERS, data=json.dumps(data))

    if response.ok:
        result = json.loads(response.content)
        message = result['choices'][0]['message']['content']
        with open('input.md', 'a') as f:
            f.write(format_message(message))
    else:
        print(response.content)