import feedparser

URL = 'http://feeds.feedblitz.com/japanese-word-of-the-day'

rss_feed = feedparser.parse(URL)
first_entry = rss_feed.entries[0]

word_of_the_day = first_entry['title']
print(word_of_the_day)
