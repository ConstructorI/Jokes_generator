import sys
import numpy as np

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PySide6.QtSql import QSqlTableModel

from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.main_action()

    def main_action(self):
        self.ui_main.pushButton_4.clicked.connect(lambda: self.gen())

    def make_pairs(self, corp):
        for i in range(len(corp) - 1):
            yield (corp[i], corp[i + 1])

    def gen(self):
        what_to_open = str(self.ui_main.lineEdit.text())
        text = open(what_to_open, encoding='utf-8').read()

        corpus = text.split()
        pairs = self.make_pairs(corpus)
        word_dict = {}
        for word_1, word_2 in pairs:
            if word_1 in word_dict.keys():
                word_dict[word_1].append(word_2)
            else:
                word_dict[word_1] = [word_2]
        first_word = np.random.choice(corpus)

        while first_word.islower() or first_word == '—' or first_word == '-':
            first_word = np.random.choice(corpus)
        chain = [first_word]
        n_words = int(self.ui_main.spinBox.text()) - 1
        for y in range(n_words):
            try:
                chain.append(np.random.choice(word_dict[chain[-1]]))
            except KeyError:
                pass
        prt = ' '.join(chain)

        self.ui_main.plainTextEdit_4.clear()
        self.ui_main.plainTextEdit_4.insertPlainText(prt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
