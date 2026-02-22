import json

tasks = {}

def add_task():
        task = input("\nAdd a task ").strip()
        tasks.update({task:{"is_it_done":"❌"}})
        return tasks
    
def view_tasks():
    print("Task     Complete")
    for num , (task,status) in enumerate(tasks.items()):
        print(f"{num + 1}.{task}       {status['is_it_done']}\n")

def mark_as_done():
    for num , (task,status) in enumerate(tasks.items()):
        print(f"{num + 1}.{task}    {status['is_it_done']}\n")
        
    done = input("\nWhich task is done ? ").strip()

    if done in tasks.keys():
        tasks[done]["is_it_done"] = "✅"
        return tasks
    return f"Task : {done} does not exist\n" 

def delete_task():
    for num , (task,status) in enumerate(tasks.items()):
        print(f"{num + 1}.{task}    {status['is_it_done']}\n")
    user_choice = input("Which task do you want to delete ").strip()
    if user_choice in tasks.keys():
        tasks.pop(user_choice)
        return tasks
    return f"Can't delete : {user_choice} it does not exists"

def save_tasks_json(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)

def load_tasks_json():
    try:
        with open("tasks.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    



def app():
    while True:
        print("1.Add a task\n2.View tasks\n3.Mark task done\n4.Delete task\n5.Exit\n")
        try:
            user_choice = int(input("Pick an option "))
        except ValueError:
            print("Please enter a valid number\n")
            continue

        if user_choice == 1:
            save_tasks_json(add_task())
        
        elif user_choice == 2:
            view_tasks()
        
        elif user_choice == 3:
            mark_as_done()
        
        elif user_choice == 4:
            delete_task()


        elif user_choice == 5:
            print("Bye :) .....")
            break
        else:
            print("Invalid option :( \n")


        

if __name__ == "__main__":
    app()