import praw
import Private
from tickers import allTickers

reddit = praw.Reddit(
    client_id = Private.client_id,
    client_secret = Private.client_secret,
    password = Private.password,
    user_agent = Private.user_agent,
    username = Private.username
)
def Parse():
    subreddit = reddit.subreddit('wallstreetbets')
    hot_WSB = subreddit.hot(limit=60)  # including pinned posts limits posts read
    # sub= []
    # for submission in hot_WSB:
    #     if not submission.stickied:
    #         sub.append(submission.title)

    ignoredTickers = ["I", "A", "IT", "CASH", "B","DD","CEO","FOR","MM","HF","UK","ALL","ARE",
                      "BK","DO","G","LOVE","ON","ANY","CAN","GO","DM","F","L"]

    for submission in hot_WSB:
        if not submission.stickied:  # neglects pinned posts
            title = str(submission.title)
            if "GME Megathread" not in title:
                #print(title)  # prints the post name
                submission.comments.replace_more(limit=None)
                count = 0
                for comment in submission.comments:
                    for ticker in allTickers:
                        if ticker not in ignoredTickers:
                            # if (" " + ticker + " ") in comment.body.lower():
                            if ((" " + ticker + " ") or ("$" + ticker)) in comment.body:
                                # print(comment.body)
                                allTickers[ticker] += 1

            # print(comment.body) #prints top level comments
    # remove all tickers that have a value of 0
    relevantTickers = {ticker: value for ticker, value in allTickers.items() if value > 2}

    # get top 5 tickers
    # mostPopular = sorted(relevantTickers, key=relevantTickers.get, reverse=True)[:5]
    mostPopular = dict(sorted(relevantTickers.items(), key=lambda item: item[1], reverse=True))
    #print(mostPopular)

    return(mostPopular)


#print(Parse())
