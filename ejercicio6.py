import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QComboBox, QSpinBox, QVBoxLayout, QPushButton

class VentaCrepasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Venta de Crepas")
        
        layout = QVBoxLayout()

        # 1. RadioButtons para seleccionar el tamaño de la crepa
        self.label_tamaño = QLabel("1. Seleccione el tamaño de la crepa:", self)
        layout.addWidget(self.label_tamaño)
        
        self.radio_pequeña = QRadioButton("Pequeña", self)
        self.radio_mediana = QRadioButton("Mediana", self)
        self.radio_grande = QRadioButton("Grande", self)
        
        layout.addWidget(self.radio_pequeña)
        layout.addWidget(self.radio_mediana)
        layout.addWidget(self.radio_grande)

        # 2. ComboBox para seleccionar el tipo de relleno
        self.label_relleno = QLabel("2. Seleccione el sabor del relleno:", self)
        layout.addWidget(self.label_relleno)

        self.combo_relleno = QComboBox(self)
        self.combo_relleno.addItems(["Nutella", "Dulce de leche", "chessecake"])
        layout.addWidget(self.combo_relleno)

        # 3. SpinBox para seleccionar la cantidad de crepas
        self.label_cantidad = QLabel("3. Seleccione la cantidad de crepas:", self)
        layout.addWidget(self.label_cantidad)

        self.spin_cantidad = QSpinBox(self)
        self.spin_cantidad.setRange(1, 10)
        layout.addWidget(self.spin_cantidad)

        # Botón para mostrar datos
        self.boton = QPushButton("Mostrar Pedido", self)
        self.boton.clicked.connect(self.mostrar_datos)
        layout.addWidget(self.boton)

        self.setLayout(layout)

    def mostrar_datos(self):
        # Obtener el tamaño seleccionado
        tamaño = "No seleccionado"
        if self.radio_pequeña.isChecked():
            tamaño = "Pequeña"
        elif self.radio_mediana.isChecked():
            tamaño = "Mediana"
        elif self.radio_grande.isChecked():
            tamaño = "Grande"

        # Obtener el tipo de relleno
        relleno = self.combo_relleno.currentText()

        # Obtener la cantidad de crepas
        cantidad = self.spin_cantidad.value()

        # Mostrar el resumen en la terminal
        print(f"Tamaño: {tamaño}")
        print(f"Sabor del relleno de la crepa: {relleno}")
        print(f"Cantidad: {cantidad}")

# Inicializar la aplicación
app = QApplication(sys.argv)
ventana = VentaCrepasWindow()
ventana.show()
sys.exit(app.exec_())

#Inspirado en una venta de crepas:
#Este programa soluciona la necesidad de gestionar pedidos de un producto con múltiples opciones personalizables de 
#una manera clara y eficiente. Permite a los clientes seleccionar sus preferencias en cuanto al tamaño, tipo de relleno y cantidad de 
#crepas, simplificando el proceso de compra y evitando errores en la toma de pedidos.
