import requests
import xml.etree.ElementTree as ET

# 	http://feeds.bbci.co.uk/news/business/rss.xml
# 	http://feeds.bbci.co.uk/news/technology/rss.xml
# https://feeds.bbci.co.uk/news/rss.xml

def get_multiple_rss_urls():
    """
    function gets multiple feed urls from the user

    """
    print("getting multiple urls")
    feed_urls = []
    print("Enter rss URLS. type 'end' when finished")
    while True:
        # enter urls and remove any trailing spaces using .strip()
        url = input("Enter feed URL: ").strip()
        if url.lower()=='end':
            break
        if url:
            if url not in feed_urls:
                feed_urls.append(url)
            print(feed_urls)
        else:
            print("Please enter a feed URL or 'end'")

    return feed_urls


def fetch_content(feed_url):
    """this function fetches content from the feed urls"""
    print('this is url: ', feed_url)
    try:
        response = requests.get(feed_url,timeout=10)
        response.raise_for_status()
        print("response content",response.content)
        return response.content
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching feed from {feed_url}:{e}")
        return None

def parse_feed(xml_content):
    """
    Parses the RSS feed XML content using ElementTree.
    Extracts title, description, and link from each item.
    """
    if not xml_content:
        return []
    items_data = []
    try:
        root = ET.fromstring(xml_content)
        channel = root.find('channel')
        if channel is not None:
            print(f"channel found as: {channel}")
    except ET.ParseError as e:
        print(f"Error parsing XML : {e}")
    except Exception as e:
        print(f"An unexpected error occurred during parsing: {e}")
    return items_data


def multiple_url_feeds():
    """function uses custom parser to read from multiple rss urls"""
     # 1.prompt user to enter URLs and end loop by typing the word 'end'
    feed_urls = get_multiple_rss_urls()
    print(f"entered urls: {feed_urls}")
    if not feed_urls:
        print("No feed URLs provided")
        return
    
    # 2. Request user to enter number of links they would like to view
    
    num_links = None
    while num_links is None:
        num_links_str = input("Enter the number of links you want to display: ")

        if not num_links_str:
            print("Please provide the number of links: ")
            continue
        try:
            num_links = int(num_links_str)
            if num_links <0:
                print("Please enter a positive integer.")
                num_links=None
        except ValueError:
            print("Invalid input. Please enter a whole number")

     # 3. loop through getting x number of links from the provided URLs
    for url in feed_urls:
        xml_content = fetch_content(url)
        if xml_content:
            items = parse_feed(xml_content)



if __name__ == "__main__":
    multiple_url_feeds()


