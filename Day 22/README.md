# Day 22 – Pong Game 🏓

This repository contains my **Day 22 project** from the **100 Days of Python Bootcamp (Udemy)**.
The project is a fully playable **Pong game** built using Python’s `turtle` graphics module. 
This day focused on applying **Object-Oriented Programming (OOP)** concepts, collision detection, and real-time screen updates.

---

## 🎮 Project Overview

Pong is a classic arcade game where two players control paddles to hit a ball back and forth. A player scores a point when the opponent misses the ball.

In this implementation:

* The **right paddle** is controlled using the **Up / Down arrow keys**
* The **left paddle** is controlled using **W / S keys**
* The ball speeds up slightly after every paddle hit
* Scores are displayed at the top of the screen

---

## 🧠 Concepts Learned & Applied

* Object-Oriented Programming (OOP)

  * Class inheritance using `turtle.Turtle`
  * Modular code structure (`Paddle`, `Ball`, `Scoreboard`)
* Collision detection (walls & paddles)
* Game loop with manual screen refresh (`screen.tracer(0)`)
* Keyboard event handling
* Dynamic game speed adjustment

---

## 🗂️ Project Structure

```text
Day_22_Pong_Game/
│
├── main.py          # Main game loop & event handling
├── paddle.py        # Paddle class (player controls)
├── ball.py          # Ball movement & collision logic
├── scoreboard.py    # Score tracking & display
└── assets/
    └── pong_output.png   # Game output screenshot
```

---

## ⚙️ How the Game Works

### 🟦 Paddle

* Moves vertically
* Controlled by keyboard input
* Implemented as a stretched square turtle

### ⚪ Ball

* Moves diagonally across the screen
* Bounces off walls and paddles
* Increases speed after each paddle hit
* Resets position when a point is scored

### 🧮 Scoreboard

* Displays left and right player scores
* Updates instantly when a point is scored

---

## ⌨️ Controls

| Player       | Move Up | Move Down |
| ------------ | ------- | --------- |
| Left Paddle  | W       | S         |
| Right Paddle | ↑       | ↓         |

---

## ▶️ How to Run

1. Make sure Python is installed (Python 3.x recommended)
2. Clone the repository
3. Navigate to the Day 22 folder
4. Run the game:

```bash
python main.py
```

---

## 📸 Final Output

Below is the final output of the Pong game:

> *(Screenshot attached in the repository)*

The game window displays:

* Two paddles on either side
* A moving ball
* Live score updates at the top

---

## 🚀 Key Takeaways

* Writing clean, modular code makes games easier to scale
* OOP is extremely powerful for managing game entities
* Small logic tweaks (like increasing ball speed) can greatly improve gameplay

---

## 📌 Day 22 Progress

✔ Built a complete game from scratch
✔ Applied OOP principles effectively
✔ Improved confidence in handling real-time game logic

---

### ⭐ This project is part of my **PYProject_Udemy** repository, where I consistently push my daily progress from the *100 Days of Python Bootcamp*.

If you like this project, feel free to ⭐ the repo or explore other days!

Happy Coding! 🐍✨
