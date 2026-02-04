
# ☕ OOP Coffee Machine
A robust, terminal-based coffee machine simulator built with Python using Object-Oriented Programming principles. This machine manages ingredients, processes varied coin inputs, calculates change, and tracks profits.

## 🛠 Features
**Resource Management:** Tracks water, milk, and coffee levels.

**Menu System:** Offers Espresso, Latte, and Cappuccino with specific ingredient requirements and pricing.

**Payment Processing:** Accepts Quarters, Dimes, Nickels, and Pennies.

**Error Handling:** Manages invalid inputs (non-numeric) without crashing the program.

**Reporting:** Real-time status updates on ingredients and total profit.

## 🏗 Project Structure
The project is split into two main files to maintain clean code and separation of concerns:

**coffee_machine.py:** Contains the logic for the four core classes:
  - MenuItem: Models each drink's name, cost, and recipe.
  - Menu: Manages the collection of available drinks.
  - CoffeeMaker: Handles the hardware logic (checking resources, brewing).
  - MoneyMachine: Handles the financial logic (payment, change, profit).

**main.py:** The entry point that runs the program loop.

## 🚀 How to Run
1. Ensure you have Python installed (Python 3.x recommended).

2. Clone or download the project files into a folder.

3. Run the program via your terminal or command prompt:

```Bash
cd Day16
python main.py
```

## 🎮 How to Use
Once the machine starts, you can interact with it using the following commands:

**Drink Names:** Type latte, espresso, or cappuccino to start an order.

**report:** Type this to see how much water, milk, and coffee is left, as well as total earnings.

**off:** Shuts down the machine and ends the program.

## 👌🏼 Example Interaction
<video width="640" height="360" controls>
<source src="coffee_machine.mp4" type="video/mp4">
Your browser does not support the video tag
</video>

## ⚙️ Logic Workflow
**Check Resources:** When a user selects a drink, the machine first checks if it has enough water, milk, and coffee.

**Process Payment:** If resources are sufficient, it prompts for coins. It calculates the total value and checks if it covers the drink cost.

**Calculate Change:** If the user overpays, the machine provides exact change.

**Brew:** Once paid, the machine deducts the ingredients from its internal storage and serves the coffee.

## 📝 License
This project is open-source and free to use for educational purposes.