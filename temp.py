import praw
from tickers import allTickers
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)
subreddit = reddit.subreddit('wallstreetbets')
hot_WSB = subreddit.hot(limit=5) # including pinned posts limits posts read
# sub= []
# for submission in hot_WSB:
#     if not submission.stickied:
#         sub.append(submission.title)

ignoredTickers = ["I","A","IT","CASH","B"]

for submission in hot_WSB:
    if not submission.stickied: #neglects pinned posts
        title = str(submission.title)
        if "GME Megathread" not in title:
            print(title)  # prints the post name
            submission.comments.replace_more(limit=None)
            count = 0
            for comment in submission.comments:
                for ticker in allTickers:
                    if ticker not in ignoredTickers:
                        #if (" " + ticker + " ") in comment.body.lower():
                        if ((" "+ ticker +" ") or ("$"+ticker)) in comment.body:
                            #print(comment.body)
                            allTickers[ticker] += 1

        # print(comment.body) #prints top level comments
# remove all tickers that have a value of 0
relevantTickers = {ticker : value for ticker,value in allTickers.items() if value > 1}
print(relevantTickers)

#get top 5 tickers
#mostPopular = sorted(relevantTickers, key=relevantTickers.get, reverse=True)[:5]
mostPopular = dict(sorted(relevantTickers.items(), key=lambda item: item[1],reverse=True))
print(mostPopular)



