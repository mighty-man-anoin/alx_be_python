task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

message = ""

match priority:
    case "high":
        message += f"Reminder: '{task}' is a high priority task"
    case "medium":
        message += f"Note: '{task}' is a medium priority task"
    case "low":
        message += f"Note: '{task}' is a low priority task"
    case _:
        print("Invalid priority level.")
        exit()
        
if time_bound == "yes":
    message += " that requires immediate attention today! Let's get it done!"
else:
    message += ". Consider completing it when you have free time. Don't forget it!"


print(message)
