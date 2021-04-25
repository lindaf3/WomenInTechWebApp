
import operator
import struct 

def add_project_idea(posts, posts_in_order, description: str, poster: str):
    #a post always starts with 1 upvote
    pid = len(posts)
    posts_in_order.append([pid, poster, description, 1])
    posts.append([pid, poster, description, 1])
    posts = sorted(posts,key=operator.itemgetter(3), reverse=True)

def up_vote(posts, posts_in_order, pid):
    posts_in_order[pid][3]+=1

    posts = sorted(posts_in_order, key=operator.itemgetter(3),reverse = True)

def down_vote(posts, posts_in_order, pid):
    posts_in_order[pid][3]-=1
    posts = sorted(posts_in_order, key=operator.itemgetter(3), reverse=True)

p = []
po = []
add_project_idea(p, po, "asdlfkjsldkf", "post1")
add_project_idea(p, po, "adfsdfasdfasdfasd", "post2")
down_vote(p, po, 0)
# down_vote(p,po, )
# up_vote(p, po, 0)
print(p)
print(po)