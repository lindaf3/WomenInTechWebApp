
import operator
import struct 

def add_project_idea(chron_posts, description: str, poster: str):
    #a post always starts with 1 upvote
    pid = len(chron_posts)
    chron_posts.append([pid, poster, description, 1])
    return sorted(chron_posts,key=operator.itemgetter(3), reverse=True)

def up_vote(chron_posts, pid):
    chron_posts[pid][3]+=1
    
    return sorted(chron_posts, key=operator.itemgetter(3),reverse = True)
    

def down_vote(chron_posts, pid):
    chron_posts[pid][3]-=1
    return sorted(chron_posts, key=operator.itemgetter(3), reverse=True)

chrp = []
p = add_project_idea(chrp, "asdlfkjsldkf", "post1")
print(p)
p = add_project_idea(chrp, "adfsdfasdfasdfasd", "post2")
print(p)
p = down_vote(chrp, 0)
print(p)