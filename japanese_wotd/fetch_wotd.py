import os
import feedparser

URL = 'http://feeds.feedblitz.com/japanese-word-of-the-day'
ROOT = os.path.dirname(os.path.dirname(__file__))


def fetch_word_of_the_day():
    rss_feed = feedparser.parse(URL)
    first_entry = rss_feed.entries[0]

    word_of_the_day = first_entry['title']
    return word_of_the_day

def main():
    readme = ROOT + 'README.md'
    print(readme)
    word_of_the_day = fetch_word_of_the_day()
    print(word_of_the_day)

if __name__ == '__main__':
    main()
