import re

# Sample posts LIST
posts = ["Brunch with fam", "Sisters day out", "Hunza you beauty", "After exam glow",
         "Explored this cafe with @Amna", "Studying #python with @Halime"]

# Posts with usernames TUPLE-
postswithUsername = [
    ("Aaisha", "Beach day with @Arshiya"),
    ("Boshra", "BFF Birthday Party"),
    ("Javeria", "#HPMarathon and snacks with @aaisha"),
    ("Ali", "finished #HPmarathon with @omer"),
    ("Omer", "KiteRunner, A must read !#bookstagram")
]

# Sets will fill later (sets remove duplicates automatically)
hashtags_set = set()
mentions_set = set()

# Users nested dictionary
users = {
    "Ali": {"password": "A2004", "posts": ["finished #HPmarathon with @omer"]}, 
    "Omer": {"password": "Kp231", "posts": ["KiteRunner, A must read !#bookstagram"]}
} #here Ali is the key and remaining is another dictionary of further key(password , posts) and their values

# ================== LOGIN / SIGNUP ==================

print("===== Welcome to Mini Social Media =====")

while True:
    # LOGIN only
    username = input("Enter username: ").strip() #enters and cleans the inout from user
    password = input("Enter password: ").strip()

    # Password regex validation 
    pattern = r'^[A-Za-z0-9_]{6,}$' #(at least 6 chars, 1 uppercase, 1 number)
    if re.match(pattern, password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        print(f"\nLogin successful! Welcome {username}.")
        break   # goes to main menu later
    else:
        print("Invalid username or password format. Try again.\n")
#after hitting break it goes to next section which is main menu 

 # ================== MAIN MENU ==================
while True:
    print("\n===== Mini Social Media - Post Manager =====")
    #=========== List based ================
    print("1. Add a post(List)") 
    print("2. Delete a post by index")
    print("3. View all posts")
    print("4. Search posts by keyword")
    print("5. Sort posts alphabetically")
     #=========== Tuple based ================
    print("6. Add posts with Username(Tuple)") 
    print("7. View posts with Usernames")
     #=========== Set based ================
    print("8. Extract hashtags & mentions from all posts(Set)") 
    print("9. Show all unique hashtags")
    print("10. Show all unique mentions")
    print("11. Check if a hashtag exists")
    print("12. Common hashtags between two usernames")
     #=========== Dictionary based ================
    print("13. Print the list of users")
    print("14. Add users in dict")
    print("15. Remove users")
    print("16. Access their posts")
    print("17. Exit")
    
    
    choice = input("Select an option (1-17): ")
    
    #============== LIST OPTION================
    if choice == "1":
        ask = input("What do you want to post? ")
        posts.append(ask.strip())
        print("Post added successfully!\n")
        print(posts)
        
    elif choice == "2":
        ind = int(input("Enter the index you want to delete: "))
        posts.pop(ind)
        print("Post deleted successfully!")
        
    elif choice == "3":
        print(posts)
        
    elif choice == "4":
        tosearch = input("Which post do you want to search? ").strip().lower()
        found = False
        for post in posts:
            if tosearch in post.lower():
                print(f"'{tosearch}' found in: {post}") 
                found = True
        if not found:
            print(f"'{tosearch}' not found!")
            
    elif choice == "5":
        posts.sort()
        print(posts)

 #============== TUPLE OPTION================
    elif choice == "6":
        username = input("Enter the username:\t")
        message = input("Enter the post:\t")
        newpost = (username, message)
        postswithUsername.append(newpost)
        print("Post with username added successfully!\n")
        print(postswithUsername)

    elif choice == "7":
        searchkey = input("Enter the username you want to search the post for?:\t").strip()
        found = False
        for username, message in postswithUsername:
            if searchkey.lower() == username.lower():
                print(f"Username: {username}, Post: {message}")
                found = True
        if not found:
            print(f"'{searchkey}' doesn't exist")
    
    
# ============== SET OPTION================
    elif choice == '8':  # Extract hashtags & mentions
        tagpattern = r"#[a-zA-Z0-9_]+"
        mentionpattern = r"@[a-zA-Z0-9_]+"

        hashtags_set.clear()
        mentions_set.clear()

        # Collect from list posts
        for post in posts:
            hashtags_set.update(re.findall(tagpattern, post))
            mentions_set.update(re.findall(mentionpattern, post))

        # Collect from tuple posts
        for username, message in postswithUsername:
            hashtags_set.update(re.findall(tagpattern, message))
            mentions_set.update(re.findall(mentionpattern, message))

        # Collect from dict user posts
        for user, details in users.items():
            for post in details.get("posts", []):
                hashtags_set.update(re.findall(tagpattern, post))
                mentions_set.update(re.findall(mentionpattern, post))

        print("Hashtags found:", hashtags_set if hashtags_set else "None")
        print("Mentions found:", mentions_set if mentions_set else "None")


    elif choice == '9':  # Show all unique hashtags
        tagpattern = r"#[a-zA-Z0-9_]+"
        hashtags_set = set()

        for post in posts:
            hashtags_set.update(tag.lower() for tag in re.findall(tagpattern, post))
        for username, message in postswithUsername:
            hashtags_set.update(tag.lower() for tag in re.findall(tagpattern, message))
        for user, details in users.items():
            for post in details.get("posts", []):
                hashtags_set.update(tag.lower() for tag in re.findall(tagpattern, post))

        print("Hashtags found:", hashtags_set if hashtags_set else "None")


    elif choice == '10':  # Show all unique mentions
        mentionpattern = r"@[a-zA-Z0-9_]+"
        mentions_set = set()

        for post in posts:
            mentions_set.update(re.findall(mentionpattern, post))
        for username, message in postswithUsername:
            mentions_set.update(re.findall(mentionpattern, message))
        for user, details in users.items():
            for post in details.get("posts", []):
                mentions_set.update(re.findall(mentionpattern, post))

        print("Mentions found:", mentions_set if mentions_set else "None")


    elif choice == '11':  # Check if a hashtag exists
        tagpattern = r"#[a-zA-Z0-9_]+"
        hashtags_set = set()

        for post in posts:
            hashtags_set.update(re.findall(tagpattern, post))
        for username, message in postswithUsername:
            hashtags_set.update(re.findall(tagpattern, message))
        for user, details in users.items():
            for post in details.get("posts", []):
                hashtags_set.update(re.findall(tagpattern, post))

        tagsearch = input("Enter the hashtag to search (with #):\t").strip()
        if tagsearch in hashtags_set:
            print(f"Yes, {tagsearch} exists in posts.")
        else:
            print(f"No, {tagsearch} not found.")

    elif choice == '12':  # Common hashtags between two usernames
        tagpattern = r"#[a-zA-Z0-9_]+"

        user1 = input("Enter the first username:\t").strip()
        user2 = input("Enter the second username:\t").strip()

        user1_tags = set()
        user2_tags = set()

        for username, message in postswithUsername:
            if username.lower() == user1.lower():
                user1_tags.update(tag.lower() for tag in re.findall(tagpattern, message)) #convert in lower case for unique to normalise
            if username.lower() == user2.lower():
                user2_tags.update(tag.lower() for tag in re.findall(tagpattern, message))

        common = user1_tags.intersection(user2_tags)

        if common:
            print(f"Common hashtags between {user1} and {user2}: {common}")
        else:
            print(f"No common hashtags between {user1} and {user2}.")

    elif choice == '13':  # Print all users
        print("Active users:\n")
        for user, details in users.items():#user is just like omer or ali and remaining is its details(password & post)
            print(f"User: {user}, Password: {details['password']}, Posts: {details['posts']}") #here it fetches both details password and posts

    elif choice == '14':  # Add a new user
        key = input("Enter new username:\t").strip()
        password = input("Enter password for user:\t").strip()
        
        # Ask if user wants to add an initial post
        post = input("Enter a post for this user (leave empty if none):\t").strip()
        
        posts_list = []
        if post:  # only add if not empty
            posts_list.append(post)
        
        users[key] = {"password": password, "posts": posts_list}  # dictionary for user
        print("User added successfully!")
        print(users)


    elif choice == '15':  # Remove a user
        topop = input("Enter the username you want to remove:\t").strip()
        if topop in users:
            users.pop(topop)
            print(f"User '{topop}' removed successfully.")
        else:
            print(f"User '{topop}' not found.")
        print(users)

    elif choice == '16':  # Access user posts
        show = input("Enter the username whose posts you want to see:\t").strip()
        user_details = users.get(show)   # safely get user dictionary
        
        if user_details:  # if user exists
            print(f"Posts of {show}: {user_details.get('posts', [])}") #if the user exists and post found then show otherwise print empty [] dict
        else:
            print(f"User '{show}' not found.")

    elif choice == '17':
        print("Exiting program... Goodbye! ")
        break
    
    else:
        print("Invalid choice, please select again.")
