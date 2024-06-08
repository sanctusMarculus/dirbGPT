import openai
import os
import requests
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_wordlist(prompt, max_tokens=2000):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates wordlists for directory brute-forcing."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.5,
    )
    wordlist = response['choices'][0]['message']['content'].strip().split("\n")
    return wordlist

def scan_website(base_url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(base_url)
    links = driver.find_elements(By.TAG_NAME, "a")
    paths = set()
    for link in links:
        href = link.get_attribute("href")
        if href and href.startswith(base_url):
            path = href.replace(base_url, "")
            if path and path not in paths:
                paths.add(path)
    driver.quit()
    return list(paths)

def scan_hidden_dirs(base_url, wordlist):
    found_dirs = []
    for word in wordlist:
        url = f"{base_url}/{word.strip()}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                found_dirs.append(url)
                print(f"Found: {url}")
            else:
                print(f"Not found: {url}")
        except requests.RequestException as e:
            print(f"Error accessing {url}: {e}")
    return found_dirs

def main():
    parser = argparse.ArgumentParser(description='Scan website for hidden directories using Selenium and OpenAI GPT-3.5-turbo.')
    parser.add_argument('base_url', type=str, help='Base URL of the website to scan')
    args = parser.parse_args()

    base_url = args.base_url
    print("Scanning website using Selenium...")
    scanned_paths = scan_website(base_url)
    print(f"Scanned paths: {scanned_paths}")

    prompt = f"Generate at least 1000 wordlist entries based on these paths: {', '.join(scanned_paths)}"
    print("Generating extended wordlist using GPT-3.5-turbo...")
    extended_wordlist = generate_wordlist(prompt)
    print(f"Generated extended wordlist: {extended_wordlist[:10]}...")

    with open("extended_wordlist.txt", "w") as f:
        for word in extended_wordlist:
            f.write(f"{word}\n")
    
    print("Extended wordlist saved to extended_wordlist.txt")

    print("Scanning for hidden directories...")
    found_dirs = scan_hidden_dirs(base_url, extended_wordlist)

    with open("found_dirs.txt", "w") as f:
        for dir in found_dirs:
            f.write(f"{dir}\n")
    
    print("Found directories saved to found_dirs.txt")

if __name__ == "__main__":
    main()
