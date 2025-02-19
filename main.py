import requests
import random
import time

def click_link(link, proxy): # click a link using a proxy
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        
        parts = proxy.split(":") # check if the proxy includes authentication details
        if len(parts) == 2:  # IP and port only
            ip, port = parts
            proxy_url = f"http://{ip}:{port}"
            proxies = {
                "http": proxy_url,
                "https": proxy_url
            }
        elif len(parts) == 4:  # IP, port, username, and password
            ip, port, username, password = parts
            proxy_url = f"http://{username}:{password}@{ip}:{port}"
            proxies = {
                "http": proxy_url,
                "https": proxy_url
            }
        else:
            print(f"wrong proxy format for {proxy}")
            return

        response = requests.get(link, headers=headers, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"successfulyl clicked {link} with proxy: {proxy}")
        else:
            print(f"failed to click link {link} with proxy: {proxy}, Status code: {response.status_code}")
    except Exception as e:
        print(f"error with proxy {proxy}: {e}")

def load_proxies(file_name="MODIFY"): # load proxies from proxy file - MODIFY
    with open(file_name, "r") as f:
        proxies = f.read().splitlines()
    return proxies

def load_links(file_name="MODIFY"): # load links from a file filled with links - MODIFY
    with open(file_name, "r") as f:
        links = f.read().splitlines()
    return links

def main():
    # load proxies and links
    proxies = load_proxies()
    links = load_links()
    
    if not proxies:
        print("no proxies found in PROXY FILE")
        return
    if not links:
        print("no links found in LINKS FILE")
        return

    while True: # infinite loop to click a random link with a ranom proxy every 90 seconds
        link = random.choice(links)
        proxy = random.choice(proxies)
        print(f"clicking link {link} with proxy: {proxy}")
        click_link(link, proxy)
        print("waiting for 90 seconds before the next click")
        time.sleep(90) # modufy time to click link

if __name__ == "__main__":
    main()