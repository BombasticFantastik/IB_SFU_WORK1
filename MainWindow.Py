import sys 
from Tricemus import TricemusСode,BackTricemusСode
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit,QVBoxLayout,QWidget,QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label0=QLabel("Введите ваше ключ-слово")
        
        self.input0=QLineEdit()
        self.label1=QLabel("Введите ваше слово для кодирования")
        self.input1=QLineEdit()
        self.button0=QPushButton("Закодировать слово")
        self.button0.clicked.connect(self.the_button_was_clicked)
        
        self.label3=QLabel("ваш_результат")

        self.checkbox=QCheckBox("Обратная кодировка")
        

        layout=QVBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.label0)
        layout.addWidget(self.input0)
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        
        
        layout.addWidget(self.button0)
        
        layout.addWidget(self.label3)

        self.setFixedSize(QSize(300, 300))
        
        

        container=QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
        #меняем название
    def the_button_was_clicked(self):
        if self.checkbox.isChecked():
            code_word=self.input0.text()
            word=self.input1.text()
            new_word=BackTricemusСode(code_word,word)
            self.label3.setText(new_word)
        else:
            code_word=self.input0.text()
            word=self.input1.text()
            new_word=TricemusСode(code_word,word)
            self.label3.setText(new_word)


        


app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()