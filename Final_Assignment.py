# SECTION A: FOR-LOOP

# Answer # 1
files = ["Pdf", "Image", "MyFile", "Mails"]
for file in files:
    print(file)

# # Answer # 2
students = [
    {"name": "Abid", "roll_number": 1},
    {"name": "Karim", "roll_number": 2},
    {"name": "Ibad", "roll_number": 3},
    {"name": "Adeel", "roll_number": 4}
]

for student in students:
    print(f"Name:{student['name']}, Roll Number:{student['roll_number']}")

# #Answer # 3
mails = ["mymail@gmail.com", "xyz@youmail.com", "abs@gmail.com", "vss@otmail.com", "firstmail@gmail.com" ]
for mail in mails:
    if mail.endswith("@gmail.com"):
        print(mail)

# Answer # 4
products_li = [
    {"product": "Shampoo", 'price': 200},
    {"product": "Soap", 'price': 120},
    {"product": "Conditioner", 'price': 400},
    {"product": "Towel", 'price': 350},
]
for product_li in products_li:
    print(f"Product: {product_li['product']}, Price: {product_li['price']} PKR")

# Answer # 5
contacts = [
    "+92334-2333413",
    "+92231-2312344",
    "+92345-9284921",
    "+92365-1585454"
]
for contact in contacts:
    n_contact = "+92***-***" + contact[10:]
    print(n_contact)

# Answer # 6
transactions = [ "23000PKRS", "360000PKRS","80500PKRS", "9700PKRS", "95000PKRS"]
for transaction in transactions:
    transaction_n = int(transaction.replace("PKRS", ""))
    if transaction_n >= 50000:
        print(transaction_n)

# Answer # 7
sentence = "My name is Syed Imad Ali"
words = sentence.split()
reversed_words = words[::-1]
for word in reversed_words:
    print(word)

# Answer # 8
shop_cart = [
    {"item": "Shirt", "Quant": 2},
    {"item": "Plate", "Quant": 5},
    {"item": "Trousers", "Quant": 0},
    {"item": "Glass", "Quant": 4},
    {"item": "Cups", "Quant": 0},
    {"item": "Clippers", "Quant": 7}
]

for cart in shop_cart:
    if cart["Quant"] == 0:
        print("Out of Stock")
    else:
        print("Available")

# Answer # 9
to_do_li = [
    {"task": "Homework", "status": "pending"},
    {"task": "Cleaning", "status": "done"},
    {"task": "Sorting", "status": "done"},
    {"task": "Study", "status": "pending"},
    {"task": "Iron Clothes", "status": "pending"}
]
for remain_li in to_do_li:
    if remain_li["status"] == "pending":
        print(f"Remaining Tasks:-\n{remain_li["task"]}")
    
# Answer # 10
notifications = [
    "New message from Friend",
    "'xyz' liked your post",
    "System update available",
    "New follower: ABC",
    "Event reminder: Meeting at 5 PM",
    "Friend request from Friend-3",
    "New comment on your photo"
]

for i in range(min(5, len(notifications))):
    print(notifications[i])


# SECTION B: WHILE LOOP
#Answer # 13
correct_password = "secure123"

password = input("Enter password: ")
while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter password: ")

print("Access granted!")

# Answer # 14
correct_pin = "secure123"
attempts = 0
max_attempts = 3

pin = input("Enter PIN: ")
while pin != correct_pin and attempts < max_attempts:
    attempts += 1
    print(f"Incorrect PIN. {max_attempts - attempts} attempts left.")
    if attempts < max_attempts:
        pin = input("Enter PIN: ")
    else:
        print("Too many attempts. Access denied.")
        break

if pin == correct_pin:
    print("PIN accepted! Access granted.")

# Answer # 15
import time

percent = 0
while percent <= 100:
    filled = int(percent / 10)
    empty = 10 - filled
    bar = '[' + '#' * filled + ' ' * empty + ']'
    print(f'{bar} {percent}%', end='\r')
    time.sleep(0.1)  
    percent += 1  

print("Download Completed")

# Answer # 16
marks = []

while True:
    user_input = input("Enter a student's mark (or 'done' to finish): ").lower()
    
    if user_input == "done":
        break
    
    try:
        mark = float(user_input)
        marks.append(mark) 
    except ValueError:
        print("Invalid input! Please enter a number or 'done'.")

print("Collected marks:", marks)

# Answer # 17
import time
import random  

def check_internet():
    return random.choice([True, False])  


connected = check_internet()

while not connected:
    print("No internet connection. Retrying in 1 seconds...")
    time.sleep(1)  
    connected = check_internet()  

print("Internet connection established!")

# Answer # 18
while True:
   
    user_input = input("You: ").lower()
    
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    
    if user_input == "hi" or user_input == "hello":
        print("Chatbot: Hey there! How can I help you?")
    elif user_input == "help":
        print("Chatbot: I'm a simple chatbot. Say 'hi', 'help', or 'bye' to exit.")
    else:
        print("Chatbot: Hmm, I don't understand that. Try 'hi', 'help', or 'bye'.")


# Answer # 19
import time

while True:  # Comment this line to access the code 
    print("Red Light - Stop!")
    time.sleep(5)
    
    print("Green Light - Go!")
    time.sleep(4)
    
    print("Yellow Light - Caution!")
    time.sleep(2)

# Answer # 20
import time

base_fare = 80.00  
rate_per_km = 50.00  
distance = 0.0  
speed_km_per_sec = 0.1  

print("Taxi meter started. Press Ctrl+C to stop.")
try:
    while True:
        fare = base_fare + (distance * rate_per_km)
        print(f"Distance: {distance:.1f} km, Fare: Rs{fare:.2f}", end='\r')
        
        distance += speed_km_per_sec
        
        time.sleep(2)
except KeyboardInterrupt:
    print("\nTaxi meter stopped.")
    fare = base_fare + (distance * rate_per_km)
    print(f"Final Distance: {distance:.1f} km, Final Fare: Rs{fare:.2f}")

# SECTION "C"
# Answer # 23
rows = ['A', 'B', 'C']
seats = [1,2,3,4,5]

hall_seats=[]

for row in rows:
    for seat in seats:
        hall_seats = row + str(seat)
        print(hall_seats)
        

# Answer # 24
shirts = ["White shirt", "White shirt", "Linen white shirt "]
pants = ["black pants", "navy blue pants","charcoal grey pants"]

for shirt in shirts:
    for pant in pants:
        print(f"{shirt} shirt with {pant}")

# Answer # 25
for minute in range(11):  
    print(f"12:{minute:02d}")

# Answer # 26
days = [1, 2, 3]
slots = ["Morning", "Evening"]

for day in days:
    for slot in slots:
        print(f"Day {day} {slot}")


# Answer # 27
rows = [1,2,3]
seats = ["A", "B", "C", "D"]

for row in rows:
    for seat in seats:
         print(f"Row {row} Seat {seat}")

# Answer # 28
for row in range(3):
    print("   |   |  ")
    if row < 2:
        print("-----------")

# Answer # 29
rows = 5

for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (2 * i + 1))

# Answer # 30
players = ["Alice", "Bob", "Charlie"]

for i in range(len(players)):
    for j in range(i + 1, len(players)):
        print(f"Team: {players[i]} and {players[j]}")


# Answer # 31
for number in range(2, 6): 
    print(f"Multiplication Table for {number}:")
    for multiplier in range(1, 11):  
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
    print()  

# Answer # 32
shopping = {
    "Fruits": ["Apple", "Banana"],
    "Vegetables": ["Carrot", "Potato"],
    "Dairy": ["Milk", "Cheese"]
}

for category, products in shopping.items():
    print(f"Category: {category}")
    for product in products:
        print(f"- {product}")
    print()  


# SECTION "D"
# Answer # 35
def count_pdf_files(file_list):
    count = 0
    for file in file_list:
        if file.endswith('.pdf'):
            count += 1
    return count

files = ['document1.pdf', 'image.jpg', 'report.pdf', 'data.txt', 'summary.pdf']

result = count_pdf_files(files)
print(result)  


# Answer # 36
def is_username_available(username, taken_usernames):
    if username in taken_usernames:
        return False
    else:
        return True
    
taken_usernames = ['alice', 'bob', 'john123', 'sarah']

print(is_username_available('john123', taken_usernames))  
print(is_username_available('mike', taken_usernames))    


# Answer # 37
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


sentence = "I love programming in Python"
print(longest_word(sentence))  

sentence = "Hello world"
print(longest_word(sentence))  

sentence = "My name is Syed Imad"
print(longest_word(sentence)) 

# Answer # 38
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    for i in range(len(text) // 2):
        if text[i] != text[-(i + 1)]:
            return False
    return True

print(is_palindrome("radar"))      
print(is_palindrome("hello"))      
print(is_palindrome("Race car"))   
print(is_palindrome("A man a plan a canal Panama"))  

# Answer # 39
def print_multiplication_table(number, up_to=10):
    print(f"Multiplication Table for {number}:")
    for i in range(1, up_to + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

print_multiplication_table(5)      

# Answer # 40
import random

def roll_until_six():
    rolls = 0
    while True:
        result = random.randint(1, 6)
        rolls += 1
        print(f"Roll {rolls}: {result}")
        if result == 6:
            print(f"Got a 6 after {rolls} rolls!")
            return rolls
        
roll_until_six()


# Answer # 41
def filter_products(products, max_price):
    filtered_products = []
    for product in products:
        if product["price"] < max_price:
            filtered_products.append(product)
    return filtered_products

products = [
    {"name": "Gaming accessories", "price": 15000},
    {"name": "Laptop", "price": 50000},
    {"name": "Computer", "price": 40000},
    {"name": "Phone", "price": 25000}
]

result = filter_products(products, 35000)
print(result)  

# Answer # 42
def mask_passwords(passwords):
    masked_list = []
    for password in passwords:
        masked = "*" * len(password)
        masked_list.append(masked)
    return masked_list

passwords = ["secret", "password123", "abc"]
result = mask_passwords(passwords)
print(result)  

passwords = ["hello", "", "test123"]
result = mask_passwords(passwords)
print(result)  


# Answer # 43
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

sentence = "The cat, the dog, and the cat!"
result = word_frequency(sentence)
print(result)  

sentence = "Hello... hello, world!!"
result = word_frequency(sentence)
print(result)  


# Answer # 44
def extract_hashtags(post):
    words = post.split()
    hashtags = []
    for word in words:
        if word.startswith('#'):
            hashtags.append(word)
    return hashtags

post = "I love #coding and #python on #socialmedia"
result = extract_hashtags(post)
print(result)  

post = "No hashtags here"
result = extract_hashtags(post)
print(result)  

post = "#Fun #2025 Let's go #coding!"
result = extract_hashtags(post)
print(result)  

# SECTION E
# Answer # 47
def print_above_average_salaries(employees):
    if not employees:
        print("No employees provided.")
        return
    
    total = 0
    count = 0
    for emp in employees:
        if "salary" in emp and isinstance(emp["salary"], (int, float)) and emp["salary"] >= 0:
            total += emp["salary"]
            count += 1
    
    if count == 0:
        print("No valid salaries found.")
        return
    
    average = total / count
    above_average = [
        emp for emp in employees
        if "salary" in emp and isinstance(emp["salary"], (int, float)) and emp["salary"] > average
    ]
    above_average.sort(key=lambda x: x["salary"], reverse=True)
    
    print(f"Average salary: {average:.2f}")
    print("Employees with salaries above average:")
    for emp in above_average:
        name = emp.get("name", "Unknown")
        print(f"{name}: Rs{emp['salary']:,.2f}")


employees = [
    {"name": "Ali", "salary": 50000},
    {"name": "Asad", "salary": 60000},
    {"name": "Bilal", "salary": 45000},
    {"name": "Danish", "salary": 80000},
    {"name": "Emad", "salary": "invalid"}  
]
print_above_average_salaries(employees)

# Answer # 48
def print_pass_fail(grades, passing_grade=60):
    if not grades:
        print("No grades provided.")
        return
    
    print("Student grades results:")
    for i, grade in enumerate(grades, 1):
        if isinstance(grade, (int, float)) and grade >= 0:
            result = "Pass" if grade >= passing_grade else "Fail"
            print(f"Student {i}: {grade} - {result}")
        else:
            print(f"Student {i}: Invalid grade")


grades = [85, 55, 90, 62, 45, "invalid", 75]
print_pass_fail(grades)

# Answer # 49
def remove_duplicates(input_list):
    result = []
    for item in input_list:
        if item not in result:
            result.append(item)
    return result


numbers = [1, 2, 2, 3, 1, 4, 3]
print(remove_duplicates(numbers))  

words = ["apple", "banana", "apple", "cherry", "banana"]
print(remove_duplicates(words)) 

mixed = [1, "hello", 1, "hello", 2]
print(remove_duplicates(mixed))  


# Answer # 50
def flatten_list(nested_list):
    result = []
    stack = [nested_list]  
    
    while stack:
        current = stack.pop() 
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            result.append(current)
    
    return result

nested_list = [1, [2, 3], 4]
print(flatten_list(nested_list))  

nested_list = [1, [2, [3, 4], 5], [6]]
print(flatten_list(nested_list))  

nested_list = [[1, [2]], [[3, 4], 5], [], 6]
print(flatten_list(nested_list))  

nested_list = []
print(flatten_list(nested_list))  

# Answer # 51
while True:
    email = input("Please enter your email address: ")
    if "@" in email:
        print("Valid email! You entered:", email)
        break
    else:
        print("Invalid email! It must contain an '@' symbol. Try again.")


# Answer # 52
# Cannot be Answered at the Moment

# Answer # 53
contacts = [
    ("Ali", "+923001234567"),
    ("Sara", "+971501234567"),
    ("Ahmed", "+923331234567"),
    ("Emma", "+12025550123"),
    ("Zain", "+923451234567")
]

print("Pakistani Contacts:")
for name, phone in contacts:
    if phone.startswith("+92"):
        print(f"Name: {name}, Phone: {phone}")

# Answer # 54
# Cannot be Answered at the Moment

# Answer # 55
doctor_profiles = [
    {"name": "Dr. Sahira", "type": "general"},
    {"name": "Dr. Jameel", "type": "specialist"},
    {"name": "Dr. Laraib", "type": "specialist"},
    {"name": "Dr. Baseer", "type": "general"},
]

for doctor in doctor_profiles:
    if doctor["type"] == "specialist":
        print(doctor)

# Answer # 56
students = {
    "Imad": ["Math", "English", "Biology"],
    "Sameer": ["Physics", "Chemistry"],
    "Husain": ["Islamiat", "Math"]
}

for student, courses in students.items():
    print(f"{student} is enrolled in:")
    for course in courses:
        print(f"  - {course}")
    print()  


# SECTION F 
# Answer # 59
def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:  
            result += char
    return result

text = "My name is Syed Imad Ali Hashmi"
print(remove_duplicates(text))


# Answer # 60
def first_non_repeated(s):
    for char in s:
        if s.count(char) == 1:  
            return char
    return None  

text = "My name is Syed Imad Ali Hashmi"
print(first_non_repeated(text))


# Answer # 61
def rotate_left(s):
    if len(s) <= 1:
        return s
    return s[1:] + s[0]

text = "abc"
print(rotate_left(text))

# Answer # 62
# Not possible at the Moment

# Answer # 63
def reverse_words(sentence):
    words = sentence.split()      
    result = []
    
    for word in words:
        rev = ""
        for ch in word:
            rev = ch + rev         
        result.append(rev)
    
    return " ".join(result)

text = "hello world"
print(reverse_words(text))

# Answer # 64
def count_case(s):
    upper = 0
    lower = 0
    
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    
    return upper, lower

text = "Hello World"
u, l = count_case(text)
print("Uppercase:", u)
print("Lowercase:", l)

# Answer # 65
def validate_password(pwd):
    if len(pwd) < 8:
        return False
    
    has_digit = False
    for ch in pwd:
        if ch.isdigit():
            has_digit = True
            break
    
    return has_digit

print(validate_password("pass123"))     
print(validate_password("password1"))   

# Answer # 66
def find_duplicate_words(paragraph):
    words = paragraph.lower().split()  
    duplicates = []
    
    for word in words:
        if words.count(word) > 1 and word not in duplicates:
            duplicates.append(word)
    
    return duplicates

text = "This is a test. This test is simple."
print(find_duplicate_words(text))

# Answer # 67
def count_vowels(s):
    vowels = "aeiou"
    freq = {v: 0 for v in vowels}   
    
    for ch in s.lower():
        if ch in vowels:
            freq[ch] += 1
    
    return freq

text = "My name is Syed Imad Ali"
print(count_vowels(text))

# Answer # 68
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))   
print(are_anagrams("hello", "world"))     
