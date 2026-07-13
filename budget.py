name = input("name: ")
total_budget= float(input("total budget: "))
saving = float(input(" how much to save: "))
spendable= total_budget - saving
shopping_list =[]
levels = ["high", "medium", "low"]
while True:
    items= input("What do you want to spend on :  ")
    if items == "done":
        break
    levels= input(" Preference for this high/medium/low : ")
    shopping_list.append({"item" : items , "level" : levels})
high_count =len([i for i in shopping_list if i["level"] == "high"])
medium_count = len([i for i in shopping_list if i["level"] == "medium"])
low_count = len([i for i in shopping_list if i["level"] == "low"])
high_budget = (spendable*0.50) / high_count if high_count > 0 else 0
medium_budget = (spendable*0.30) / medium_count if medium_count > 0 else 0
low_budget = (spendable*0.20) / low_count if low_count > 0 else 0
print(f"\n YOUR BUDGET ALLOCATION :")
for item in shopping_list:
    if item["level"] == "high":
        print(f"{item['item']} = Rs. {high_budget} ")
    elif item["level"]=="medium":
        print(f"{item['item']} = Rs. {medium_budget}")
    else:
        print(f"{item['item']} = Rs. {low_budget}")
        with open("budget.txt", "w") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Total Budget: Rs. {total_budget}\n")
            f.write(f"Saving: Rs. {saving}\n")
            f.write(f"Spendable: Rs. {spendable}\n")
            f.write("Budget Allocation:\n")
            for item in shopping_list:
                if item["level"] == "high":
                    f.write(f"{item['item']} = Rs. {high_budget}\n")
                elif item["level"] == "medium":
                    f.write(f"{item['item']} = Rs. {medium_budget}\n")
                else:
                    f.write(f"{item['item']} = Rs. {low_budget}\n")
                    print("\nBudget allocation saved to budget.txt")