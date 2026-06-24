tasks = []
while True:
    print ("\n list of choice")
    print("1.enter the task in to the list")
    print("1.read the task")
    print("3.exist")
    choice=input("enter your choice:")
    if choice=="1":
        print("enter the task in to the list")
        task=input("enter the task:")
        tasks.append(task)
        print("task is entered successfully")
    elif choice=="2":
        print("looking for the task...")
        if len(task)==0:
            print("no task is in the list")
        else:
            print("task:")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}. {tasks}")
    elif choice=="3":
        print("exiting the program...")
        break
    else:
        print("theren no existing choice")


