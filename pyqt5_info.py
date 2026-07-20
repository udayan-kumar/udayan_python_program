import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my cool first GUI")
        self.setGeometry(0 , 0 , 500 , 500)

        # label = QLabel("udayan singh" , self)

        # label.setFont(QFont("Arial" , 30))

        # label.setGeometry(0,0,500,100)

        # label.setStyleSheet("color: blue;" "background-color:black;" "font-weight:bold;" "font-style:italic;" "text-decoration:underline")
        # # label.setAlignment(Qt.AlignTop)
        # # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)

        label = QLabel(self)
        label.setGeometry(0,0,500,500)

        pixmap = QPixmap("images.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

  