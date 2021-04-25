
import operator


class Post:
    def __init__(self,pid,description,poster,votes):
        self.pid = pid
        self.description = description
        self.poster = poster
        self.votes = votes
    def __repr__(self):
        return '{},{} '.format(self.pid,self.votes)
    def upvote(self):
        self.votes += 1
    def downvote(self):
        self.votes -= 1
        
def add_project_idea(chron_posts, description: str, poster: str):
    #a post always starts with 1 upvote
    chron_posts.append(Post(len(chron_posts), description, poster, 1))
    #chron_posts.append([pid, poster, description, 1])
    return sorted(chron_posts,key=operator.attrgetter('votes'), reverse=True)

def up_vote(chron_posts, pid):
    chron_posts[pid].upvote()
    return sorted(chron_posts, key=operator.attrgetter('votes'),reverse = True)
    

def down_vote(chron_posts, pid):
    chron_posts[pid].downvote()
    return sorted(chron_posts, key=operator.attrgetter('votes'), reverse=True)

# chrp = []
# p = add_project_idea(chrp, "asdlfkjsldkf", "post1")
# print(p)
# p = add_project_idea(chrp, "adfsdfasdfasdfasd", "post2")
# print(p)
# p = down_vote(chrp, 0)
# p = up_vote(chrp, 0)
# print(p)