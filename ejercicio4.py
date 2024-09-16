import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class MascotasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos de Mascotas")
        
        
        layout = QVBoxLayout()
 
        self.mascotas = []
        for i in range(1, 4):
            layout.addWidget(QLabel(f"Mascota {i}"))
            nombre = QLineEdit(self)
            nombre.setPlaceholderText(f"Nombre de la mascota {i}")
            layout.addWidget(nombre)
            
            especie = QLineEdit(self)
            especie.setPlaceholderText(f"Especie de la mascota {i}")
            layout.addWidget(especie)
            
            edad = QLineEdit(self)
            edad.setPlaceholderText(f"Edad de la mascota {i}")
            layout.addWidget(edad)
            
            self.mascotas.append((nombre, especie, edad))
 
        self.boton = QPushButton("Mostrar Datos", self)
        self.boton.clicked.connect(self.mostrar_datos)
        layout.addWidget(self.boton)

         
        self.setLayout(layout)

    def mostrar_datos(self):
        for idx, (nombre, especie, edad) in enumerate(self.mascotas, start=1):
            print(f"Mascota {idx}:")
            print(f"Nombre: {nombre.text()}")
            print(f"Especie: {especie.text()}")
            print(f"Edad: {edad.text()}")
            print("---")

# Crear la aplicación y la ventana
app = QApplication(sys.argv)
ventana = MascotasWindow()
ventana.show()
sys.exit(app.exec_())
