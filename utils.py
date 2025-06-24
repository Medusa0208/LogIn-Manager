import random
import string

def generate_password(length=12):
    """
    Generiert ein zufälliges Passwort mit Buchstaben, Zahlen und Sonderzeichen.
    
    Args:
        length (int): Die gewünschte Länge des Passworts (Standard: 12).
    
    Returns:
        str: Das generierte Passwort.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def get_input(prompt, manager=None):
    """
    Holt eine Benutzereingabe und reagiert auf spezielle Befehle wie 'exit' oder 'back'.

    Args:
        prompt (str): Die Eingabeaufforderung für den Benutzer.
        manager (PasswordManager, optional): Wird übergeben, um ggf. vor 'exit' zu speichern.

    Returns:
        str: Die Benutzereingabe oder der Befehl 'BACK'.
    """
    user_input = input(prompt).strip()
    
    if user_input.lower() == "exit":
        if manager:
            print("💾 Speichere Einträge vor dem Beenden...")
            manager.save_entries()
        print("👋 Programm beendet.")
        exit()
    
    if user_input.lower() == "back":
        return "BACK"
    
    return user_input