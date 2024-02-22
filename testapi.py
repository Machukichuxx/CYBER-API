# test_api_key.py
import requests

def test_api_key(api_key):
    url = "https://api.openai.com/v1/engines/davinci/codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": "Hello, ChatGPT!",
        "max_tokens": 5
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("API Key is valid!")
        print("Response:", response.json())
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    api_key = "sk-ouY0MxHl093nBl50TjfgT3BlbkFJ62faPoUHvP7UojLvN6o"  # Replace this with your actual API key
    test_api_key(api_key)
