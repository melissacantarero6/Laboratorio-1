import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Ingresar Clave Secreta')
        self.setGeometry(100, 100, 300, 200)
        
       
        self.instrucciones_label = QLabel('Ingresa tu clave secreta:', self)
        self.instrucciones_label.setAlignment(Qt.AlignCenter)
        
        
        self.clave_input = QLineEdit(self)
        self.clave_input.setEchoMode(QLineEdit.Password)  
        self.clave_input.setPlaceholderText("Clave secreta")
        
        self.boton_mostrar = QPushButton('Mostrar Clave', self)
        self.boton_mostrar.clicked.connect(self.mostrar_clave)
        
        
        self.resultado_label = QLabel('', self)
        self.resultado_label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.instrucciones_label)
        layout.addWidget(self.clave_input)
        layout.addWidget(self.boton_mostrar)
        layout.addWidget(self.resultado_label)
       
        self.setLayout(layout)
    
    def mostrar_clave(self):
        
        clave = self.clave_input.text()
        self.resultado_label.setText(f'Clave ingresada: {clave}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())


