import json
from pathlib import Path

DATA = Path(__file__).with_name("contacts.json")
FIELDS = ("name", "phone", "email", "address")

def load():
    try: return json.loads(DATA.read_text())
    except FileNotFoundError: return []

def save(contacts): DATA.write_text(json.dumps(contacts, indent=2))

def select(contacts):
    query = input("Name or phone to search: ").strip().lower()
    matches = [(i, c) for i, c in enumerate(contacts) if query and (query in c["name"].lower() or query in c["phone"])]
    for number, (_, contact) in enumerate(matches, 1): print(f"{number}. {contact['name']} — {contact['phone']}")
    if not matches: print("No contacts found."); return None
    try:
        number = int(input("Select number: "))
        if not 1 <= number <= len(matches): raise ValueError
        return matches[number - 1][0]
    except ValueError:
        print("Invalid selection."); return None

def main():
    contacts = load()
    while True:
        print("\nContacts: 1 Add  2 List  3 Search  4 Update  5 Delete  0 Quit")
        choice = input("Choice: ").strip()
        if choice == "0": break
        if choice == "1":
            contact = {field: input(f"{field.title()}: ").strip() for field in FIELDS}
            if not contact["name"] or not contact["phone"]: print("Name and phone are required."); continue
            contacts.append(contact); save(contacts)
        elif choice == "2":
            for contact in contacts: print(f"{contact['name']} — {contact['phone']}")
        elif choice in {"3", "4", "5"}:
            index = select(contacts)
            if index is None: continue
            if choice == "3":
                for field in FIELDS: print(f"{field.title()}: {contacts[index][field]}")
            elif choice == "4":
                for field in FIELDS:
                    value = input(f"{field.title()} [{contacts[index][field]}]: ").strip()
                    if value: contacts[index][field] = value
                save(contacts)
            else: contacts.pop(index); save(contacts)
        else: print("Invalid choice.")

if __name__ == "__main__": main()
