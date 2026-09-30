# Terminal Dice Casino

## Problem Statement

When learning Python, beginners often struggle to bridge the gap between learning isolated syntax and building a cohesive, practical application. Standard exercises teach loops, conditional logic, functions, exception handling, and random number generation separately, making it hard to visualize how these concepts fit together in a real project.

This project addresses that gap by building a simple, interactive, command-line dice casino game. By combining fundamental Python concepts into a unified terminal app, learners get hands-on experience managing application state, handling unexpected user input, and controlling program flow.

---

## Scope of the Project

**In-Scope:**

* **Virtual Currency Management:** Interactive balance tracking with simulated deposits and withdrawals.
* **Dice Mechanics:** Randomized roll simulation from 1 to 6.
* **Outcome Logic:** Instant win/loss calculations based on roll results.
* **Input Validation:** Error handling to process invalid inputs (e.g., non-numeric entries or bets exceeding balance) without crashing.
* **Session Control:** Clear prompts allowing players to continue playing or quit whenever they choose.
* **Visual UI Styling:** Color-coded terminal text using `Colorama` for an engaging experience.

**Out-of-Scope:**

* Real money transactions, payment gateways, or actual financial risk/gambling integration.

---

## Target Users

* **Python Beginners:** New coders looking to build their first interactive project and see core syntax come together.
* **Computer Science Students:** Learners practicing fundamental topics like control flow, input validation, and modular functions.
* **Self-Taught Developers:** Coders looking for practical, project-based exercises to add to their early portfolios.

---

## High-Level Features

1. **Dice Rolling Engine:** Uses Python's `random` module to generate fair rolls between 1 and 6.
2. **Betting System:** Allows users to place wagers using virtual balance and updates funds instantly based on the result.
3. **Balance Management:** Keeps track of session balance with options to deposit extra virtual funds or cash out.
4. **Input Validation:** Prevents crashes by validating all keyboard inputs before running game logic.
5. **Game Loop Control:** Gives users complete control to play another round or exit gracefully.
6. **Terminal Visuals:** Enhances the command-line interface with `Colorama` (e.g., green for wins, red for losses, yellow for prompts).