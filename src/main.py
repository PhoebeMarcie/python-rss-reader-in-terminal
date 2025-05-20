import os;
import time;
import feedparser;

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

def process_feeds(feed_url,num_links_to_display):
    """this function takes a feeder url and number of links to be generated from the url """

    feed = feedparser.parse(feed_url)
    print('\n---- Feed Entries from: ',feed_url,'------')

    if not feed.entries:
        print("No Entries found in provided feed")
    
    for entry in feed.entries[:num_links_to_display]:
        print('\n--- Entry ----')
        print(f"Title: {entry.title}")
        print(f"Description: {entry.description}")
        print(f"Link: {entry.link}")
        print()

def multiple_url_feeds():
    """
    function uses feedparser to display feeds from multiple rss url
    """
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
        process_feeds(url,num_links)



if __name__ == "__main__":
    # rss_feed()
    multiple_url_feeds()