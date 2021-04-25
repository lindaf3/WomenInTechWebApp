
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

chrp = []
p = add_project_idea(chrp, "Build a website about your favorite TV series", "Bob Billy")
p = add_project_idea(chrp, "Build an android app based on a simple to-do list", "Bill Bobby")
p = add_project_idea(chrp, "Build a website about your favorite TV series", "Kaela Kealoha")
p = add_project_idea(chrp, "Build a website with the Spotify API", "Kiana Kealoha")
p = add_project_idea(chrp, "Build yourself a weather app!", "Sabrina Capello")
p = add_project_idea(chrp, "Create a website to teach people about sustainability", "Chanda Misra")
p = add_project_idea(chrp, "Make a video game!", "Billy Bob")
p = add_project_idea(chrp, "Make a health app to stay fit!","Reckless Man")
p = add_project_idea(chrp,"Location tracker for when you lose your friends","Turtle Boy")
p = add_project_idea(chrp,"Build yourself a virtual paint wheel for color mixing","Chalk Prince")
p = add_project_idea(chrp,"Build an app to help you invest money and get rich","Eclipse Star")

# p = down_vote(chrp, 0)
# p = up_vote(chrp, 0)
# print(p)