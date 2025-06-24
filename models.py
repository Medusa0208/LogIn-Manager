# models.py

class Login:
    """
    Basisklasse für einen allgemeinen Login-Eintrag.
    
    Attribute:
        login_type (str): Typ des Logins (z. B. "Web", "App", "Device", etc.)
        description (str): Beschreibung des Eintrags
        username (str): Benutzername
        password (str): Passwort
    """

    def __init__(self, login_type, description, username, password):
        self.login_type = login_type
        self.description = description
        self.username = username
        self.password = password

    def display(self): # Gibt die Login-Daten formatiert aus.
        print(f"[{self.login_type}] {self.description}")
        print(f"👤 Benutzername: {self.username}")
        print(f"🔑 Passwort: {self.password}")

    def to_dict(self): # Gibt die Login-Daten als Dictionary zurück (für JSON-Speicherung).
        return {
            "login_type": self.login_type,
            "description": self.description,
            "username": self.username,
            "password": self.password
        }


class WebLogin(Login): 
    """
    Spezialisierung für Web-Logins mit URL-Feld.

    Attribute:
        url (str): Die Website-URL zum Login
    """
    def __init__(self, description, url, username, password):
        super().__init__("Web", description, username, password)
        self.url = url

    def display(self):
        super().display()
        print(f"🌐 URL: {self.url}")

    def to_dict(self):
        data = super().to_dict()
        data["url"] = self.url
        return data


class AppLogin(Login):
    """
    Spezialisierung für App-Logins mit App-Namen.

    Attribute:
        app_name (str): Name der App, für die der Login gilt
        description (str): Beschreibung des Eintrags (geerbt von Login)
        username (str): Benutzername (geerbt von Login)
        password (str): Passwort (geerbt von Login)
    """
    def __init__(self, description, app_name, username, password):
        super().__init__("App", description, username, password)
        self.app_name = app_name

    def display(self):
        super().display()
        print(f"📱 App-Name: {self.app_name}")

    def to_dict(self):
        data = super().to_dict()
        data["app_name"] = self.app_name
        return data


class DeviceLogin(Login): 
    """
    Spezialisierung für Geräte-Logins (z. B. Computer, SmartTV).

    Attribute:
        device (str): Gerätebezeichnung, z. B. "MacBook", "Samsung TV"
        description (str): Beschreibung des Eintrags (geerbt von Login)
        username (str): Benutzername (geerbt von Login)
        password (str): Passwort (geerbt von Login)
    """
    def __init__(self, description, device, username, password):
        super().__init__("Device", description, username, password)
        self.device = device

    def display(self):
        super().display()
        print(f"💻 Gerät: {self.device}")

    def to_dict(self):
        data = super().to_dict()
        data["device"] = self.device
        return data


class PinLogin:
    """
    Spezialklasse für PIN-Zugänge ohne Benutzername/Passwort.
    
    Attribute:
        description (str): Beschreibung (z. B. "Wohnungstür")
        location (str): Ort des PIN-Zugangs
        pin (str): Die PIN selbst
    """

    def __init__(self, description, location, pin):
        self.login_type = "PIN"
        self.description = description
        self.location = location
        self.pin = pin

    def display(self):
        print(f"[{self.login_type}] {self.description}")
        print(f"📍 Ort: {self.location}")
        print(f"🔐 PIN: {self.pin}")

    def to_dict(self):
        return {
            "login_type": self.login_type,
            "description": self.description,
            "location": self.location,
            "pin": self.pin
        }
    
def login_from_dict(data):
    """
    Erstellt ein Login-Objekt anhand eines Dictionary-Eintrags aus der JSON-Datei.
    
    Args:
        data (dict): Dictionary mit gespeicherten Login-Daten
    
    Returns:
        Ein Instanz-Objekt der passenden Login-Klasse
    """
    login_type = data.get("login_type")

    if login_type == "Web":
        return WebLogin(
            description=data["description"],
            url=data["url"],
            username=data["username"],
            password=data["password"]
        )
    elif login_type == "App":
        return AppLogin(
            description=data["description"],
            app_name=data["app_name"],
            username=data["username"],
            password=data["password"]
        )
    elif login_type == "Device":
        return DeviceLogin(
            description=data["description"],
            device=data["device"],
            username=data["username"],
            password=data["password"]
        )
    elif login_type == "PIN":
        return PinLogin(
            description=data["description"],
            location=data["location"],
            pin=data["pin"]
        )
    elif login_type == "Allgemein":
        return Login(
            login_type="Allgemein",
            description=data["description"],
            username=data["username"],
            password=data["password"]
        )
    else:
        raise ValueError(f"Unbekannter Login-Typ: {login_type}")