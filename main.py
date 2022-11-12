import os
import sys
import webbrowser
import subprocess

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from Interface import Ui_Interface

webbrowser.register('Yandex', None, webbrowser.BackgroundBrowser('C:\\Users\\furys\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe'))


def open_link(self, url):
    webbrowser.get(using='Yandex').open_new_tab(url)


def change_str(str):
    idx = 0
    symbols = ['%', ' ', '?', ',', '#', '$', '^', '@', '/', '&', "'", '`', '+', '=']
    symbols_replace = ['%25', '%20', '%3F', '%2C', '%23', '%24', '%5E', '%40', '%2F', '%26', '%27', '%60', '%2B', '%3D']
    while idx < len(symbols):
        str = str.replace(symbols[idx], symbols_replace[idx])
        idx += 1


class MainPage:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Interface()
        self.ui.setupUi(self.main_win)

        self.ui.XVM.clicked.connect(self.go_to_xvm)
        self.ui.vk.clicked.connect(self.go_to_vk)
        self.ui.ProTanki.clicked.connect(self.go_to_protanki)
        self.ui.Lesta.clicked.connect(self.go_to_lesta)
        self.ui.Tanksgg.clicked.connect(self.go_to_tanksgg)
        self.ui.Wottactics.clicked.connect(self.go_to_wottact)
        self.ui.youtube.clicked.connect(self.go_to_yt)
        self.ui.steam.clicked.connect(self.go_to_steam)
        self.ui.lichess.clicked.connect(self.go_to_lichess)
        self.ui.mosru.clicked.connect(self.go_to_mosru)
        self.ui.calculator.clicked.connect(self.go_to_calc)
        self.ui.gotrans.clicked.connect(self.go_to_trans)
        self.ui.gosearch.clicked.connect(self.go_to_search)
    def show(self):
        self.main_win.show()

    def go_to_xvm(self):
        open_link(self, 'https://stats.modxvm.com/ru/stats/players/132259250')

    def go_to_vk(self):
        open_link(self, 'https://vk.com/im?')

    def go_to_protanki(self):
        open_link(self, 'https://protanki.tv/')

    def go_to_lesta(self):
        open_link(self, 'https://lesta.ru/ru')

    def go_to_tanksgg(self):
        open_link(self, 'https://tanks.gg/list')

    def go_to_wottact(self):
        open_link(self, 'https://ru.wottactic.com/wot2?room=12zroptouBpCB7')

    def go_to_yt(self):
        open_link(self, 'https://www.youtube.com/')

    def go_to_steam(self):
        open_link(self, 'https://steamcommunity.com/market/')

    def go_to_lichess(self):
        open_link(self, 'https://lichess.org/@/XenatanitZ')

    def go_to_mosru(self):
        open_link(self, 'https://www.mos.ru/uslugi/')

    def go_to_calc(self):
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    def go_to_trans(self):
        str = self.ui.transfield.text()
        def match(text, alphabet=None):
            if alphabet is None:
                alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
            return not alphabet.isdisjoint(text.lower())
        change_str(str)
        if match(str):
            link = f"https://translate.yandex.ru/?lang=ru-en&text={str}"
        else:
            link = f"https://translate.yandex.ru/?lang=en-ru&text={str}"
        open_link(self, link)
        print(str)

    def go_to_search(self):
        str = self.ui.searchfield.text()
        change_str(str)
        open_link(self, f"https://yandex.ru/search/?text={str}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainPage()
    main_win.show()

    sys.exit(app.exec_())