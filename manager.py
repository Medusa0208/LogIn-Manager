
'''manager.py – Verwaltungsklasse für Login-Daten
Diese Datei enthält die Klasse PasswordManager mit Methoden zum:
- Laden/Speichern
- Hinzufügen
- Bearbeiten
- Löschen
- Suchen
- Filtern nach Typ

Alle Daten werden in 'passwoerter.json' abgelegt.
'''
import json
import os
from models import login_from_dict, WebLogin, AppLogin, DeviceLogin, PinLogin
from utils import get_input

DATA_FILE = "passwoerter.json"

class PasswordManager:
    def __init__(self): # Initialisiert den Passwortmanager und lädt vorhandene Einträge aus der Datei
        self.filename = DATA_FILE
        self.entries = []
        self.load_entries()

    def load_entries(self):
        """Lädt gespeicherte Einträge aus der JSON-Datei."""
        if not os.path.exists(self.filename): # Wenn Datei nicht existiert, keine Aktion nötig
            return
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    try:
                        entry = login_from_dict(item)
                        self.entries.append(entry)
                    except Exception as e:
                        print(f"⚠️ Fehler beim Laden eines Eintrags: {e}")
        except Exception as e:
            print(f"⚠️ Fehler beim Laden: {e}")

    def save_entries(self):
        """Speichert alle Einträge in die JSON-Datei."""
        try:
            with open(self.filename, "w") as file:
                json.dump([entry.to_dict() for entry in self.entries], file, indent=4)
        except Exception as e:
            print(f"⚠️ Fehler beim Speichern: {e}")

    def add_entry(self, entry): # Fügt einen neuen Login-Eintrag hinzu und speichert ihn sofort.
        self.entries.append(entry)
        self.save_entries()

    def display_entries(self): # Gibt alle gespeicherten Einträge nummeriert in der Konsole aus.
        if not self.entries:
            print("📂 Keine Einträge gefunden.")
            return
        for i, entry in enumerate(self.entries, start=1):
            print(f"\n{i})")
            entry.display()
    
    def delete_entry(self, index): # Löscht einen Login-Eintrag anhand des Index und Gibt eine Warnung aus, wenn Index ungültig ist
        if 0 <= index < len(self.entries):
            del self.entries[index]
            self.save_entries()
            print("🗑️ Eintrag gelöscht.")
        else:
            print("⚠️ Ungültiger Index.")

    def search(self, term): # Sucht nach Einträgen anhand von Beschreibung oder Benutzernamen und gibt eine Liste passender Objekte zurück
        results = []
        for entry in self.entries:
            if term.lower() in entry.description.lower():
                results.append(entry)
            elif hasattr(entry, "username") and term.lower() in entry.username.lower():
                results.append(entry)
        return results

    def edit_entry(self, index): # Ermöglicht das Bearbeiten eines bestehenden Login-Eintrags
        if 0 <= index < len(self.entries):
            entry = self.entries[index]
            print("📝 Aktueller Eintrag:")
            entry.display()
            print("🔁 Neuer Wert (leer lassen = behalten):")

            new_description = input("📝 Neue Beschreibung: ").strip()
            if new_description:
                entry.description = new_description

            if hasattr(entry, "username"):
                new_username = input("👤 Neuer Benutzername: ").strip()
                if new_username:
                    entry.username = new_username

            if hasattr(entry, "password"):
                new_password = input("🔑 Neues Passwort: ").strip()
                if new_password:
                    entry.password = new_password

            if isinstance(entry, WebLogin):
                new_url = input("🌐 Neue URL: ").strip()
                if new_url:
                    entry.url = new_url

            elif isinstance(entry, AppLogin):
                new_app = input("📱 Neuer App-Name: ").strip()
                if new_app:
                    entry.app_name = new_app

            elif isinstance(entry, DeviceLogin):
                new_device = input("💻 Neue Gerätebezeichnung: ").strip()
                if new_device:
                    entry.device = new_device

            elif isinstance(entry, PinLogin):
                new_location = input("📍 Neuer Ort: ").strip()
                if new_location:
                    entry.location = new_location
                new_pin = input("🔐 Neuer PIN: ").strip()
                if new_pin:
                    entry.pin = new_pin

            self.save_entries()
            print("✅ Eintrag aktualisiert.")
        else:
            print("⚠️ Ungültiger Index.")

    def filter_by_type(self, login_type): # Zeigt nur die Einträge, die dem angegebenen Login-Typ entsprechen
        filtered = [e for e in self.entries if e.login_type == login_type]
        if not filtered:
            print("📂 Keine Einträge dieses Typs gefunden.")
            return
        for i, entry in enumerate(filtered, start=1):
            print(f"\n{i})")
            entry.display()