# 🃏 Kuhn Poker Game

This is a **command-line implementation** of **Kuhn Poker**, a simplified poker game with **three cards**:\
**King (K), Queen (Q), and Jack (J)**. The game is designed for **one player vs a bot**, with a automate opponent.

---

## 📌 **Game Rules**

- The deck consists of **only three cards**: `K`, `Q`, `J`.
- Each player **antes 1 chip** at the start of each round.
- Each player receives **one secret card**.
- The **first player to act** can **check or bet**.
- If the **first player checks**, the second player can **check or bet**.
- If the **first player bets**, the second player can **call or fold**.
- If a bet is **called**, the player with the **higher-ranked card wins** (`K > Q > J`).
- If a player **folds**, the other player wins **without a showdown**.
- The game continues until **one player runs out of chips**.

---

## 🔧 **Installation & Setup**

### 1⃣ **Clone the Repository**

```sh
git clone https://github.com/your-username/kuhn-poker.git
cd kuhn-poker
```

### 2⃣ **Run the Game**

Make sure you have **Python 3.x** installed, then run:

```sh
python khunpoker.py
```

### 3⃣ **Play the Game**

Follow the prompts to make decisions (`check`, `bet`, `call`, or `fold`).

---

## 🎮 **How to Play**

### **Example Game Session**

```
Your card: K
Bot's card: Hidden
Your stack: 10, Bot's stack: 10
You act first this round.
Choose to 'check' or 'bet': bet
Bot chooses to: fold
You win the pot!

Your stack: 11, Bot's stack: 9

Play another hand? (yes/no): yes
```

### **Game Flow**

1. Players **pay 1 chip ante**.
2. Players **receive a hidden card**.
3. **First player acts** (`check` or `bet`).
4. **Second player responds** (`check`, `bet`, `call`, or `fold`).
5. If both players bet and call, the **winner is determined**.
6. Game continues until **one player runs out of chips**.

---

## 🤖 **Bot Strategy (Current Version)**

- 🃏 **Always bets with a King**.
- 🔄 **Mixes between checking and betting with a Queen**.
- 🔒 **Always checks with a Jack**.
- 💪 **Calls bets with a King, sometimes with a Queen, and folds with a Jack**.

🚨 **Upcoming Feature:**\
🔄 The **bot will be improved** with a **better strategy** using **Game Theory Optimal (GTO) principles** for more challenging gameplay. Stay tuned! 🚀

---

## ✅ **Features**

- ✔️ Fully functional **Kuhn Poker** game.
- ✔️ **Simple AI (IF ELSE 🤣) bot** for single-player experience.
- ✔️ **Ante system and pot calculation** implemented correctly.
- ✔️ **Forced check-check** when a player has **no chips left to bet**.
- ✔️ **Unit-tested core functions** (`deal_cards`, `determine_winner`, `bot_action`, etc.).
- ✔️ **Command-line interface (CLI)** for a classic poker feel.

---

## 🛠 **Planned Improvements**

- 🧐 **Advanced bot strategy** (improving betting mix for GTO).
- 📊 **Game history tracking** (to analyze player and bot decisions).
- 🎨 **Graphical User Interface (GUI)** (optional future feature).

---

## 🔧 **Development & Testing**

To test the game logic, install `pytest`:

```sh
pip install pytest
```

Run tests:

```sh
pytest test_khun_poker.py
```

---

## 👨‍💻 **Contributing**

If you want to contribute:

1. Fork this repo 🍴.
2. Make your improvements ✍️.
3. Submit a Pull Request 🚀.

---

## 📃 **License**

This project is licensed under the **MIT License**. Feel free to modify and share!

---

**Happy bluffing! 🃏**\
🔥 Stay tuned for a smarter bot in the next update! 🔥

