# client.py
import pygame
import socket
import threading
import sys

def receive_data(sock, messages):
    """
    Empfangsfunktion für den Client.
    Wartet auf Daten vom Server und fügt sie zur Nachrichtenliste hinzu.
    """
    while True:
        try:
            data = sock.recv(1024).decode()
            if data:
                print("Empfangene Daten:\n" + data)
                messages.clear()  # Vorherige Nachrichten löschen
                messages.extend(data.splitlines())  # Daten in Zeilen aufteilen und speichern
        except ConnectionResetError:
            print("Verbindung zum Server verloren.")
            break
        except Exception as e:
            print(f"Fehler: {e}")
            break

def main():
    # Pygame initialisieren
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Pygame Bestelldaten-Client')
    font = pygame.font.Font(None, 36)
    messages = []

    # Verbindung zum Server herstellen
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(('localhost', 65432))
        print("Verbindung zum Server hergestellt.")
    except ConnectionRefusedError:
        print("Konnte keine Verbindung zum Server herstellen.")
        sys.exit()

    # Empfangsthread starten
    threading.Thread(target=receive_data, args=(sock, messages), daemon=True).start()

    # Haupt-Loop für Pygame
    running = True
    while running:
        screen.fill((255, 255, 255))  # Hintergrundfarbe setzen (weiß)
        
        # Ereignisse prüfen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Empfangene Nachrichten anzeigen
        y = 20  # Y-Position für die Anzeige der Nachrichten
        for message in messages:
            text = font.render(message, True, (0, 0, 0))  # Schwarzer Text
            screen.blit(text, (20, y))
            y += 40  # Abstand zwischen den Zeilen

        pygame.display.flip()  # Bildschirm aktualisieren

    # Verbindung schließen und Pygame beenden
    sock.close()
    pygame.quit()

if __name__ == '__main__':
    main()
