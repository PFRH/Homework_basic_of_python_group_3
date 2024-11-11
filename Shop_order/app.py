# app.py
from flask import Flask, render_template, request, redirect, url_for
import threading
import socket

app = Flask(__name__)
clients = []

def socket_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 65432))
    server.listen()
    print("Socket-Server läuft...")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        print(f"Neue Verbindung von {addr}")

# Starten des Socket-Servers in einem separaten Thread
socket_thread = threading.Thread(target=socket_server, daemon=True)
socket_thread.start()

@app.route('/')
def order_form():
    return render_template('order_form.html')

@app.route('/submit', methods=['POST'])
def submit_order():
    # Sammeln der Formulardaten
    email = request.form.get('email')
    vorname = request.form.get('vorname')
    nachname = request.form.get('nachname')
    firma = request.form.get('firma', '')  # Optionales Feld
    strasse = request.form.get('strasse')
    hausnummer = request.form.get('hausnummer')
    plz = request.form.get('plz')
    stadt = request.form.get('stadt')
    land = request.form.get('land')
    telefon = request.form.get('telefon')

    # Formatierung der Daten für die Ausgabe in der Konsole und die Pygame-Clients
    formatted_data = (
        f"E-Mail: {email}\n"
        f"Name: {vorname} {nachname}\n"
        f"Firma: {firma}\n"
        f"Adresse: {strasse} {hausnummer}, {plz} {stadt}, {land}\n"
        f"Telefon: {telefon}"
    )

    # Ausgabe in der Konsole
    print("Bestelldaten erhalten:\n" + formatted_data)

    # Senden der formatierten Daten an alle verbundenen Pygame-Clients
    for client in clients[:]:  # Kopie der Liste, um Änderungen während der Iteration zu vermeiden
        try:
            client.sendall(formatted_data.encode())
        except BrokenPipeError:
            clients.remove(client)

    # Weiterleitung zur Danke-Seite
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
