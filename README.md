# Personal Expense Tracker

A small Python command-line application for recording expenses and understanding where money goes. Built as a beginner software engineering project with readable code, CSV storage, and automated tests.

## Overview

The tracker lets users add an expense, view all recorded expenses, see their total spending, and view totals grouped by category. Expenses can be saved to a CSV file and loaded the next time the program starts.

**Why this project?** It provides practice with the building blocks of software development: functions, loops, conditionals, lists, dictionaries, file I/O, basic input validation, and testing. It deliberately avoids external dependencies and complicated frameworks.

## Features

- Add an expense with a description, amount, and category
- View expenses in a numbered list
- Calculate total spending
- Summarize spending by category (case-insensitive)
- Save expenses to `expenses.csv` and load them on startup
- Reject missing descriptions/categories and invalid or non-positive amounts
- Run automated tests for calculations and CSV storage

## Technology

- **Language:** Python
- **Storage:** CSV (Python standard library)
- **Testing:** `unittest` (Python standard library)
- **Dependencies:** None outside Python

## Getting started

1. Install Python 3 and VS Code.
2. Download or clone this repository, then open the project folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Run:

   ```bash
   python3 main.py
   ```

   On Windows, you may need to use `python main.py` instead.

5. Choose a menu option. The application creates `expenses.csv` when you save or exit successfully.

## Example

```text
===== PERSONAL EXPENSE TRACKER =====
1. Add expense
2. View expenses
3. View total spending
4. View spending by category
5. Save expenses
6. Exit
Choose an option (1-6): 1
Description: Coffee
Amount ($): 4.50
Category: Food
Expense added!

Choose an option (1-6): 3
Total spent: $4.50
```

For example data, see [`sample_expenses.csv`](sample_expenses.csv). The app uses `expenses.csv` for your own records. Your real records are intentionally excluded from Git through `.gitignore`.

## Project structure

```text
personal-expense-tracker/
├── main.py                 # Menu, expense functions, and CSV operations
├── sample_expenses.csv     # Fake sample data
├── tests/
│   └── test_main.py        # Automated tests
├── .gitignore              # Excludes local data and generated files
└── README.md               # Project documentation
```

## Testing

From the project directory, run:

```bash
python3 -m unittest discover -s tests -v
```

The tests cover total calculations, category totals, saving/loading CSV data, and behavior when a CSV file does not exist. You should also manually test the menu and invalid inputs.

## Design decisions

| Choice | Reason |
| --- | --- |
| One `main.py` file | Keeps the project approachable for new Python learners |
| List of dictionaries | Easy to understand and iterate over; each dictionary represents one expense |
| CSV file | Saves data between runs without requiring a database |
| Separate functions | Each function has one clear job and can be tested individually |
| Standard-library tests | Makes it easy to verify behavior without installing packages |

## Limitations and next steps

This project is intended for learning, not production accounting. It stores amounts as Python `float` values, which can have rounding limitations. For money-sensitive use, a future version should store integer cents or use `decimal.Decimal`. The save operation also rewrites the CSV file; more robust applications would use safer, atomic writes.

Potential improvements:

- Delete or edit an existing expense
- Filter expenses by category
- Add dates and monthly summaries
- Use `Decimal` for exact monetary calculations
- Add tests for the interactive menu and invalid input handling

## What I learned

This project is a useful way to practice breaking a problem into small functions, organizing expenses with dictionaries, processing lists, reading and writing CSV data, and checking results with automated tests.

> **For your portfolio:** Personalize this section after you've run the application, explained the code in your own words, and made a change yourself. Be transparent about any AI or tutorial assistance if asked.

## License

For personal learning and portfolio demonstration. No open-source license has been selected.
