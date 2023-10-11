from flask import Flask, jsonify

app = Flask(__name__)

# Estructura de datos para almacenar las entradas del blog (lista de diccionarios)
entradas_blog = [
    {
        'id': 1,
        'titulo': 'Primer Post',
        'contenido': 'Este es el contenido del primer post en mi blog.',
    },
    {
        'id': 2,
        'titulo': 'Segundo Post',
        'contenido': 'Este es el contenido del segundo post en mi blog.',
    },
    {
        'id': 3,
        'titulo': 'Tercer Post',
        'contenido': 'Este es el contenido del tercer post en mi blog.',
    },
    # Puedes agregar más entradas según sea necesario.
]

@app.route('/')
def hola_mundo():
    return '¡Hola! Bienvenido a mi blog.'

@app.route('/post/<int:post_id>')
def mostrar_entrada(post_id):
    # Código para mostrar una entrada específica (se mantiene igual)
    entrada = next((entrada for entrada in entradas_blog if entrada['id'] == post_id), None)

    if entrada:
        return f"Mostrando la entrada del blog con el ID: {post_id}\nTítulo: {entrada['titulo']}\nContenido: {entrada['contenido']}"
    else:
        return f"No se encontró una entrada con el ID: {post_id}"

@app.route('/posts')
def obtener_titulos_entradas():
    # Devolver una lista de títulos de todas las entradas
    titulos = [entrada['titulo'] for entrada in entradas_blog]
    return jsonify(titulos)

if __name__ == '__main__':
    app.run()