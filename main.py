import requests
from tqdm import tqdm

def check_for_php_error(url):
    """
    Check if response code is not 200
    """
    headers = {
        # "x-borsen-native": "1"
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
    base_url = "https://lusc.borops.net"
    error_urls = []

    with open("all-unique-links.txt", "r") as file:
        links = [link.strip() for link in file.readlines()]

    for link in tqdm(links, desc="Checking URLs"):
        mst = "eyJpdiI6IlJ4aEVOMFdoOFcyeUI4SFhRMXpDYXc9PSIsInZhbHVlIjoibzFVYnRLODEwR0pGQzJpTDBRb2s3aWplM1J4MjVOVldubXkyMndxU3pOTnJ3L3B5djRISWE0WkJlNE9sVDFqZCIsIm1hYyI6ImI4ZjViMzhiMTBhMzM2MmE0NjY2N2MxODVjYzJmMWFlMTViOTNmZTljZjQyMDAzZmRjNTM1M2UyOTI3N2QxMDYiLCJ0YWciOiIifQ=="
        full_url = base_url + link + "?mst=" + mst
        if check_for_php_error(full_url):
            error_urls.append(full_url)

    if error_urls:
        with open("error_links.txt", "w") as file:
            for url in error_urls:
                file.write(url + "\n")
        print(f"Found {len(error_urls)} URLs with not 200 http errors. Check 'error_links.txt' for details.")
    else:
        print("All links are valid.")

if __name__ == "__main__":
    main()
