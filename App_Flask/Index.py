from flask import Flask, render_template

app =Flask(__name__)

"""
@app.route('/')
def pricipal():
    return "Bienvenido a mi sitio Web con Python zorrita beeeeb"
"""

#retona plantilla HTML
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes = ("PHP", "Python", "Java", "C#",
                    "JavaScript", "Perl", "Ruby", "Rust")
    return render_template('lenguajes.html', lenguajes=misLenguajes)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__=='__main__':
    app.run(debug=True)
