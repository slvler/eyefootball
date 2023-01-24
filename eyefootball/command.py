import feedparser

class command:
  def __init__(self, url):
    self.url = url

  def football_full_command(self):
    url = self.url + "football_news.xml"
    items = feedparser.parse(url)
    return items

  def football_command(self):
    url = self.url + "rss_news_main.xml"
    items = feedparser.parse(url)
    return items

  def football_transfer_command(self):
    url = self.url + "rss_news_transfers.xml"
    items = feedparser.parse(url)
    return items

  def football_blogs_command(self):
    url = self.url + "rss_football_blogs.xml"
    items = feedparser.parse(url)
    return items

  def mobile_site_command(self):
    url = self.url + "mobile.xml"
    items = feedparser.parse(url)
    return items
