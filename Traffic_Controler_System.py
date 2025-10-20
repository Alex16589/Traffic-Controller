from flask import Flask, render_template_string, jsonify
import threading
import time
import os

app = Flask(__name__)

# Traffic state for each direction
traffic_state = {
    "north": "red",
    "south": "red",
    "east": "red",
    "west": "red"
}

# Load HTML file
html_file = os.path.join(os.path.dirname(__file__), "traffic_controller.html")
with open(html_file, "r") as f:
    html_page = f.read()

@app.route("/")
def index():
    return render_template_string(html_page)

@app.route("/state")
def get_state():
    return jsonify(traffic_state)

def traffic_loop():
    sequence = ["south", "west", "north", "east"]  # Order of directions
    all_red_time = 1
    yellow_time = 2
    green_time = 5

    while True:
        for dir in sequence:
            # Step 1: All red
            traffic_state.update({d: "red" for d in traffic_state})
            time.sleep(all_red_time)

            # Step 2: Red → Yellow (prepare to go green)
            traffic_state[dir] = "yellow"
            time.sleep(yellow_time)

            # Step 3: Green
            traffic_state[dir] = "green"
            time.sleep(green_time)

            # Step 4: Green → Yellow (prepare to stop)
            traffic_state[dir] = "yellow"
            time.sleep(yellow_time)

            # Step 5: Back to red
            traffic_state[dir] = "red"

# Start background thread
threading.Thread(target=traffic_loop, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)
