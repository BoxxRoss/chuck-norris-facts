import sys
import controller
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QComboBox,
    QTextEdit,  

    
)
bg_color = "#424242"
color = "white"

category_selected = "joke goes here"

from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(600,400)
        self.setWindowTitle("Chuck Norris Facts")
       
        self.setStyleSheet(f"background-color: {bg_color}; color: {color};")
        self.setContentsMargins(20,20,20,20)

        layout = QVBoxLayout()
        
        title = QLabel("Chuck Norris Facts")
        title.setFont(QFont("Impact",22,800))
        title.setContentsMargins(150,0,0,20)

        self.result = QLabel(category_selected)
        self.result.setFont(QFont("Impact",20,200))
        self.result.setWordWrap(True)
        
        self.category_box = QComboBox()
        self.category_box.setFont(QFont("Impact",16,400))
        self.category_box.addItems(
            [
            "animal",
            "career",
            "celebrity",
            "dev",
            "fashion",
            "food",
            "history",
            "money",
            "movie",
            "music",
            "political",
            "religion",
            "science",
            "sport",
            "travel"
            ]
        )

        self.fact_button = QPushButton(
            "get fact"
        )
        self.fact_button.setFont(QFont("Impact",18,400))
        self.fact_button.clicked.connect(self.get_fact)

        #add wigets to layout
        layout.addWidget(title)
        layout.addWidget(self.category_box)
        layout.addWidget(self.fact_button)
        layout.addWidget(self.result)

        #these things come last
        layout.addStretch()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def get_fact(self):
        category = self.category_box.currentText()
        fact = controller.grab_fact(category)

        self.result.setText(fact)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()