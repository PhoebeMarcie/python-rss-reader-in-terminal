import os;
import time;
import feedparser;


def rss_feed():
    """
    function uses feedparser
    
    """
    feed_link = "https://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(feed_link)

    num_links = int(input("Number of links: "))
    print('printing here')

    if not feed.entries:
        print("No entries found in the feed.")
        return

    for link in feed.entries[:num_links]:
        print('finding links')
        print(link.title)
        print(link.description)
        print(link.link)
        print()

rss_feed()