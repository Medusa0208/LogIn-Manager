# main.py

from manager import PasswordManager
from models import Login, WebLogin, AppLogin, DeviceLogin, PinLogin
from utils import generate_password, get_input

def get_input(prompt, manager=None):
    user_input = input(prompt)
    if user_input.strip().lower() == "exit":
        if manager:
            print("💾 Speichere Einträge vor dem Beenden...")
            manager.save_entries()
        print("👋 Programm beendet.")
        exit()
    if user_input.strip().lower() == "back":
        return "BACK"
    return user_input

def show_menu():
    print("\n🔐 Passwort-Manager Menü")
    print("1) Eintrag hinzufügen")
    print("2) Einträge anzeigen")
    print("3) Eintrag löschen")
    print("4) Eintrag suchen")
    print("5) Eintrag bearbeiten")
    print("6) Nach Typ filtern")
    print("7) Beenden")

def add_entry(manager):  # Fragt den Benutzer nach den Angaben für einen neuen Login-Eintrag. 
    while True: 
        print("\n➕ Welcher Typ von Login?") 
        print("1) Web")
        print("2) App")
        print("3) Gerät")
        print("4) PIN")
        print("5) Allgemein")

        entry_type = get_input("👉 Auswahl (1–5): ", manager)
        if entry_type == "BACK":
            return

        description = get_input("📝 Beschreibung: ", manager)
        if description == "BACK":
            continue

        if entry_type == "1":
            url = get_input("🌐 URL: ", manager)
            if url == "BACK": continue
            username = get_input("👤 Benutzername: ", manager)
            if username == "BACK": continue
            password = get_input("🔑 Passwort (leer = zufällig): ", manager)
            if password == "BACK": continue
            if not password:
                password = generate_password()
                print(f"🔐 Generiertes Passwort: {password}")
            entry = WebLogin(description, url, username, password)

        elif entry_type == "2":
            app_name = get_input("📱 App-Name: ", manager)
            if app_name == "BACK": continue
            username = get_input("👤 Benutzername: ", manager)
            if username == "BACK": continue
            password = get_input("🔑 Passwort (leer = zufällig): ", manager)
            if password == "BACK": continue
            if not password:
                password = generate_password()
                print(f"🔐 Generiertes Passwort: {password}")
            entry = AppLogin(description, app_name, username, password)

        elif entry_type == "3":
            device = get_input("💻 Gerätebezeichnung: ", manager)
            if device == "BACK": continue
            username = get_input("👤 Benutzername: ", manager)
            if username == "BACK": continue
            password = get_input("🔑 Passwort (leer = zufällig): ", manager)
            if password == "BACK": continue
            if not password:
                password = generate_password()
                print(f"🔐 Generiertes Passwort: {password}")
            entry = DeviceLogin(description, device, username, password)

        elif entry_type == "4":
            location = get_input("📍 Ort (z. B. Tür, Tresor): ", manager)
            if location == "BACK": continue
            pin = get_input("🔐 PIN: ", manager)
            if pin == "BACK": continue
            entry = PinLogin(description, location, pin)

        elif entry_type == "5":
            username = get_input("👤 Benutzername: ", manager)
            if username == "BACK": continue
            password = get_input("🔑 Passwort (leer = zufällig): ", manager)
            if password == "BACK": continue
            if not password:
                password = generate_password()
                print(f"🔐 Generiertes Passwort: {password}")
            entry = Login("Allgemein", description, username, password)

        else:
            print("❌ Ungültige Auswahl.")
            continue

        manager.add_entry(entry)
        print("✅ Eintrag gespeichert!")
        break

def delete_entry(manager): #Löscht einen gewählten Eintrag anhand der Nummer.
    manager.display_entries()
    index_input = get_input("\n❌ Welchen Eintrag löschen? (Nummer): ", manager)
    if index_input == "BACK":
        return
    try:
        index = int(index_input) - 1
        manager.delete_entry(index)
    except ValueError:
        print("⚠️ Ungültige Eingabe.")

def search_entries(manager): # Durchsucht alle Einträge nach Beschreibung oder Benutzername.
    term = get_input("🔍 Suchbegriff eingeben (Beschreibung oder Benutzername): ", manager)
    if term == "BACK":
        return
    results = manager.search(term)
    if not results:
        print("❌ Keine passenden Einträge gefunden.")
        return
    print(f"\n🔎 {len(results)} Treffer gefunden:")
    for i, entry in enumerate(results, start=1):
        print(f"\nTreffer {i}:")
        entry.display()

def edit_entry(manager): # Erlaubt das gezielte Bearbeiten eines bestehenden Eintrags.
    manager.display_entries()
    index_input = get_input("\n✏️ Welchen Eintrag bearbeiten? (Nummer): ", manager)
    if index_input == "BACK":
        return
    try:
        index = int(index_input) - 1
        manager.edit_entry(index)
    except ValueError:
        print("⚠️ Ungültige Eingabe.")

def filter_by_type(manager): # Zeigt nur Einträge eines bestimmten Login-Typs.
    print("\n📂 Nach welchem Typ filtern?")
    print("1) Web")
    print("2) App")
    print("3) Gerät")
    print("4) PIN")
    print("5) Allgemein")
    selection = get_input("👉 Auswahl (1–5): ", manager)
    if selection == "BACK":
        return

    type_map = {
        "1": "Web",
        "2": "App",
        "3": "Geraet",
        "4": "PIN",
        "5": "Allgemein"
    }

    type_name = type_map.get(selection)
    if type_name:
        manager.filter_by_type(type_name)
    else:
        print("❌ Ungültige Auswahl!")

def main(): # Startet das Hauptmenü des Passwort-Managers und leitet alle Aktionen.
    manager = PasswordManager()
    while True:
        show_menu()
        choice = get_input("\n➡️ Auswahl: ", manager)

        if choice == "1":
            add_entry(manager)
        elif choice == "2":
            manager.display_entries()
        elif choice == "3":
            delete_entry(manager)
        elif choice == "4":
            search_entries(manager)
        elif choice == "5":
            edit_entry(manager)
        elif choice == "6":
            filter_by_type(manager)
        elif choice == "7":
            manager.save_entries()
            print("👋 Programm beendet.")
            break
        elif choice == "BACK":
            continue
        else:
            print("❌ Ungültige Eingabe!")

if __name__ == "__main__":
    main()