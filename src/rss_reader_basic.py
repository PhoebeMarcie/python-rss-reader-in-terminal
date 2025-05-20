import feedparser;
# 	http://feeds.bbci.co.uk/news/business/rss.xml
# 	http://feeds.bbci.co.uk/news/technology/rss.xml
# https://feeds.bbci.co.uk/news/rss.xml


def rss_feed():
    """
    function uses feedparser to fetch and display entries from an RSS feed
    reference tutorial:https://www.youtube.com/watch?v=ZH_Xi_1w-eg

 
    
    """
    #    1. Request user to enter an rss feed url and loop until a link is provided
    feed_link = ""
    while not feed_link:
        feed_link = input("Enter the RSS feed URL: ")
        if not feed_link:
            print("Please provide an RSS feed URL.")
        


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

    

    # 3. fetch rss feed from provided link
    feed = feedparser.parse(feed_link)
    print('\n---- Feed Entries from: ',feed_link,'------')

    if not feed.entries:
        print("No Entries found in provided feed")
    
    for entry in feed.entries[:num_links]:
        print('\n--- Entry ----')
        print(f"Title: {entry.title}")
        print(f"Description: {entry.description}")
        print(f"Link: {entry.link}")
        print()



if __name__ == "__main__":
    rss_feed()