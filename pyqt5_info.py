import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QWidget , QVBoxLayout , QHBoxLayout , QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my cool first GUI")
        self.setGeometry(0 , 0 , 500 , 500)
        self.initUI()

        # label = QLabel("udayan singh" , self)

        # label.setFont(QFont("Arial" , 30))

        # label.setGeometry(0,0,500,100)

        # label.setStyleSheet("color: blue;" "background-color:black;" "font-weight:bold;" "font-style:italic;" "text-decoration:underline")
        # # label.setAlignment(Qt.AlignTop)
        # # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)

        # label = QLabel(self)
        # label.setGeometry(0,0,500,500)

        # pixmap = QPixmap("images.jpg")
        # label.setPixmap(pixmap)
        # label.setScaledContents(True)

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1" , self)
        label2 = QLabel("#2" , self)
        label3 = QLabel("#3" , self)
        label4 = QLabel("#4" , self)
        label5 = QLabel("#5" , self)

        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: black")
        label4.setStyleSheet("background-color: orange")
        label5.setStyleSheet("background-color: yellow")

        # vbox = QVBoxLayout()

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # hbox = QVBoxLayout()

        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)

        grid= QGridLayout()

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1,0)
        grid.addWidget(label4,1,1)
        grid.addWidget(label5,1,2)


        # central_widget.setLayout(vbox)
        # central_widget.setLayout(hbox)
        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

9:53