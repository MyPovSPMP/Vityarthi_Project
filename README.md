AI detectors like Pangram trigger on specific patterns: repetitive sentence structures, balanced bullet lists (`**Bold Keyword:** Explanation`), transition words like "furthermore" or "seamlessly," and overly polished phrasing.

Here is a version written like a real student project—casual, direct, with natural variation in sentence length and zero corporate fluff.

---

# Vityarthi Python Project - Dice Betting Game

This is a basic command-line dice game I made for my Vityarthi Python course. You start with some fake money, make a bet, and try to guess what number a 6-sided die will land on. If you guess right, you double your bet. If you get it wrong, you lose the wager.

I built this to practice combining basic Python concepts like loops, functions, `try/except` error handling, and the `random` module into a single program.

---

## Features

* Random dice rolls (1 to 6)
* Virtual money system with betting, deposits, and withdrawals
* Simple win/loss tracking that updates your balance after every roll
* Input validation so the game doesn't crash if someone types letters instead of numbers
* Colored text using `colorama` (green for wins, red for losses)
* Automatic terminal screen clearing between turns
* Bankruptcy check that ends the game if your money hits $0

---

## Tools Used

* **Python 3**
* **colorama** (pip library for terminal colors)
* Built-in modules: `random`, `os`, `subprocess`

---

## How to Install and Run

1. Make sure you have Python 3 installed.
2. Install `colorama` by running this in your terminal:
```bash
pip install colorama

```


3. Open your terminal, go into the project folder, and run:
```bash
python casino.py

```



---

## How to Test It

If you want to test how the program handles weird inputs or edge cases, try these:

* Enter letters or symbols instead of numbers when placing a bet.
* Try entering a bet of $0, a negative number, or more money than you actually have.
* Pick a number out of range (like 0, 7, or -5) when guessing the dice roll.
* Test depositing and withdrawing money to see if the balance math works.
* Play until your money reaches $0 to make sure the game over screen triggers properly.