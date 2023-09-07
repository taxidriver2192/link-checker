import requests
from bs4 import BeautifulSoup

def extract_internal_links(url, domain):
    """
    Extract internal links from the given URL.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()  

        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            links.add(link)

        return links
    except requests.RequestException:
        return set()

def main():
    base_url = "https://siko.borops.net"
    all_links = set()

    with open("test-links-atikler.txt", "r") as file:
        links_to_visit = [link.strip() for link in file.readlines()]

    all_links.update(links_to_visit)

    for link in links_to_visit:
        full_url = base_url + link
        found_links = extract_internal_links(full_url, base_url)
        all_links.update(found_links)

    with open("lot-of-links.txt", "w") as file:
        for link in all_links:
            file.write(link + "\n")

    print(f"Found {len(all_links)} unique internal links. Check 'lot-of-links.txt' for details.")

if __name__ == "__main__":
    main()
