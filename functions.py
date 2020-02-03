"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

# Write your function here
def hometown(city):
    return city == "San Francisco"

print(hometown("San Francisco"))
print(hometown("Oakland"))

"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here
def full_name(first_name, last_name):
    """Takes first name and last name and returns a full name"""
    return f"{first_name} {last_name}"

print(full_name("John", "Wayne"))
print(full_name("Keith", "Urban"))

"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

# Write your function here
def greeting(first_name, last_name, hometown):
    if hometown == "San Francisco":
        return f"Hi {first_name} {last_name}, we're from the same place!"
    else:
        return f"Hi {first_name} {last_name}, I'd love to visit {hometown}!"

print(greeting("Keith", "Urban", "Georgia"))
print(greeting("John", "Wayne", "San Francisco"))
"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

# Write your function here
def berry_checker(fruit):
    """Returns True if a fruit is a berry"""
    berry_list = ["strawberry", "raspberry", "blackberry", "currant"]
    return fruit in berry_list

print(berry_checker("raspberry"))
print(berry_checker("orange"))

"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

# Write your function here
def ship_cost(fruit):
    berry_list = ["strawberry", "raspberry", "blackberry", "currant"]
    berry_cost = 0
    non_berry_cost = 5
    if fruit in berry_list:
        return berry_cost
    else:
        return non_berry_cost

print(ship_cost("raspberry"))
print(ship_cost("orange"))

"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# Write your function here
def total_cost(price, state, tax):
    """Returns total price after taxes and fees (float)

    Takes arguments:
    Base price (int)
    Two-letter state abbreviation (str)
    Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)"""
    if state == "CA":
        return price + (price * (tax + 0.03))
    elif state == "PA":
        return price + (price * tax) + 2.00
    elif state == "MA":
        if price <= 100.00:
            return price + (price * tax) + 1.00
        else:
            return price + (price * tax) + 3.00
    else:
        return price + (price * tax)

print(total_cost(5.00, "CA", 0.08))
print(total_cost(3.00, "PA", 0.05))
print(total_cost(7.00, "MA", 0.03))
print(total_cost(8.00, "NY", 0.04))

"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

# Write your function here
def elongate(my_list, arg1):
    my_list.append(arg1)
    return my_list

print(elongate(['a', 'b', 'c'], 'd'))

"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here
def word_mult(word):
    mult = word*3
    return (word, mult)

print(word_mult("bye"))
