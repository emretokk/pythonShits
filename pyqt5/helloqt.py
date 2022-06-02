from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

# Dark Theme
# qApp.setStyle("Fusion")

# dark_palette = QPalette()

# dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
# dark_palette.setColor(QPalette.WindowText, Qt.white)
# dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
# dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
# dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
# dark_palette.setColor(QPalette.ToolTipText, Qt.white)
# dark_palette.setColor(QPalette.Text, Qt.white)
# dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
# dark_palette.setColor(QPalette.ButtonText, Qt.white)
# dark_palette.setColor(QPalette.BrightText, Qt.red)
# dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
# dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
# dark_palette.setColor(QPalette.HighlightedText, Qt.black)

# qApp.setPalette(dark_palette)

# qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

app = QApplication([])
app.setStyle('Fusion') # 'Windows', 'Fusion', $ windows only 'WindowsVista', $ mac only 'Macintosh'
window = QWidget()

topButton = QPushButton("Top")
bottomButton = QPushButton("Bottom")

def topButtonClicked():
	alert = QMessageBox()
	alert.setText("You clicked the 'Top' button")
	alert.exec()

topButton.clicked.connect(topButtonClicked)

layout = QVBoxLayout()
layout.addWidget(topButton)
layout.addWidget(bottomButton)

palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)

app.setStyleSheet("QPushButton { padding: 10px }")

window.setLayout(layout)
window.show()
app.exec()