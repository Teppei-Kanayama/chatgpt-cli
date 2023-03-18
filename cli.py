import requests
import os
import json
import sys

if __name__ == '__main__':
    prompt = sys.stdin.read()

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ.get('OPENAI_API_KEY')
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1024,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.ok:
        result = json.loads(response.content)
        message = result['choices'][0]['message']['content']

        if not 'GPT >' in message:
            message = 'GPT > ' + message

        with open('input.md', 'a') as f:
            f.write('\n' + message + '\n\n' + '私 > ')
    else:
        print(response.content)