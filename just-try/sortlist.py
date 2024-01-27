#fix this code so that it prints a sorted list of all of our friends (alphabetical).
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend)
sort_friend=sorted(friends)
print(sort_friend)  