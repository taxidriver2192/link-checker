import requests
from tqdm import tqdm

def check_for_php_error(url):
    headers = {
        "x-borsen-native": "1"
    }
    try:
        response = requests.get(url, headers=headers)
        if 200 != response.status_code:
            print("status code : " + str(response.status_code))
            print("Url : " + url)
            print("--------------------------------------")
            return True
        
        return False
    except requests.RequestException:
        return False

def main():
    base_url = "https://siko.borops.net"
    error_urls = []

    with open("test-links.txt", "r") as file:
        links = [link.strip() for link in file.readlines()]

    for link in tqdm(links, desc="Checking URLs"):
        full_url = base_url + link
        if check_for_php_error(full_url):
            error_urls.append(full_url)

    if error_urls:
        with open("error_links.txt", "w") as file:
            for url in error_urls:
                file.write(url + "\n")
        print(f"Found {len(error_urls)} URLs with PHP errors. Check 'error_links.txt' for details.")
    else:
        print("No PHP errors found in the provided URLs.")

if __name__ == "__main__":
    main()
