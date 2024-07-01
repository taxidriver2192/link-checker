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
    base_url = "https://lusc.borops.net/nyheder/side/"
    all_links = set()

    for page_number in range(1, 11):  # Iterate over pages 1 to 10
        full_url = base_url + str(page_number)
        found_links = extract_internal_links(full_url, base_url)
        all_links.update(found_links)  # Update all_links with new found links
        print(f"Processed page {page_number}.")

    print(f"Found {len(all_links)} unique internal links in total.")

    # Write all unique links to a single file
    with open("all-unique-links.txt", "w") as file:
        for link in all_links:
            file.write(link + "\n")
if __name__ == "__main__":
    main()
