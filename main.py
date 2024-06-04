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

    with open("test-links.txt", "r") as file:
        links = [link.strip() for link in file.readlines()]

    for link in tqdm(links, desc="Checking URLs"):
        mst = "eyJpdiI6IkZadFhEMm9FMj5YjllVWExNUthOVE9PSIsInZhbHVlIjoiTG1FcUxGMzUrV2toWkVhOUJ0M0ozbWcxbitLb2xUWkxDK3ZSaXkyY3BkSzl4MWxRcjJLc1ZxM0QrVnlDaGtzTCIsIm1hYyI6IjQ3MmE0ZWQ4MTJlMjA1NWZjMWMyNTY1YzZhZDRhNTU0ZjU3NDE5MTI5MjAxMTVmMDlkZDE5Y2ZjODExOTljMjEiLCJ0YWciOiIifQ=="
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
