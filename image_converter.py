from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout,QLineEdit, QPushButton, QHBoxLayout, QLCDNumber, QLabel, QWidget
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer
import time
from PIL import Image

a = chr(34)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(272, 72, 800, 600)
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setWindowTitle("\t IMAGE CONVERTER")
        self.setWindowIcon(QIcon("burger.ico"))


        self.lcd_number()

    def lcd_number(self):

        vbox = QVBoxLayout()
        self.label = QLabel("      IMAGE CONVERTER")
        self.label.setStyleSheet("background-color:white")
        self.label.setFont(QFont("times new roman", 48))
        self.label.setFixedHeight(120)
        vbox.addWidget(self.label)

        self.label2 = QLabel("      Image MUST be in SQUARE dimensions.\n"
                             "      OTHERWISE, software would convert PORTRAIT image into LANDSCAPE\n"
                             "      and SQUEEZE the Landscape image into a Square")
        self.label2.setStyleSheet("background-color:yellow")
        self.label2.setFont(QFont("times new roman", 12))
        self.label2.setFixedHeight(72)

        hbox = QHBoxLayout()

        self.label3 = QLabel(" NOTE  ")
        self.label3.setStyleSheet("color:Red")
        self.label3.setFont(QFont("castellar", 27))
        self.label3.setFixedHeight(72)
        self.label3.setFixedWidth(144)

        hbox.addWidget(self.label3)
        hbox.addWidget(self.label2)

        vbox.addLayout(hbox)



        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("\tEnter the Image link here")
        self.input1.setFont(QFont("times new roman", 12))
        self.input1.setFixedHeight(60)
        self.input1.setStyleSheet("background-color:white")
        vbox.addWidget(self.input1)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox3 = QHBoxLayout()

        self.label4 = QLabel(" NAME   ")
        self.label4.setStyleSheet("color:indigo")
        self.label4.setFont(QFont("castellar", 27))
        self.label4.setFixedHeight(72)
        self.label4.setFixedWidth(144)
        hbox3.addWidget(self.label4)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("\tEnter Name of the Image that will be exported")
        self.input2.setFont(QFont("times new roman", 12))
        self.input2.setFixedHeight(60)
        self.input2.setStyleSheet("background-color:white")
        hbox3.addWidget(self.input2)

        vbox.addLayout(hbox3)

        btn1 = QPushButton(" Export .ico ")
        btn1.setFont(QFont("times new roman", 36))
        btn1.setStyleSheet("background-color:green")
        btn1.clicked.connect(self.ico)
        hbox1.addWidget(btn1)

        btn2 = QPushButton(" Export .pdf ")
        btn2.setFont(QFont("times new roman", 36))
        btn2.setStyleSheet("background-color:red")
        btn2.clicked.connect(self.pdf)
        hbox1.addWidget(btn2)

        btn3 = QPushButton(" Export .png ")
        btn3.setFont(QFont("times new roman", 36))
        btn3.setStyleSheet("background-color:yellow")
        btn3.clicked.connect(self.png)
        hbox2.addWidget(btn3)

        btn4 = QPushButton(" Export .jpg ")
        btn4.setFont(QFont("times new roman", 36))
        btn4.setStyleSheet("background-color:blue")
        btn4.clicked.connect(self.jpg)
        hbox2.addWidget(btn4)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

    def ico(self):
        image_link = self.input1.text().lstrip().rstrip()
        stripper = image_link.split(a)
        image_link = stripper[1]
        my_image = Image.open(image_link)
        output_name = self.input2.text().lstrip().rstrip()
        if output_name == "":
            output_name = "Untitled"
        output_name += '.ico'
        my_image.save(output_name, 'ico')

    def pdf(self):
        image_link = self.input1.text().lstrip().rstrip()
        stripper = image_link.split(a)
        image_link = stripper[1]
        my_image = Image.open(image_link)
        output_name = self.input2.text().lstrip().rstrip()
        if output_name == "":
            output_name = "Untitled"
        output_name += '.pdf'
        my_image.save(output_name, 'pdf')

    def png(self):
        image_link = self.input1.text().lstrip().rstrip()
        stripper = image_link.split(a)
        image_link = stripper[1]
        my_image = Image.open(image_link)
        output_name = self.input2.text().lstrip().rstrip()
        if output_name == "":
            output_name = "Untitled"
        output_name += '.png'
        my_image.save(output_name, 'png')

    def jpg(self):
        image_link = self.input1.text().lstrip().rstrip()
        stripper = image_link.split(a)
        image_link = stripper[1]
        my_image = Image.open(image_link)
        output_name = self.input2.text().lstrip().rstrip()
        if output_name == "":
            output_name = "Untitled"
        output_name += '.jpg'
        my_image.save(output_name, 'jpg')



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

