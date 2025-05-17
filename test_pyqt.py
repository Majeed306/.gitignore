import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget # type: ignore

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt5 Test")
window.setGeometry(100, 100, 280, 80)

label = QLabel("<h2>Hello from PyQt5!</h2>", parent=window)
label.move(60, 15)

window.show()
sys.exit(app.exec_())
