class User:
    def __init__(self, id, name, followers=0):
        self.id = id
        self.name = name
        self.followers = followers 
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

user1 = User(1, "java") 
user2 = User(2, "python") 
user1.follow(user2)
print(f"{user1.name} {user1.followers} {user1.following}") 
print(f"{user2.name} {user2.followers} {user2.following}") 
