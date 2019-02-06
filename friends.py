from collections import OrderedDict

users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    # TODO
    num_friends = {}
    for a in friendship:
        if a[0] in num_friends.keys():
            num_friends[a[0]] = num_friends[a[0]] + 1
        else:
            num_friends[a[0]] = 1
        if a[1] in num_friends.keys():
            num_friends[a[1]] = num_friends[a[1]] + 1
        else:
            num_friends[a[1]] = 1
    for a in users:
        if a["name"]==user:
            user_id = a["id"]
    print("Number of friends of %s is %d" % (user,num_friends[user_id]))

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    # TOOD
    num_friends = {}
    for a in friendship:
        if a[0] in num_friends.keys():
            num_friends[a[0]] = num_friends[a[0]] + 1
        else:
            num_friends[a[0]] = 1
        if a[1] in num_friends.keys():
            num_friends[a[1]] = num_friends[a[1]] + 1
        else:
            num_friends[a[1]] = 1
    new_friends = (OrderedDict(sorted(num_friends.items(), reverse=True, key=lambda t:t[1])))
    for key,value in new_friends.items():
        print("%s : %d" % (users[key]["name"],value))
    

sort_by_num_friends()
num_friends("Chi")
num_friends("Clive")