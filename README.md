# 🔐 LogIn-Manager

Ein modularer, objektorientierter Passwort- und Login-Manager in Python – entwickelt im Rahmen einer Projektarbeit im Aufbaumodul **Programmieren**.

## ✨ Funktionen

- Verwaltung verschiedener Login-Typen:
  - 🌐 **WebLogin** (mit URL)
  - 📱 **AppLogin** (mit App-Name)
  - 💻 **DeviceLogin** (für Geräte)
  - 🔐 **PinLogin** (z. B. Türcode)
  - 🔒 **Allgemeine Logins**
- Zufällige Passwortgenerierung (optional bei Eingabe)
- Speichern aller Daten in einer JSON-Datei
- Suche nach Einträgen (nach Beschreibung oder Benutzername)
- Bearbeiten & Löschen von Einträgen
- Filtern nach Login-Typ
- Globale `exit`-Funktion zum sicheren Beenden (Eingabe: exit)
- Back-Funktion zum Zurückkehren während Eingaben (Eingabe: back)
- Objektorientierte Struktur mit Vererbung und Modularisierung
- Fehlerbehandlung & saubere Benutzerausgabe (auf Deutsch)

## 📁 Projektstruktur
LogIn-Manager/
│
├── main.py                         # Hauptmenü & Benutzerinteraktion
├── manager.py                      # Verwaltung der Login-Einträge (CRUD, Suche, JSON)
├── models.py                       # OOP-Klassenstruktur (Login, WebLogin, etc.)
├── utils.py                        # Hilfsfunktionen (Passworteingabe, Generator)
├── passwoerter.json                # JSON-Datei mit gespeicherten Logins
├── README.md                       # Projektdokumentation und Nutzungshinweise
├── .gitignore                      # Git-Konfigurationsdatei (optional)

## ⚙️ Voraussetzungen

- Python 3.7 oder neuer
- Optional: Virtuelle Umgebung für saubere Abhängigkeiten


⚙️ Programm ausführen
	1.	Stelle sicher, dass Python 3.7 oder neuer installiert ist.
	2.	Optional: Aktiviere eine virtuelle Umgebung:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


	3.	Starte das Programm:

python main.py


# Anforderungen installieren (wenn nötig)
pip install -r 