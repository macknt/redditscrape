import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="lenMM2Zo0kCs_ixpLBqU4g",         # your client id
                               client_secret="A_n9C4u9wy-tiliBchFjXan8WRKbXg",      # your client secret
                               user_agent="usmcscrape")


subreddit = reddit_read_only.subreddit("usmc")

print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
# print("Description:", subreddit.description)

posts = subreddit.top("month")

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

for post in posts:
    posts_dict["Title"].append(post.title)

    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)

    # Unique ID of each post
    posts_dict["ID"].append(post.id)

    # The score of a post
    posts_dict["Score"].append(post.score)

    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)

    # URL of each post
    posts_dict["Post URL"].append(post.url)

top_posts = pd.DataFrame(posts_dict)
top_posts