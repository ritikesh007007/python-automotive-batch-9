# Movie Ticket Discount System for Senior Citizens
# Group Booking - 6 Members
# Discount Rate = 20%

DISCOUNT_RATE = 20
MAX_MEMBERS = 6

# 1️⃣ Function to get user details
def get_user_details(member_no):
    print(f"\nEnter details for Member {member_no}")
    name = input("Name: ")
    age = int(input("Age: "))
    price = float(input("Ticket Price: "))
    return name, age, price


# 2️⃣ Function to check senior citizen
def check_senior_citizen(age):
    if age >= 60:
        return True
    else:
        return False


# 3️⃣ Function to calculate discount
def calculate_discount(price):
    discount = (price * DISCOUNT_RATE) / 100
    return discount


# 4️⃣ Function to calculate final ticket amount
def calculate_final_price(price, discount, is_senior):
    if is_senior:
        return price - discount
    else:
        return price


# 5️⃣ Function to display member result
def display_member_result(name, is_senior, final_price):
    print("\n--- Ticket Summary ---")
    print("Name:", name)
    print("Senior Citizen:", is_senior)
    print("Final Ticket Price:", final_price)


# 6️⃣ Function to calculate average price
def calculate_average(total, count):
    return total / count


# ---------------- Main Program ----------------
try:
    total_amount = 0

    print("\n🎬 MOVIE TICKET DISCOUNT SYSTEM 🎬")
    print("Senior Citizen Discount: 20%")
    print("Maximum Members:", MAX_MEMBERS)

    for i in range(1, MAX_MEMBERS + 1):
        name, age, price = get_user_details(i)

        is_senior = check_senior_citizen(age)
        discount = calculate_discount(price)
        final_price = calculate_final_price(price, discount, is_senior)

        display_member_result(name, is_senior, final_price)

        total_amount += final_price

    average_price = calculate_average(total_amount, MAX_MEMBERS)

    print("\n========== GROUP SUMMARY ==========")
    print("Total Members:", MAX_MEMBERS)
    print("Total Amount to Pay:", total_amount)
    print("Average Ticket Price:", average_price)

# Handling wrong inputs
except ValueError:
    print("\n❌ Error: Please enter valid numeric values!")

# Handling unexpected errors
except Exception as e:
    print("\n❌ Unexpected Error:", e)

# Finally block
finally:
    print("\n✅ Booking process completed.")
    print("Thank you for using the Movie Ticket System 🎥")