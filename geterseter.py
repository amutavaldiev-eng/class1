# class Bank:
#     def __init__(self, owner, pinkod, balance):
#         self.owner = owner
#         self.__pinkod = pinkod
#         self._balance = balance

#     @property
#     def show_balance(self):
#         return f"Balance: {self._balance}"

#     @show_balance. setter
#     def show_balance(self, amount):
#         if amount > 0:
#             self._balance+=amount
#             return f"New balance {self._balance}"

# card1 = Bank("Ehson", 1234, 10000)

# print(card1.show_balance)
# card1.show_balance = 10
# print(card1.show_balance)









from datetime import datetime
task_db = []
user_db = []
is_login = None
user_id = 0
task_id = 0 

def create_task(title, description, dueration):
    global task_id
    task_id+=1
    task = {
        "task_id": task_id,
        "title":title,
        "description": description,
        "dueration": dueration,
        "status": False,
        "created_at": datetime.now(),
        "username": is_login["username"],
    }
    task_db. append(task)



def read_task(task_id):
    for i in task_db:
        if i["task_id"] == task_id:
            return f"""
Your task {i["task_id"]}:
Username: {i["username"]}
Title:{i["title"]}
Description:{i["description"]}
Dueration :{i["dueration"]}
Status:{i["status"]}
"""
    else:
        return False
    
    
def registration(username, password):
    global user_id, is_login
    user_id+=1
    user = {
        "user_id": user_id,
        "username": username,
        "password": password,
        "created_at": datetime.now()
    }
    user_db.append(user)
    is_login = user
    
    
    
def update_task(task_id, title, descp, due, status):
    for i in task_db:
        if i["task_id"]==task_id:
            if title:
                i["title"] = title
            if descp:
                i["description"] = descp
            if due:
                i["dueration"] = due
            if status:
                i["status"] = status

def delete_task(task_id):
    for i in task_db:
        if i["task_id"] == task_id:
            task_db.remove(i)
            return True

        else:
            return False
        
        
def login(username, password):
    global is_login

    for user in user_db:
        if user["username"] == username and user["password"] == password:
            is_login = user
            print("Welcome again!\n")
            return True

        else:
            print("Wrong username or password!")
            return False
def logout():
    global is_login
    is_login = None
    print("Logout successful!\n")
    
    
def change_password(old, new):
    if is_login["password"] == old:
        is_login["password"] = new
        print("Password changed!\n")
    else:
        print("Wrong password!\n")
def help_task():
    print("""
________________________________
1) Create Task
     Create a new task.
     You need to enter:
     Title
     Description
     Duration
________________________________
2) Read Task
   Show information about a task.
   You need to enter Task ID.
________________________________
3) Update Task
     Change task information.
     You can change:
     Title
     Description
     Duration
________________________________
4) Delete Task
     Delete a task.
     You need to enter task Id.
________________________________
5) Show Profile
     Show your user information.
     User ID
     Username
     Created time
________________________________
6) Change Password
     Change your password.
     Enter old password and new password.
________________________________
7) Search User
     Search for a user by username.
     Enter username to find the user.
________________________________
8) Log out
     Log out from your account.
________________________________
0) Exit
     Exit the program.
________________________________
""")

def show_profile():
    print(f"""
User id: {is_login["user_id"]}
Username: {is_login["username"]}
Created time is : {is_login["created_at"]}
""")
    
    
    
def search_user(username):
    for user in user_db:
        if user["username"] == username:
            print(f"""
User id: {user["user_id"]}
Username: {user["username"]}
Created time: {user["created_at"]}
""")
            return

    print("User not found")
                  

while True:
        
    if is_login == None:
        n = int(input("1)Registration\n2)Login\n0)Exit\nChouse one:"))
        match n:
            case 1:
                username = input("Username: ")
                password = input("Password : ")
                registration(username, password)
            case 2:
                username = input("Username: ")
                password = input("Password: ")
                login(username, password)
            case 0:
                print("Good bye")
                break 
    
        
    
    else:
        n = int(input("1)Create Task\n2)Read task\n3)Update Task\n4)Delete\n5)Show Profile\n6)Change Password\n7)Search User\n8)Log out\n9)Help?\n0)Exit\nChouse one: "))
        match n:
            case 1:
                print("Start create task")
                title = input("Title: ")
                descp = input("Description: ")
                durat = input("Duration: ")
                create_task(title, descp, durat)
                print("Task created !! ")

            case 2:
                k = int(input("Enter id task: "))
                print(read_task(k))
            case 3:
                print("Start update task")
                k = int(input("Enter id task: "))
                if read_task(k):
                    title = input("Title or put enter for continue: ")
                    descp = input("Description or put enter for continue: ")
                    durat = input("Duration or put enter for continue: ")
                    status = bool(input("Status or put enter for continue: "))
                    update_task(k, title, descp, durat, status)
                    print("Task update !! ")
                else:
                    print("This task dinaded")
            case 4:
                k = int(input("Enter id task: "))
                if delete_task(k):
                    print("Your task deleted!")
                else:
                    print("This task dinaded")
            case 5:
                show_profile()
            case 6:
                old = input("Old password: ")
                new = input("New password: ")
                change_password(old, new)
            case 7:
                username = input("Enter username: ")
                search_user(username)
            case 8:
                logout()
            case 9:
                help_task()
            case 0:
                print("Exit")
                break
            case _:
                print("Invalid input!")
                


