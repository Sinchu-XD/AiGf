import json
import os

FILE = "userdata.json"

def load_data():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump({}, f)
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def set_name(user_id: int, name: str):
    data = load_data()
    data[str(user_id)] = {"name": name}
    save_data(data)

def get_name(user_id: int):
    data = load_data()
    return data.get(str(user_id), {}).get("name", None)
  
