import os
import re
import feedparser

URL = 'http://feeds.feedblitz.com/japanese-word-of-the-day'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORD_FRAMEWORK = '💬 Japanese Word of the Day --> {}.'
WOTD_TAG = 'japanese_wotd'


class ReadMe():
    def __init__(self):
        self.readme_data = self.get_readme_data()
        self.new_readme = None


    @property
    def filepath(self):
        filepath = os.path.join(ROOT, 'README.md')
        return filepath
    

    def get_readme_data(self):
        with open(self.filepath) as read_file:
            readme_data = read_file.read()

        return readme_data


    def replace_word_of_the_day(self, new_wotd):
        regex_pattern = re.compile(r"<!-- {} starts -->.*<!-- {} ends -->".format(
                WOTD_TAG, WOTD_TAG), re.DOTALL,)

        wrapped_new_wotd = WORD_FRAMEWORK.format(new_wotd)
        new_wotd_text = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(
            WOTD_TAG, wrapped_new_wotd, WOTD_TAG)

        self.new_readme = regex_pattern.sub(new_wotd_text, self.readme_data)


    def save_readme(self):
        with open(self.filepath, 'w') as write_file:
            write_file.write(self.new_readme)


def fetch_word_of_the_day():
    rss_feed = feedparser.parse(URL)
    first_entry = rss_feed.entries[0]

    word_of_the_day = first_entry['title']
    return word_of_the_day


def main():
    word_of_the_day = fetch_word_of_the_day()
  
    readme = ReadMe()
    readme.replace_word_of_the_day(new_wotd=word_of_the_day)
    readme.save_readme()


if __name__ == '__main__':
    main()
