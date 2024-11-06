from twitter.scraper import Scraper
from twitter.util import init_session

def IsNewVersion(latest_tweet, file):
  with open(file, "r") as f:
    firstLine = f.readline()
    if firstLine != latest_tweet:
        with open(file, 'w') as f:
          f.write(latest_tweet)
          return True
        
def scrape_x(file_path):
  scraper = Scraper(session=init_session())
  
  latest_tweet = scraper.tweets([1542707718])
  full_text = latest_tweet[0]['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
  if 'Twitch Drops' in full_text:
    if IsNewVersion(full_text, file_path):
      print('New drops are avalible')