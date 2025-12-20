"""
Quizzler API Interface
Fetches True/False trivia questions from the Open Trivia Database (OTDB).
Includes data cleaning to handle HTML entities for proper display in the GUI.
"""

import requests
import html

# --- API Configuration ---
# 'amount': number of questions to retrieve
# 'type': 'boolean' ensures True/False format
parameters = {
    "amount": 10,
    "type": "boolean"
}

# --- Fetch Data ---
# GET request to the Open Trivia Database
res = requests.get("https://opentdb.com/api.php", params=parameters)

# Check if the HTTP request was successful (200 OK)
if res.status_code == requests.codes.ok:
    # Parse the JSON response into a Python dictionary
    raw_data = res.json()

    # Extract the 'results' list which contains the questions and answers
    quiz_results = raw_data["results"]

    # --- Data Processing ---
    # List comprehension to create a simplified list of dictionaries.
    # html.unescape() converts entities like &quot; into actual " characters.
    question_data = [
        {
            "question": html.unescape(ele["question"]),
            "correct_answer": ele["correct_answer"]
        }
        for ele in quiz_results
    ]

    print(f"Successfully loaded {len(question_data)} questions.")

else:
    print(f"Error fetching data. Status Code: {res.status_code}")