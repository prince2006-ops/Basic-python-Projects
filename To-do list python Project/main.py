def task():
    tasks=[]
    print("--- welcome to the task management app----")
    total_task=int(input("How many task do you want to add?"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter the task {i}:")
        tasks.append(task_name)
    print(f"Today's task are : {tasks}")

    while True:
        print("Choose an option:")
        choice=int(input("1.Add task\n2.Update task\n3.Delete Task\n4.View Task\n5.Exit\n"))
        if choice==1:
            add_task=input("Enter the task name:")
            tasks.append(add_task)
            print(f"The {add_task} task is successfully added.")
        elif choice==2:
            update_task=input("Which task do you want to update?")
            if update_task not in tasks:
                print("There is not such task in the list!❌")
            else:
                new_task=input("Enter the task to update:")
                index_task=tasks.index(update_task)
                tasks[index_task]=new_task
                print("The task is successfully updated:")
        elif choice==3:
            delete_task=input("Enter the task to delete:")
            if delete_task in tasks:
                index_task=tasks.index(delete_task)
                tasks.pop(index_task)
                print("The task is successfully deleted!")
            else:
                print("Task is not in the list!")
        elif choice==4:
            print(f"The task is {tasks}")
        elif choice==5:
            print("Exiting the program.....")
            break
        else:
            print("Input is Invalid!!")

task()
