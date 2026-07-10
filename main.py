import sys
import requests
import argparse
import concurrent.futures

def user_input():
    parser = argparse.ArgumentParser(description="Python Directory Buster")
    parser.add_argument("-w", "--wordlist", dest="wordlist", required=True, help="Enter wordlist name")
    parser.add_argument("-u", "--url", dest="target_url", required=True, help="Enter url name")
    parser.add_argument("-x", "--extension", nargs="+", dest="extensions", required=False, help="Enter target extensions")
    return parser.parse_args()

def target_urls(base_url, wordlist, extensions):
    target_url_list = []
    try:
        with open(wordlist, "r") as my_file:
            for line in my_file:
                endpoint = line.strip()
                if not endpoint:
                    continue

                target_url_list.append(f"{base_url}{endpoint}")
                if(extensions):
                    for ext in extensions:
                        if not ext.startswith("."):
                            target_url_list.append(f"{base_url}{endpoint}.{ext}")
                        else:
                            target_url_list.append(f"{base_url}{endpoint}{ext}")

            return target_url_list

    except FileNotFoundError:
        print(f"{wordlist} could not found !")
        sys.exit(1)

def send_request(target_url):
    try:
        response = requests.get(target_url, timeout=3)

        if (response.status_code == 200):
            print(f"[+] Found: {target_url} (Status: {response.status_code})")
        else:
            pass
    except requests.exceptions.RequestException as e:
        print(f"[!] Connection Error -> {target_url}")


args = user_input()
wordlist = args.wordlist
base_url = args.target_url
extensions = args.extensions

if not base_url.endswith("/"):
    base_url+="/"

target_url_list = target_urls(base_url, wordlist, extensions)

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(send_request, target_url_list)
