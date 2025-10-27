from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# --- RUTA PRINCIPAL ---
@app.route('/')
def index():
    return render_template('index.html')

# --- RUTA PARA SUBIR EXCEL ---
@app.route('/subir_excel', methods=['POST'])
def subir_excel():
    try:
        file = request.files['file']
        if not file:
            return "No se seleccionó ningún archivo", 400

        df = pd.read_excel(file, dtype=str)  # mantiene los valores tal como están
        tabla_html = df.to_html(index=False, na_rep='', escape=False)

        return render_template('index.html', tabla=tabla_html)

    except Exception as e:
        return f"Error al procesar el archivo: {e}"

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True, port=5000)