# Some additional mini projects


1. **Palindrome Checker:**

   **Description:** Create a program that checks whether a given word or phrase is a palindrome, meaning it reads the same forwards and backwards (ignoring spaces and punctuation).

   **Solution:**
   ```python
   def is_palindrome(text):
       cleaned_text = "".join(char.lower() for char in text if char.isalnum())
       reversed_text = cleaned_text[::-1]
       return cleaned_text == reversed_text

   # Example usage
   word = "Madam"
   is_word_palindrome = is_palindrome(word)
   print(f"Is '{word}' a palindrome? {is_word_palindrome}")
   ```

2. **Contact Book:**

   **Description:** Develop a contact book program that allows the user to add, view, update, and delete contacts. Store the contacts in a dictionary or a file.

   **Solution:**
   ```python
   def add_contact(contact_book, name, phone):
       contact_book[name] = phone

   def view_contact(contact_book, name):
       if name in contact_book:
           phone = contact_book[name]
           print(f"Contact: {name} - Phone: {phone}")
       else:
           print("Contact not found.")

   def update_contact(contact_book, name, phone):
       if name in contact_book:
           contact_book[name] = phone
           print(f"Contact '{name}' updated successfully.")
       else:
           print("Contact not found.")

   def delete_contact(contact_book, name):
       if name in contact_book:
           del contact_book[name]
           print(f"Contact '{name}' deleted successfully.")
       else:
           print("Contact not found.")

   # Example usage
   contacts = {}
   add_contact(contacts, "John", "1234567890")
   view_contact(contacts, "John")
   update_contact(contacts, "John", "9876543210")
   delete_contact(contacts, "John")
   ```

3. **Number Guessing Game:**

   **Description:** Create a number guessing game where the computer generates a random number and the player tries to guess it. Provide feedback to the player if their guess is too high or too low. Track the number of attempts and display the final score.

   **Solution:**
   ```python
   import random

   def number_guessing_game():
       target_number = random.randint(1, 100)
       attempts = 0

       while True:
           guess = int(input("Guess a number between 1 and 100: "))
           attempts += 1

           if guess == target_number:
               print("Congratulations! You guessed the number correctly.")
               break
           elif guess < target_number:
               print("Too low! Guess higher.")
           else:
               print("Too high! Guess lower.")

       print("Number of attempts:", attempts)

   # Example usage
   number_guessing_game()
   ```

4. **Currency Converter:**

   **Description:** Develop a currency converter program that converts an amount from one currency to another. Use real-time exchange rates or predefined conversion rates.

   **Solution:**
   ```python
   def convert_currency(amount, exchange_rate):
       converted_amount = amount * exchange_rate
       return converted_amount

   # Example usage
   amount_in_usd = 100
   usd_to_eur_rate = 0.85
   converted_amount = convert_currency(amount_in_usd, usd_to_eur_rate)
   print(f"{amount_in_usd} USD is equal to {converted_amount} EUR.")
   ```

5. **Hangman Game:**

   **Description:** Create a hangman game where the player tries

 to guess a hidden word by suggesting letters. Display the number of attempts remaining and reveal the correct letters when guessed correctly.

   **Solution:**
   ```python
   def hangman_game(word):
       hidden_word = "_" * len(word)
       attempts = 6

       while attempts > 0:
           print(f"\nHidden Word: {hidden_word}")
           print(f"Attempts Remaining: {attempts}")

           guess = input("Guess a letter: ").lower()

           if guess in word:
               updated_word = ""
               for i in range(len(word)):
                   if word[i] == guess:
                       updated_word += guess
                   else:
                       updated_word += hidden_word[i]
               hidden_word = updated_word
           else:
               attempts -= 1

           if hidden_word == word:
               print("Congratulations! You guessed the word correctly.")
               break

       if attempts == 0:
           print("Game Over! You ran out of attempts.")
           print("The word was:", word)

   # Example usage
   secret_word = "python"
   hangman_game(secret_word)
   ```

These additional mini projects will provide you with more opportunities to practice Python programming concepts and strengthen your skills. Have fun exploring and enhancing these projects according to your preferences!

---
---
---

# Here are more mini projects


1. **Random Password Generator:**

   **Description:** Create a program that generates a random password of a specified length. The password should include a combination of uppercase letters, lowercase letters, numbers, and symbols.

   **Solution:**
   ```python
   import random
   import string

   def generate_password(length):
       characters = string.ascii_letters + string.digits + string.punctuation
       password = ''.join(random.choice(characters) for _ in range(length))
       return password

   # Example usage
   password = generate_password(10)
   print("Generated Password:", password)
   ```

2. **Dice Rolling Simulator:**

   **Description:** Develop a program that simulates rolling dice. Allow the user to specify the number of dice and the number of sides on each die. Display the results of each roll.

   **Solution:**
   ```python
   import random

   def roll_dice(num_dice, num_sides):
       rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
       return rolls

   # Example usage
   num_dice = 2
   num_sides = 6
   dice_rolls = roll_dice(num_dice, num_sides)
   print("Dice Rolls:", dice_rolls)
   ```

3. **File Organizer:**

   **Description:** Create a program that organizes files in a directory by moving them into subdirectories based on their file extension.

   **Solution:**
   ```python
   import os
   import shutil

   def organize_files(directory):
       for file in os.listdir(directory):
           if os.path.isfile(os.path.join(directory, file)):
               extension = os.path.splitext(file)[1][1:]
               if extension:
                   if not os.path.exists(os.path.join(directory, extension)):
                       os.makedirs(os.path.join(directory, extension))
                   shutil.move(os.path.join(directory, file), os.path.join(directory, extension, file))

   # Example usage
   target_directory = "files"
   organize_files(target_directory)
   ```

4. **URL Shortener:**

   **Description:** Develop a program that shortens long URLs into shorter, more manageable URLs. Store the original and shortened URLs in a database or file.

   **Solution:**
   ```python
   import random
   import string

   class URLShortener:
       def __init__(self):
           self.url_mapping = {}

       def shorten_url(self, original_url):
           characters = string.ascii_letters + string.digits
           short_url = ''.join(random.choice(characters) for _ in range(6))
           self.url_mapping[short_url] = original_url
           return short_url

       def retrieve_url(self, short_url):
           return self.url_mapping.get(short_url, None)

   # Example usage
   shortener = URLShortener()
   original_url = "https://example.com/very-long-url"
   shortened_url = shortener.shorten_url(original_url)
   print("Shortened URL:", shortened_url)
   retrieved_url = shortener.retrieve_url(shortened_url)
   print("Retrieved URL:", retrieved_url)
   ```

5. **Text-Based Adventure Game:**

   **Description:** Create a text-based adventure game where the player navigates through a series of rooms, interacts with objects, and makes decisions that affect the outcome of the game.

   **Solution:**
   ```python
   def adventure_game():
       current_room = "start"

       while True:
           if current_room == "start":
               print("You are in a dark room. There are two doors in front of you.")
               print("What do you do?")
               choice = input

("1. Go through door A\n2. Go through door B\n")

               if choice == "1":
                   current_room = "room A"
               elif choice == "2":
                   current_room = "room B"
               else:
                   print("Invalid choice. Try again.")

           elif current_room == "room A":
               print("You are in room A. There is a key on the table.")
               print("What do you do?")
               choice = input("1. Take the key\n2. Go back to the starting room\n")

               if choice == "1":
                   print("You took the key.")
                   # Do something with the key
                   current_room = "start"
               elif choice == "2":
                   current_room = "start"
               else:
                   print("Invalid choice. Try again.")

           elif current_room == "room B":
               print("You are in room B. There is a locked chest.")
               print("What do you do?")
               choice = input("1. Try to open the chest\n2. Go back to the starting room\n")

               if choice == "1":
                   # Check if the player has the key to open the chest
                   if has_key:
                       print("You opened the chest and found a treasure!")
                       # Do something with the treasure
                       current_room = "start"
                   else:
                       print("The chest is locked. You need a key to open it.")
               elif choice == "2":
                   current_room = "start"
               else:
                   print("Invalid choice. Try again.")

           else:
               print("Unknown room. The game will exit.")
               break

   # Example usage
   adventure_game()
   ```

6. **Tic-Tac-Toe Game:**

   **Description:** Create a program that allows two players to play the game of Tic-Tac-Toe. Display the board, accept player moves, and determine the winner.

   **Solution:**
   ```python
   def display_board(board):
       for row in board:
           print(" | ".join(row))
           print("-" * 9)

   def check_winner(board, player):
       for row in board:
           if all(cell == player for cell in row):
               return True

       for column in range(3):
           if all(board[row][column] == player for row in range(3)):
               return True

       if all(board[i][i] == player for i in range(3)):
           return True

       if all(board[i][2 - i] == player for i in range(3)):
           return True

       return False

   def tic_tac_toe():
       board = [[" ", " ", " "] for _ in range(3)]
       current_player = "X"
       moves = 0

       while True:
           display_board(board)

           row = int(input("Enter the row (0-2): "))
           column = int(input("Enter the column (0-2): "))

           if board[row][column] == " ":
               board[row][column] = current_player
               moves += 1

               if check_winner(board, current_player):
                   print(f"Player {current_player} wins!")
                   break
               elif moves == 9:
                   print("It's a tie!")
                   break

               current_player = "O" if current_player == "X" else "X"
           else:
               print("Invalid move. Try again.")

   # Example usage
   tic_tac_toe()
   ```

7. **To-Do List Manager:**

   **Description:** Develop a program that allows the user to manage a to-do list. Implement functionality to add tasks, mark tasks as complete,

 and remove tasks.

   **Solution:**
   ```python
   class ToDoList:
       def __init__(self):
           self.tasks = []

       def add_task(self, task):
           self.tasks.append(task)
           print(f"Task '{task}' added.")

       def complete_task(self, task):
           if task in self.tasks:
               self.tasks.remove(task)
               print(f"Task '{task}' marked as complete.")
           else:
               print(f"Task '{task}' not found in the to-do list.")

       def remove_task(self, task):
           if task in self.tasks:
               self.tasks.remove(task)
               print(f"Task '{task}' removed.")
           else:
               print(f"Task '{task}' not found in the to-do list.")

       def display_tasks(self):
           if self.tasks:
               print("To-Do List:")
               for index, task in enumerate(self.tasks, start=1):
                   print(f"{index}. {task}")
           else:
               print("To-Do List is empty.")

   # Example usage
   todo_list = ToDoList()
   todo_list.add_task("Complete assignment")
   todo_list.add_task("Buy groceries")
   todo_list.display_tasks()
   todo_list.complete_task("Buy groceries")
   todo_list.display_tasks()
   todo_list.remove_task("Complete assignment")
   todo_list.display_tasks()
   ```

8. **Web Scraper:**

   **Description:** Create a program that scrapes data from a website. Use libraries like BeautifulSoup and requests to retrieve specific information from web pages.

   **Solution:**
   ```python
   import requests
   from bs4 import BeautifulSoup

   def scrape_website(url):
       response = requests.get(url)
       if response.status_code == 200:
           soup = BeautifulSoup(response.text, 'html.parser')
           # Scrape data from the webpage
           # ...

   # Example usage
   website_url = "https://example.com"
   scrape_website(website_url)
   ```

9. **Quiz Game:**

   **Description:** Develop a program that presents a series of questions to the user and keeps track of their score. Display the final score at the end of the quiz.

   **Solution:**
   ```python
   def quiz_game(questions):
       score = 0
       total_questions = len(questions)

       for index, question in enumerate(questions, start=1):
           print(f"Question {index}: {question['question']}")
           for option in question['options']:
               print(f"- {option}")
           answer = input("Enter your answer: ")
           if answer.lower() == question['answer'].lower():
               print("Correct!")
               score += 1
           else:
               print("Incorrect!")

       print("Quiz completed!")
       print(f"Your score: {score}/{total_questions}")

   # Example usage
   quiz_questions = [
       {
           'question': 'What is the capital of France?',
           'options': ['A. London', 'B. Paris', 'C. Madrid', 'D. Rome'],
           'answer': 'B'
       },
       {
           'question': 'Which planet is known as the Red Planet?',
           'options': ['A. Mars', 'B. Jupiter', 'C. Venus', 'D. Saturn'],
           'answer': 'A'
       },
       # Add more questions...
   ]
   quiz_game(quiz_questions)
   ```

10. **Currency Converter:**

    **Description:** Create a program that converts currency from one denomination to another using real-time exchange rates. Fetch exchange rate data from a reliable API.

    **Solution:**
    ```python
    import requests

    def currency_converter(amount, base_currency, target_currency):
       

 url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        
        if response.status_code == 200:
            rates = response.json()['rates']
            if target_currency in rates:
                conversion_rate = rates[target_currency]
                converted_amount = amount * conversion_rate
                return converted_amount
            else:
                print(f"Exchange rate for {target_currency} not found.")
        else:
            print("Failed to fetch exchange rates.")

    # Example usage
    amount = 100
    base_currency = "USD"
    target_currency = "EUR"
    converted_amount = currency_converter(amount, base_currency, target_currency)
    print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")
    ```

Feel free to modify and expand on these project ideas to further enhance your learning experience as a Python beginner. Enjoy coding!

---
---
---
## Here are some additional sources where you can find more free mini projects for Python:

1. PyBites - PyBites offers a collection of Python coding exercises, challenges, and mini-projects to enhance your Python skills. You can check out their "Code Challenges" section: [PyBites Code Challenges](https://codechalleng.es/)

2. Codewars - Codewars is a platform that provides coding challenges in various programming languages, including Python. You can solve challenges and compare your solutions with others: [Codewars Python](https://www.codewars.com/kata/search/python?q=&beta=false)

3. Reddit - The Python community on Reddit offers a wealth of resources, including mini project ideas and discussions. You can explore the r/learnpython and r/Python subreddits for project inspiration: [r/learnpython](https://www.reddit.com/r/learnpython/) and [r/Python](https://www.reddit.com/r/Python/)

4. Awesome Python - Awesome Python is a curated list of Python frameworks, libraries, and software. It includes a section dedicated to projects that you can explore for inspiration: [Awesome Python Projects](https://github.com/vinta/awesome-python#readme)

5. FreeCodeCamp - FreeCodeCamp offers a wide range of coding tutorials and resources, including Python projects. You can browse their "Python Projects" section for ideas and step-by-step guides: [FreeCodeCamp Python Projects](https://www.freecodecamp.org/learn/scientific-computing-with-python/#python-projects)

Remember to always check the licensing and usage terms for the projects you find and ensure that they align with your requirements.

---
---
---
## Some advance topics

1. Image Recognition:
   - Solution: [Image Recognition Solution](https://github.com/example-user/image-recognition-project)
   - Description: The solution includes code that uses pre-trained models like ResNet or VGG to perform image recognition on a given image dataset. It demonstrates how to load the model, preprocess the images, and make predictions.

2. Chatbot:
   - Solution: [Chatbot Solution](https://github.com/example-user/chatbot-project)
   - Description: The solution includes code for building a chatbot using natural language processing techniques. It shows how to define rules or use machine learning algorithms to generate responses based on user input.

3. Data Analysis Dashboard:
   - Solution: [Data Analysis Dashboard Solution](https://github.com/example-user/data-analysis-dashboard)
   - Description: The solution includes code and visualization templates for creating a data analysis dashboard. It demonstrates how to load and analyze a dataset using Pandas, and generate interactive visualizations using libraries like Matplotlib and Plotly.

4. Stock Market Analysis:
   - Solution: [Stock Market Analysis Solution](https://github.com/example-user/stock-market-analysis)
   - Description: The solution includes code that fetches stock market data from an API, performs data analysis, and generates insights or trading signals. It showcases techniques for calculating moving averages, plotting trends, and making investment decisions.

5. Web Scraping and Automation:
   - Solution: [Web Scraping and Automation Solution](https://github.com/example-user/web-scraping-automation)
   - Description: The solution includes code for web scraping and automation tasks. It demonstrates how to use libraries like BeautifulSoup and Selenium to extract data from websites or automate repetitive tasks like form filling.

Please note that the provided solutions are placeholders and may not contain the complete implementation. You can explore these projects, customize them as per your requirements, and refer to the code as a starting point for your own implementation.