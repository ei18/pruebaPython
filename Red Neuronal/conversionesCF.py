## CELSIUS A FAHRENHEIT

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Grados celsius y fahrenheit
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)

# Crear el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compilar el modelo
model.compile(
    loss='mean_squared_error',
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1)
)

# Entrenando el modelo. epochs -> se agrega un número más alto para que sea más exacto
history = model.fit(celsius, fahrenheit, epochs=2000, verbose=False)

# Predicción
def celsius_to_fahrenheit(celsius_input):

  celsius_input = np.array([[celsius_input]], dtype=float) # Convert to 2D NumPy array
  return model.predict(celsius_input)[0][0]

# Manejo de errores
try:
  user_celsius = float(input("Enter temperature in Celsius: "))

  fahrenheit_result = celsius_to_fahrenheit(user_celsius)
  print(f"{user_celsius} degrees Celsius is equal to {fahrenheit_result:.2f} degrees Fahrenheit.")
except ValueError:
  print("Please enter a valid numeric value.")

# Gráfica
plt.xlabel('Epoch Number')    
plt.ylabel('Loss Magnitude')
plt.plot(history.history['loss'])
plt.title("Modelo de prueba")
plt.show() 

