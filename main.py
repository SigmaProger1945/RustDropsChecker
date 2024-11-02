from acount_stuff import scraper

def main():
     tweets = scraper.tweets([
        ...,  # tweet ids
    ])

    df = parse_tweets(tweets)

    df.to_csv('tweets.csv')
    

if __name__ ==  "__main__":
    main()
