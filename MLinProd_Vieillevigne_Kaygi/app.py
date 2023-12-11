from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# Charger la base de données depuis le fichier CSV
try:
    df = pd.read_csv('Spotify.csv')
    items = df.values.tolist()
except FileNotFoundError:
    items = []

@app.route('/')
def index():
    indexed_items = [(index, item) for index, item in enumerate(items)]
    return render_template('suggestions.html', items=indexed_items)

@app.route('/add', methods=['POST'])
def add():
    artiste = request.form.get('artiste')
    musique = request.form.get('musique')
    if artiste and musique:
        new_item = [artiste, musique]
        items.append(new_item)
        # Mettre à jour le fichier CSV
        update_csv()
    return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    artiste = request.form.get('artiste')
    musique = request.form.get('musique')
    if 0 <= index < len(items) and artiste and musique:
        items[index] = [artiste, musique]
        # Mettre à jour le fichier CSV
        update_csv()
    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(items):
        del items[index]
        # Mettre à jour le fichier CSV
        update_csv()
    return redirect('/')

def update_csv():
    # Mettre à jour le fichier CSV avec les données actuelles
    df = pd.DataFrame(items, columns=['Artiste', 'Titre'])
    df.to_csv('Spotify.csv', index=False)

if __name__ == '__main__':
    app.run(debug=True)
