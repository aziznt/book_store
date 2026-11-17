from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

class BookStore(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,500)
        self.setStyleSheet("font-size: 25px")

        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.year_input = QLineEdit()

        self.title_input.setPlaceholderText("Kitob nomi....")
        self.author_input.setPlaceholderText("Kitob muallifi....")
        self.year_input.setPlaceholderText("Kitob chop etilgan yili....")

        self.save_btn = QPushButton("Saqlash")
        self.save_btn.clicked.connect(self.save_book)

        self.vBox = QVBoxLayout()

        self.vBox.addStretch()
        self.vBox.addWidget(self.title_input)
        self.vBox.addWidget(self.author_input)
        self.vBox.addWidget(self.year_input)
        self.vBox.addSpacing(20)
        self.vBox.addWidget(self.save_btn)
        self.vBox.addStretch()

        self.setLayout(self.vBox)

    def save_book(self):
        title = self.title_input.text().strip().capitalize()
        author = self.author_input.text().strip().title()
        year = int(self.year_input.text().strip())

        book = (title, author, year)
        print(book)

app = QApplication([])
bs = BookStore()
bs.show()
app.exec_()