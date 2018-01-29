from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        'author': 'Tetrabaum',
        'books': [
            {
                'title': 'Arc of PC',
                'pages': 666
            },
            {
                'title': 'Arc of PC 2',
                'pages': 666
            },
        ]
    }
    return render_template('home.html', **context)

@app.route('/books/')
def books():
    book_name = 'Arc of PC'
    return render_template('books.html', book_n=book_name)

@app.route('/contact/')
@app.route('/contact/<phone>')
def contact(phone=None):
    if phone is None:
        phone = '88005553535'
    return 'Мой телефон: +7 (9**) ** 85 ' + phone

if __name__ == '__main__':
    app.run(debug=True)
