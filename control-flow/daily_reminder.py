task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_message = (f"'{task}' is a {priority} priority task")

while priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority = input("Priority (high/medium/low): ").lower()

    match priority:
        case "high":
            if time_bound == "yes":
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += ". It's important, so try to tackle it soon."
        case "medium":
            if time_bound == "yes":
                reminder_message += " that needs to be addressed today."
            else:
                reminder_message += ". Aim to complete it soon."
        case "low":
            if time_bound == "yes":
                reminder_message += " that you should get to today if possible."
            else:
                reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

        case _: 
            reminder_message = f"'{task}' has an unknown priority. Please review."

    print(f"Reminder:, {reminder_message}")