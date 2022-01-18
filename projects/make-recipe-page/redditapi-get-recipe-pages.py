# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

import praw
from praw.models import MoreComments
from decouple import config
import re
import os
# how to rebuild website?
#api keys
#sign up for an account


reddit = praw.Reddit(
    client_id=config("CLIENT_ID"),
    client_secret=config("SECRET_TOKEN"),
    #password=config("password"),
    user_agent="Recipebot",
    #username=config("username")
)


#Authorized Instance: With authorized instance we can do whatever a normal reddit account can do. Actions like comment, post, repost, upvote etc. can be performed.
#right now it is an authorized instance

#print(reddit.user.me())
#print(reddit)


subreddit = reddit.subreddit('recipes')
# display the subreddit name
#print(subreddit.display_name)
 
# display the subreddit title
#print(subreddit.title)      
 
# display the subreddit description
#print(subreddit.description)

# url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
# submission = reddit.submission(url=url)
#submission = reddit.submission(id="3g1jfi")

dict_data={}
list_data=[]
for i in subreddit.top("all"):
    #print(i.title) #i is a submission object
    #print(f"https://www.reddit.com{i.permalink}")
    str=i.title[0:20].lower()
    str_clean=re.sub("[@_!#$%^&*()<>?'/\|}{~:\s\-\[\]]+", "_", str)
    dict_data["title"]=i.title
    dict_data["reddit_link"]=f"https://www.reddit.com{i.permalink}"
    list_data.append(dict_data.copy())
#print(list_data)
title=[]
link=[]
for i in list_data: 
    title.append(i["title"])
    link.append(i["reddit_link"])
print(title)
print(link)


cwd=os.getcwd()
print(cwd)
path="Documents\codingnomads\python-301-main_jsiu\python-301-main\projects\make-recipe-page"
#C:\Users\jsiu

def ulify(elements):
    string = "<ul>\n"
    for s in elements:
        string += "<li><a href='" + s["reddit_link"]+ "'>" + s["title"] + "</a></li>\n"
    string += "</ul>"
    return string

print(ulify(list_data))

#<li><a href="recipes/11-making-my-own-baguet.html">Making my own baguettes :)</a></li>


f = open(os.path.join(cwd, path,'recipe.html'),'w', encoding="utf-8")

message = f"""<html>
<head></head>
<body><p>
{ulify(list_data)}
</p></body>
</html>"""

f.write(message)
f.close()



#rebuild coding nomads recipe website

#TODO
#rename links
#clean title and add underscores
# loop through dictionary



#dictionary {clean_link_key:clean_link_value, title_key:title_value, reddit_link_key, reddit_link_value }