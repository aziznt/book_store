from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
    QMessageBox
)

from core import *

class AddBook(QWidget):
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
        try:
            year = int(self.year_input.text().strip())
        except:
            QMessageBox.warning(
                self,
                "Xatolik",
                "Iltimos, yilga butun son kiriting"
            )
            return

        if not all([title, author, year]):
            QMessageBox.warning(
                self,
                "Xatolik",
                "Iltimos barcha malumotni kiriting"
            )
            return

        book = (title, author, year)
        add_book(book)
        QMessageBox.information(
            self,
            "Malumot",
            "Yangi kitob qo'shildi"
        )

class ListBooks(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,500)
        self.setStyleSheet("font-size: 25px")   
        books = list_books()
        books_str = ""
        for id, title, author, year in books:
            book = f"{id}. {title} {author} {year}\n"
            books_str += book
        self.books_edit = QTextEdit()
        self.books_edit.setText(books_str)
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.books_edit)

        self.setLayout(self.vBox)

def run():
    app = QApplication([])
    lb = AddBook()
    lb.show()
    app.exec_()


if __name__ == "__main__":  
    run()