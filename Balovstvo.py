from PyQt6.QtWidgets import QMainWindow, QApplication,QLabel, QCheckBox, QComboBox, QLineEdit,QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
from PyQt6.QtCore import Qt
import sys




class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox("hellow")
        widget.setCheckState(Qt.CheckState.Checked)

        # Включение трёх состояний: widget.setCheckState(Qt.PartiallyChecked)
        # Или: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)


    def show_state(self, s):
        print(s == Qt.CheckState.Checked)
        print(s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()