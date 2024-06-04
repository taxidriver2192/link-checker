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
        new_links = found_links - all_links  # Determine the new links found on this page
        all_links.update(found_links)

        print(f"Found {len(new_links)} new links on page {page_number}.")
        with open(f"links-page-{page_number}.txt", "w") as file:
            for link in new_links:
                file.write(link + "\n")

    print(f"Found {len(all_links)} unique internal links in total.")

if __name__ == "__main__":
    main()
