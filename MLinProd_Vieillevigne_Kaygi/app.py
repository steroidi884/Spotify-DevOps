from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Liste pour stocker les éléments
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
        items.append(f"{artiste} - {musique}")
    return redirect('/')


@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    # Récupérez les nouvelles valeurs de l'artiste et de la musique
    artiste = request.form.get('artiste')
    musique = request.form.get('musique')
    if 0 <= index < len(items) and artiste and musique:
        items[index] = f"{artiste} - {musique}"
    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(items):
        del items[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)