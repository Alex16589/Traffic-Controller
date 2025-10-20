# 🚦 Sequential Traffic Controller System

A **Flask-based web simulation** of a traffic light controller that manages four directions — **South, West, North, and East** — with each signal cycling **one at a time** through the proper sequence:  

> 🔴 **Red → 🟡 Yellow → 🟢 Green → 🟡 Yellow → 🔴 Red**

Built using **Python**, **Flask**, **HTML**, **CSS**, and **JavaScript**.

---

## 🧩 Features

- Four independent traffic signals: **North, South, East, West**  
- Sequential control — one direction active at a time  
- Realistic light sequence: Red → Yellow → Green → Yellow → Red  
- Web-based visualization using live updates from Flask  
- Easy to extend with timers, buttons, and more  

---

## 📁 Project Structure

```
Traffic_Controller_System/
│
├── traffic_controller.py      # Flask backend logic
├── traffic_controller.html    # Frontend web UI
└── README.md                  # Project documentation
```

---

## ⚙️ How It Works

1. **Flask Backend (`traffic_controller.py`)**
   - Runs a web server.
   - Controls the state of each traffic signal (red/yellow/green).
   - Sends the current state to the frontend every few seconds.
   - Each direction cycles in order: **South → West → North → East**.

2. **Frontend (`traffic_controller.html`)**
   - Displays all four directions as signals.
   - Uses JavaScript to fetch live traffic light data from Flask (`/state` endpoint).
   - Dynamically updates the colors in real time.

---

## 🧠 Traffic Light Logic

Each direction follows the sequence:

| Step | Color  | Meaning |
|------|--------|----------|
| 1 | 🔴 Red | Stop |
| 2 | 🟡 Yellow | Prepare to start |
| 3 | 🟢 Green | Go |
| 4 | 🟡 Yellow | Prepare to stop |
| 5 | 🔴 Red | Stop / next direction active |

Cycle order:
```
South → West → North → East → (repeat)
```

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
Make sure you have **Python 3.x** installed, then open a terminal in the project folder and run:
```bash
pip install flask
```

### 2️⃣ Run the Python App
```bash
python traffic_controller.py
```

You’ll see output like:
```
 * Running on http://127.0.0.1:5000
```

### 3️⃣ Open the Web Interface
Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.  
You’ll see the live simulation with each direction changing color in sequence.

---

## 🖥️ Demo Preview

| Direction | Example State |
|------------|----------------|
| South | 🟢 Green |
| West | 🔴 Red |
| North | 🔴 Red |
| East | 🔴 Red |

Each direction will take its turn automatically.

---

## 🔧 Customization

You can tweak the timing of each phase in the Python file:

```python
green_time = 5   # Duration of green light (seconds)
yellow_time = 2  # Duration of yellow light (seconds)
all_red_time = 1 # Delay between cycles (seconds)
```

---

## 🧱 Future Enhancements

- Add **countdown timers** for each direction  
- Add **manual control buttons** (Start / Stop / Force Green)  
- Add **pedestrian crossings** and **emergency overrides**  
- Store logs or stats in a file or database  

---

## 📸 Screenshot (Example Layout)

```
+--------------------------+
|       NORTH (🔴)         |
|                          |
| WEST (🔴)   EAST (🔴)     |
|                          |
|       SOUTH (🟢)         |
+--------------------------+
```

---

## 🧑‍💻 Technologies Used

- **Python 3**
- **Flask**
- **HTML5 / CSS3**
- **JavaScript (Fetch API)**
- **Threading** for background control loop

---

## 🪪 License

This project is open source under the [MIT License](LICENSE).

---

## ❤️ Author

**Rehan**  
*Developed as a demonstration of traffic control logic using Flask and web technologies.*
