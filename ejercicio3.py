import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
      
        self.setWindowTitle('Ingresar Cédula y Nombre')
        self.setGeometry(100, 100, 300, 250)
        
    
        self.cedula_label = QLabel('Número de Cédula:', self)
        self.nombre_label = QLabel('Nombre Completo:', self)
        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)
        
         
        self.cedula_input = QLineEdit(self)
        self.cedula_input.setPlaceholderText("Número de cédula")
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText("Nombre completo")
        
         
        self.boton_mostrar = QPushButton('Mostrar Datos', self)
        self.boton_mostrar.clicked.connect(self.mostrar_datos)
        
         
        layout = QVBoxLayout()
        layout.addWidget(self.cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.boton_mostrar)
        layout.addWidget(self.resultado_label)
        
        
        self.setLayout(layout)
    
    def mostrar_datos(self):
      
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()
        
        
        if cedula and nombre:
            self.resultado_label.setText(f'Cédula: {cedula}\nNombre: {nombre}')
        else:
            self.resultado_label.setText('Por favor, ingresa ambos datos.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
