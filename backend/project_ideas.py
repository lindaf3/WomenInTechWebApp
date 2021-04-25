
def addProjectIdea(posts, description: str, poster: str):
    #a post always starts with 1 upvote
    pid = len(posts)
    posts.insert([pid, poster, description, 1])
    posts = sorted(posts, reverse = true, key=operator.itemgetter(3))

def up_vote(posts, pid):
    posts[pid][3]+=1
    posts = sorted(posts, reverse = true, key=operator.itemgetter(3))

def down_vote(posts, pid):
    post[pid][3]-=1
    posts = sorted(posts, reverse = true, key=operator.itemgetter(3)) 

