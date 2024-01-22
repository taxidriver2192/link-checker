import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def check_for_php_error(driver, url):
    """
    Check if response code is not 200
    """
    headers = {
        #"x-borsen-native": "1"
    }
    try:
        response = requests.get(url, headers=headers)

        if 200 != response.status_code:
            print("status code : " + str(response.status_code))
            print("Url : " + url)
            print("--------------------------------------")
            driver.get(url)
            return True
        
        return False
    except requests.RequestException:
        return False


def main():
    driver = webdriver.Chrome()

    base_url = "https://lusc.borops.net"
    error_urls = []

    with open("lot-of-links.txt", "r") as file:
        links = [link.strip() for link in file.readlines()]

    for link in tqdm(links, desc="Checking URLs"):
        full_url = base_url + link
        if check_for_php_error(driver, full_url):
            error_urls.append(full_url)

    if error_urls:
        with open("error_links.txt", "w") as file:
            for url in error_urls:
                file.write(url + "\n")
        print(f"Found {len(error_urls)} URLs with not 200 http errors. Check 'error_links.txt' for details.")
    else:
        print("All links are valid.")

    driver.quit()
    
if __name__ == "__main__":
    main()
