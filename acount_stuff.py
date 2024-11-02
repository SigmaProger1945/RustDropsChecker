from twitter.account import Account
from twitter.util import find_key
from twitter.scraper import Scraper
import pandas as pd

account = Account(cookies={"ct0": "1eff6573eaecd28342862c0cc414a250545aa95cb8c38b7fed9d6dde6aed9887fcddad54df29cec69d9bf415b98b4e36b82d077cdd3c4c513100d485fdb1919e5c54d3674bc03c6a32935cbe142aa771", "auth_token": "d8144081fabb7b990d2ca5df4c1f57092332d87e"})
scraper = Scraper(cookies={"ct0": "1eff6573eaecd28342862c0cc414a250545aa95cb8c38b7fed9d6dde6aed9887fcddad54df29cec69d9bf415b98b4e36b82d077cdd3c4c513100d485fdb1919e5c54d3674bc03c6a32935cbe142aa771", "auth_token": "d8144081fabb7b990d2ca5df4c1f57092332d87e"})

tweets = scraper.tweets_by_ids([1849850992453615949,1852712277943660952])
user = scraper.tweets('playrust')
full_text = tweets[0]['data']['tweetResult'][0]['result']['legacy']['full_text']
print(full_text, user)