import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle('Nombre y Edad')
        self.setGeometry(100, 100, 300, 200)
        
        
        self.nombre_label = QLabel('Nombre Completo: Juan Pérez', self)
        self.edad_label = QLabel('Edad: 25 años', self)
        
        
        self.nombre_label.setAlignment(Qt.AlignCenter)
        self.edad_label.setAlignment(Qt.AlignCenter)
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.edad_label)
        
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
