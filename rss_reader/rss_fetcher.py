import feedparser

class RSSFetcher:
    def __init__(self, rss_url: str):
        self.rss_url = rss_url

    def fetch(self):
        return feedparser.parse(self.rss_url)