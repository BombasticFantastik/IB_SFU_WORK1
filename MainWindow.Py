import sys 
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit,QVBoxLayout,QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label=QLabel("Введите ваше слово")
        self.input=QLineEdit()

        layout=QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        container=QWidget()
        
        container.setLayout(layout)
        

        self.setCentralWidget(container)
    
        #меняем название

        


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()