
def is_palindrome(Sentence: str) -> str:

    Sentence = Sentence.lower()
    
    left = 0
    right = len(Sentence) - 1


#  "..ade eda "
    while left < right:

        if not is_letter(Sentence[left]):
            left += 1
            continue

        if not is_letter(Sentence[right]):
            right -= 1
            continue

        if Sentence[left] != Sentence[right]:
            return "Not a palindrome"
        left += 1
        right -= 1

    return "Palindrome"


# QUESTION 1

def is_letter(ch) -> bool:
    return ("a" <= ch <= "z") or ("A" <= ch <= "Z")

def is_palindrome(text, left, right) -> str:
    
    # Base Case
    if left >= right:
        return "Palindrome"

    # Converting characters to lowercase for case-insensitivity
    char_left = text[left].lower()
    char_right = text[right].lower()

    # If the left character is not a letter we skip it by incrementing left pointer
    if not is_letter(char_left):
        return is_palindrome(text, left + 1, right)

    # If the right character is not a letter, skip it by decrementing right pointer
    if not is_letter(char_right):
        return is_palindrome(text, left, right - 1)

    # If both are letters but don't match, it is not a palindrome
    if char_left != char_right:
        return "Not a palindrome"

    # If they match, move both pointers inward recursively
    return is_palindrome(text, left + 1, right - 1)

# SENTENCE1= "Was it a car or a cat I saw?"
# SENTENCE2 = "Hello, World!"
# SENTENCE3 = "ref82er"
# print(is_palindrome(SENTENCE1, 0, len(SENTENCE1) - 1))
# print(is_palindrome(SENTENCE2, 0, len(SENTENCE2) - 1))
# print(is_palindrome(SENTENCE3, 0, len(SENTENCE3) - 1))


# Question 2


students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]},
    {"name": "Alex", "scores": [42, 45]},  # Added for extra testing
    {"name": "Chris", "scores": [30, 20]}, # Added for extra testing
]


# Manual average calculator
def calculate_average(scores) -> float:
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    return total / count if count > 0 else 0


# Pure function for grading logic
def grade_for(avg):
    if 70 <= avg <= 100:
        return "A"
    elif 60 <= avg < 70:
        return "B"
    elif 50 <= avg < 60:
        return "C"
    elif 45 <= avg < 50:
        return "D"
    elif 40 <= avg < 45:
        return "E"
    else:
        return "F"


# student processing
def process_student(student) -> tuple[str, float, str]:
    avg = calculate_average(student["scores"])
    grade = grade_for(avg)
    return (student["name"], avg, grade)

student_results = list(map(process_student, students))
print("All Student Results:")

for name, avg, grade in student_results:
    print(f"{name} → Average: {avg:.2f} → Grade: {grade}")


def holds_passing_grade(student_tuple) -> bool:
    # Grades A, B, or C pass according to constraints
    return student_tuple[2] in ["A", "B", "C"]


passing_students = list(filter(holds_passing_grade, student_results))

# print("\nPassing Students (A-C):")
# print(passing_students)


# Tracking the highest & lowest manually 

highest_student = None
lowest_student = None
highest_avg = -1  # Lower than lowest possible score
lowest_avg = 101  # Higher than highest possible score

for name, avg, grade in student_results:
    if avg > highest_avg:
        highest_avg = avg
        highest_student = (name, avg, grade)

    if avg < lowest_avg:
        lowest_avg = avg
        lowest_student = (name, avg, grade)

# print(
#     f"\nHighest Performing Student: {highest_student[0]} with {highest_student[1]:.2f}"
# )
# print(
#     f"Lowest Performing Student: {lowest_student[0]} with {lowest_student[1]:.2f}"
# )

# Replacing map with List Comprehension
student_results_comp = [
    (s["name"], calculate_average(s["scores"]), grade_for(calculate_average(s["scores"])))
    for s in students
]



# Problem 3
def count_words(words: list[str]) -> dict[str, int]:

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def most_frequent(freq: dict[str, int]) -> str:

    max_count = -1
    most_freq_word = None

    for word, count in freq.items():
        if count > max_count:
            max_count = count
            most_freq_word = word

    return most_freq_word


from functools import reduce

def most_frequent(freq: dict[str, int]) -> str:
    
    if not freq:
        return None
  
    most_freq_item = reduce(
        lambda acc, curr: curr if curr[1] > acc[1] else acc, freq.items()
    )

    return most_freq_item[0]




# sentence = input("Enter a sentence: ")
# words = sentence.split()

# words = [word.strip(",.!?;:\"'()[]{}") for word in words]  # Removing punctuation from each word

# word_freq = count_words(words)
# most_freq_word = most_frequent(word_freq)
# print(f"Most frequent word is: '{most_freq_word}' ({word_freq[most_freq_word]})")



# Quesrion 4

def twoSum(nums, targ)-> list[int]:
    seen = {}

    for i in range(len(nums)):
    
        needed = targ - nums[i]
        if needed in seen:
            return [seen[needed], i]
        seen[nums[i]] = i

    return []




def twoSum1(nums: list[int], targ: int) -> list[int]:
    initial_state = ({}, [])

    # We need both the index and value, so we reduce over enumerate(nums)
    def reduce_two_sum(state, current_item):
        seen, result = state
        index, val = current_item

        if result:
            return (seen, result)

        needed = targ - val
        if needed in seen:
            return (seen, [seen[needed], index])

        seen[val] = index
        return (seen, [])

    _, final_result = reduce(reduce_two_sum, enumerate(nums), initial_state)
    return final_result


print(twoSum1([2, 7, 11, 15], 9))



# question 5

def step(largest, second_largest, x) -> tuple[int, int]:
    
    if x > largest:
        return (x, largest)
    elif x > second_largest:
        return (largest, x)
    else:
        return (largest, second_largest)


def second_largest(nums) -> int:
    if len(nums) < 2:
        raise ValueError("List must contain at least two elements")

    largest = second_largest = float('-inf')

    for n in nums:
        largest, second_largest = step(largest, second_largest, n)

    if second_largest == float('-inf'):
        raise ValueError("No second largest element found")

    return second_largest

# print(second_largest([10, 5, 8, 20, 15]))  # Output is 15



# question 6

def make_shifter(shift):

    def shifter(char):
        
        if not char.isalpha():
            return char

        start = ord("A") if char.isupper() else ord("a")
        index = ord(char) - start
        return chr((index + (shift)%26) % 26 + start)

    return shifter

def caesar_cipher(text, shift, mode):
    if mode == "decrypt":
        shift = -shift

    # Create the pure shifter function
    char_shifter = make_shifter(shift)

    # map() returns an iterator of characters, so we join them back into a string
    return "".join(map(char_shifter, text))


# print(" Caesar Cipher System ")

# # Requirement: The program asks the user whether to encrypt or decrypt

# try:
#     mode = input("Would you like to (e)ncrypt or (d)ecrypt? ").strip().lower()
#     if mode in ["e", "encrypt"]:
#         mode = "encrypt"
#     elif mode in ["d", "decrypt"]:
#         mode = "decrypt"
#     else:
#         print("Invalid option selected. Exiting.")
#         exit()
#     message = input("Enter your message: ")
# except KeyboardInterrupt:
#     print("\nOperation cancelled by user.")
#     exit()

# try:
#     shift = int(input("Enter the shift amount (integer): "))
# except ValueError:
#     print("Shift must be an integer. Exiting.")

# # Process and print results
# result = caesar_cipher(message, shift, mode)
# print(f"\nResulting Text:")
# print(result)


# question 7

def strip(text: str) -> str:
    # Removing leading and trailing whitespace manually.
    start = 0
    end = len(text) - 1

    # Find first non-whitespace character
    while start <= end and text[start] == " ":
        start += 1

    # Find last non-whitespace character
    while end >= start and text[end] == " ":
        end -= 1
    
    return text[start : end + 1]


def lower(text: str) -> str:
    # Converts a string to lowercase manually.
    result = ""
    for char in text:
        # Check if character is an uppercase ASCII letter
        if "A" <= char <= "Z":
            result += chr(ord(char) + 32)
        else:
            result += char
    
    return result


def remove_vowels(text: str) -> str:
    # Removes vowels from a string manually.
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


def reverse(text: str) -> str:
    # Reverses a string using a manual loop (no [::-1] or .reverse()).
    result = ""
    for char in text:
        result = char + result  # Prepend each character to flip the order
    return result


# Functional Composition tools pipe and compose

def pipe(*funcs) -> callable:
    # Executes an arbitrary number of functions from left-to-right.
    def wrapper(x):
        result = x
        for func in funcs:
            result = func(result)
        return result
    return wrapper


def compose(*funcs) -> callable:
    # Executes an arbitrary number of functions from right-to-left.
    def wrapper(x):
        result = x
        # Loop through functions backward
        for i in range(len(funcs) - 1, -1, -1):
            result = funcs[i](result)
        return result
    return wrapper


def reverse(text: str) -> str:
    # Reverses a string using pure recursion (no loops, no [::-1], no .reverse()).
    # Base Case: An empty string or a single character is already reversed
    if len(text) <= 1:
        return text

    # Recursive Step: Take the last character and prepend it to the reversed remaining substring
    return text[-1] + reverse(text[:-1])



# Define the operational pipeline
pipeline = pipe(strip, lower, remove_vowels, reverse)
    
    # Run the initial input string through the engine
output = pipeline("  Hello World  ")
print(f"Pipeline Result: '{output}'")  # Output: 'dlrw hll'




# question 8

#  Pure Recursive Flattening with no loops
def flatten(nested):
    #  Flattens a list of any depth recursively without using loops.
    
    # Base Case 1: If it's not a list, wrap it in a list so it can be combined
    if not isinstance(nested, list):
        return [nested]
    
    # Base Case 2: An empty list flattens to an empty list
    if not nested:
        return []
    
    # Recursive Step: Flatten the first element, flatten the rest, and combine them
    return flatten(nested[0]) + flatten(nested[1:])


# Pure Higher-Order Group By (No external mutations)
def group_by(items, key_fn):
    
    # Groups items by a key function using a pure mapping approach.
    result = {}
    
    for item in items:
        # Determine the key using the higher-order parameter function
        key = key_fn(item)
        
        # Build the lists safely within our fresh local dictionary
        if key not in result:
            result[key] = []
        result[key].append(item)
        
    return result


# The Combined Pipeline Function
def combined(nested_list):
    # Flattens a deeply nested list of strings and groups them by their first letter.

    flat_words = flatten(nested_list)
    
    #  Extracting group mappings by feeding a lambda key function
    return group_by(flat_words, lambda w: w[0] if w else "")



    # Test 1: Simple Flattening
# print("Flatten Test:", flatten([1, [2, [3, [4]], 5]]))
# # Output: [1, 2, 3, 4, 5]

# # Test 2: Simple Grouping
# grouped = group_by(["apple", "avocado", "banana"], lambda w: w[0])
# print("Group_by Test:", grouped)
# # Output: {'a': ['apple', 'avocado'], 'b': ['banana']}

#     # Test 3: Combined Execution Example
# nested_dataset = [["apple", "avocado"], ["banana"], [["cherry"]]]
# print("Combined Test:", combined(nested_dataset))
# # Output: {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']}




# question 9

def memoize(func):
    # A pure decorator that caches results of a function based on its input arguments to avoid repeatring computation
    # The cache lives securely in the closure of the decorator — not as a global
    cache = {}

    def wrapper(*args):

        if args not in cache:
            # Evaluate the function only if the arguments haven't been seen yet
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fib(n):
    # Recursive Fibonacci function optimized with @memoize.
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# performance testing

import time

print("Calculating fib(35)...")
start_time = time.time()
    
result = fib(35)
    
end_time = time.time()
execution_time = end_time - start_time

print(f"Result: {result}")
print(f"Execution time: {execution_time:.6f} seconds")




