
import requests
import html

parameters = {
    "amount": 10,
    "type": "boolean"
}
res = requests.get("https://opentdb.com/api.php", params=parameters)

if res.status_code == requests.codes.ok:
    data = res.json()
    data = data["results"]
    question_data = [{"question": html.unescape(f"{ele["question"]}"), "correct_answer": ele["correct_answer"]} for ele in data]
