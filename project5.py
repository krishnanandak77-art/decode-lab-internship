def track_expense():
    print("enter your expense amount")
    print("when you are finished type done")
    total_spend=0.0
    while True:
        user_input= input("enter the expense amount: ").strip()
        if user_input.lower()=='done':
            break
        try:
            new_expense=float(user_input)
            if new_expense<0:
                print("please enter a positive number")
                continue
            total_spend=total_spend+new_expense
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'done'.")

    # Moved outside the function loop/blocks
    print("\n")
    print(f"Total Spent: ${total_spend:.2f}")

# Moved completely outside the function to the main level
if __name__ == "__main__":
    track_expense()
