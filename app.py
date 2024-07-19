import os
from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Configurar Matplotlib para usar el backend 'Agg'
import matplotlib
matplotlib.use('Agg')


# Se inicia el Framework Flask de Python:
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediccion = None
    plot_path = None
    if request.method == 'POST':
        # Se obtienen los datos del formulario(página web)
        a = list(map(float, request.form['a'].split(',')))
        b = list(map(float, request.form['b'].split(',')))
        learning_rate = float(request.form['learning_rate'])
        epochs = int(request.form['epochs'])
        valorp = float(request.form['valorp'])
        
        # Se convierten las listas ingresadas por el usuario a arrays numpy
        a = np.array(a, dtype=float)
        b = np.array(b, dtype=float)
        
        # Creación de dos capas con una unidad(neurona) en cada una, es decir 1 input y 1 output
        modelo = tf.keras.Sequential([
            #tf.keras.layers.Input(shape=[1]),
            #tf.keras.layers.Dense(units=1)

            #--------------------------------------------------
            #Si se desea agregar más capas y más neuronas:
            #Por ejemplo agregar dos capas intermedias con 3 neuronas, para que aprenda más nuestra red neuronal:
                        
            tf.keras.layers.Input(shape=[1]),# Capa de entrada con una neurona
            tf.keras.layers.Dense(units=3, activation='relu'),  # Primera capa intermedia con 3 neuronas
            tf.keras.layers.Dense(units=3, activation='relu'),  # Segunda capa intermedia con 3 neuronas
            tf.keras.layers.Dense(units=1)  # Capa de salida con una neurona

        ])
        
        modelo.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate),
            loss='mean_squared_error'
        )
        
        historial = modelo.fit(a, b, epochs=epochs, verbose=False)
        
        # Realizar predicción
        prediccion = modelo.predict(np.array([valorp]))[0][0]

        # Generar y guardar la gráfica de pérdida en una ubicación temporal
        plt.figure()
        plt.xlabel("# Época")
        plt.ylabel("Magnitud de pérdida")
        plt.plot(historial.history["loss"])
        
        # Guardar la figura en un archivo temporal
        plot_path = 'static/images/loss_plot.png'
        plt.savefig(plot_path)
        
        # Cerrar la figura para liberar recursos
        plt.close()

    return render_template('index.html', prediccion=prediccion, plot_path=plot_path)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
