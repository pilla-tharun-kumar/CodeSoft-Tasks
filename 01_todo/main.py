import json
from pathlib import Path

DATA = Path(__file__).with_name("tasks.json")

def load():
    try:
        return json.loads(DATA.read_text())
    except FileNotFoundError:
        return []

def save(tasks):
    DATA.write_text(json.dumps(tasks, indent=2))

def main():
    tasks = load()
    while True:
        print("\nTo-do list: 1 Add  2 View  3 Edit  4 Toggle done  5 Delete  0 Quit")
        choice = input("Choice: ").strip()
        if choice == "0": break
        if choice == "1":
            title = input("Task: ").strip()
            if title: tasks.append({"title": title, "done": False}); save(tasks)
        elif choice == "2":
            for i, task in enumerate(tasks, 1): print(f"{i}. [{'x' if task['done'] else ' '}] {task['title']}")
        elif choice in {"3", "4", "5"}:
            try:
                index = int(input("Task number: ")) - 1
                if not 0 <= index < len(tasks): raise ValueError
            except ValueError:
                print("Invalid task number."); continue
            if choice == "3":
                title = input("New task: ").strip()
                if title: tasks[index]["title"] = title
            elif choice == "4": tasks[index]["done"] = not tasks[index]["done"]
            else: tasks.pop(index)
            save(tasks)
        else: print("Invalid choice.")

if __name__ == "__main__": main()
