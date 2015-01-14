#!/usr/bin/env python
# coding=utf-8

from __future__ import unicode_literals, print_function

from io import open
import os
import sys
import time
import random
import traceback
import os.path

from PySide.QtGui import QApplication
from PySide.QtGui import QMainWindow, QMessageBox
from PySide.QtCore import QSettings

from ui_mainwindow import Ui_MainWindow

# ----------------------------------------------------------------------------------------------------------------------

if getattr(sys, "frozen", False):
    # frozen
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # unfrozen
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# ----------------------------------------------------------------------------------------------------------------------

QUOTE_FILE_NAME = "citaty.txt"

DEFAULT_QUOTES = [
    "Dělej to, co se obáváš dělat. (Aristotelés)",
    "Ne každý kdo bloudí je ztracený. (J.R.R. Tolkien)",
    "Co je důležité je očím neviditelné. (Antoine de Saint-Exupéry)"
]

TEMPLATE = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Georgia'; font-size:12pt; font-weight:400; font-style:italic;">
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<br />%s</p></body></html>
"""


def touch(path):
    with open(path, "a", encoding="utf-8-sig") as fp:
        if fp.tell() == 0:
            for quote in DEFAULT_QUOTES:
                print(quote, file=fp)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.settings = QSettings("citaty", "citaty")

        self.button.clicked.connect(self.showQuote)
        self.label.linkActivated.connect(self.editQuotes)
        self.textEdit.setText("")

        try:
            self.quotes = self.readQuoteFile()
        except Exception as exc:
            QMessageBox.critical(self, "Chyba", traceback.format_exc(exc))

        self.label.setText(self.label.text() % len(self.quotes))
        random.seed(self.seed)
        random.shuffle(self.quotes)

    @property
    def i(self): return int(self.settings.value("i", 0))

    @i.setter
    def i(self, x): self.settings.setValue("i", x)

    @property
    def seed(self): return float(self.settings.value("seed", time.time()))

    @seed.setter
    def seed(self, x): self.settings.setValue("seed", x)

    def readQuoteFile(self):
        touch(self.getQuoteFilePath())
        with open(self.getQuoteFilePath(), encoding="utf-8-sig") as fp:
            return [line.strip() for line in fp if line and not line.isspace()]

    def getQuoteFilePath(self):
        return os.path.join(BASE_DIR, QUOTE_FILE_NAME)

    def editQuotes(self):
        touch(self.getQuoteFilePath())
        os.system(self.getQuoteFilePath())

    def showQuote(self):
        if not self.quotes:
            QMessageBox.warning(self, "Žádné citáty", "Soubor s citáty je prázdný!\n\n" + self.getQuoteFilePath())
            return

        if self.i >= len(self.quotes):
            self.i = 0
            self.seed = time.time()
            random.seed(self.seed)
            random.shuffle(self.quotes)

        quote = self.quotes[self.i]
        self.textEdit.setText(TEMPLATE % quote)
        self.i += 1

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
