# 🐍 Mini Social Media (Python Console App)

This is a simple **Python-based console application** that simulates a mini social media platform.  
It demonstrates the use of **core Python data structures** (List, Tuple, Set, Dictionary) along with **regex validation** for login.

---

##  Features

###  Login System
- Username + password input
- Password validation with **regex**:
  - At least 6 characters  
  - Must contain **1 uppercase letter**  
  - Must contain **1 number**  

---

###  Post Management (Lists)
- Add a post  
- Delete a post (by index)  
- View all posts  
- Search posts by keyword  
- Sort posts alphabetically  

---

###  Posts with Usernames (Tuples)
- Add a `(username, post)` pair  
- Search posts by username  

---

### #️⃣ Mentions & Hashtags (Sets + Regex)
- Extract all **hashtags (`#tag`)** and **mentions (`@user`)**  
- Display all unique hashtags  
- Display all unique mentions  
- Search if a hashtag exists  
- Find **common hashtags** between two users  

---

### 🧑‍💻 User Management (Dictionaries of Dictionaries)
- Print all active users  
- Add a new user  
- Remove a user  
- Access posts of a specific user safely with `.get()`  

---

###  Exit
- Quit the program gracefully  

---

## 🛠️ Tech Used
- **Python 3**  
- **Regex (`re` library)**  
- **Data Structures**: List, Tuple, Set, Dictionary  

---

## 📂 Example Data

```python
# Example posts
posts = ["Brunch with fam", "Sisters day out"]

# Example posts with usernames
postswithUsername = [
    ("Aaisha", "Beach day with @Arshiya"),
    ("Ali", "Finished #HPmarathon with @Omer")
]

# Example users
users = {
    "Ali": {"password": "A2004", "posts": ["Finished #HPmarathon with @Omer"]},
    "Omer": {"password": "Kp231", "posts": ["KiteRunner, A must read! #bookstagram"]}
}
