import datetime
import calendar

expenses = []
monthly_budget = 5000.00
categories = ["🍔 Food", "🏠 Home", "💼 Work", "🎉 Fun","✈️ Travel" , "✨ Misc"]


def get_number(prompt, positive=True):
    while True:
        try:
            num = float(input(prompt))
            if not positive or num > 0:
                return num
            print("🚨 Must be positive!")
        except ValueError:
            print("🚨 Enter a valid number!")


def add_expense():
    print("\n👋 Let's add an expense!")
    name = input("➡️  What did you buy? : ")
    amount = get_number("➡️  How much? : ₹ ")
    
    print("\n🤔 Pick a category:")
    for i in range(len(categories)):
        print(f"   {i+1}. {categories[i]}")
    
    while True:
        choice = int(get_number(f"➡️  Enter 1-{len(categories)}: ", False)) - 1
        if 0 <= choice < len(categories):
            break
        print(f"🚨 Pick 1-{len(categories)}!")
    
    new_expense = {
        "name": name,
        "amount": amount,
        "category": categories[choice]
    }
    expenses.append(new_expense)
    print(f"\n✅ Added '{name}' for ₹{amount:.2f} under {categories[choice]}")


def show_summary():
    if len(expenses) == 0:
        print("\n😊 No expenses yet! Your budget is safe.")
        return

    print("\n" + "="*50)
    print("💰 YOUR EXPENSE SUMMARY")
    print("="*50)
    
    # calculate totals by category
    totals = {}
    for expense  in expenses:
        cat = expense["category"]
        if cat in totals:
            totals[cat] = totals[cat] + expense["amount"]
        else:
            totals[cat] = expense["amount"]

    print("\n📊 By Category:")
    total_spent = 0
    for cat in totals:
        amt = totals[cat]
        print(f"   {cat}: ₹{amt:.2f}")
        total_spent = total_spent + amt

    remaining = monthly_budget - total_spent
    print(f"\n💳 Total Spent: ₹{total_spent:.2f}")
    print(f"🎯 Budget: ₹{monthly_budget:.2f}")
    
    if remaining >= 0:
        print(f"✨ Left: ₹{remaining:.2f}")
    else:
        print(f"⚠️  Over by: ₹{abs(remaining):.2f}")

    # daily budget calculation
    today = datetime.datetime.now()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    days_left = days_in_month - today.day + 1
    
    if days_left > 0 and remaining > 0:
        daily = remaining / days_left
        print(f"\n💡 Daily budget for next {days_left} days: ₹{daily:.2f}")
    print("="*50)


def main():
    print("\n EXPENSE TRACKER 💰 \n")
    
    while True:
        print("\n1. ➕ Add expense | 2. 📊 Summary | 3. 👋 Exit")
        choice = input("➡️  Choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_summary()
        elif choice == '3':
            print("\n Thanks! See you soon!")
            break
        else:
            print("❌ Enter 1, 2, or 3")


if __name__ == "__main__":
    main()