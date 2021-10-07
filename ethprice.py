import requests
import PySide2
from PySide2.QtWidgets import QApplication, QMessageBox,QTextBrowser,QMainWindow,QWidget
from PySide2.QtCore import QTimer,QDateTime,QDate,QObject,Signal
from PySide2.QtUiTools import QUiLoader
import time
from threading import Thread
from ui_dis import Ui_life

class Eth(QWidget):
    def __init__(self):
        # self.ui = QUiLoader().load('dis.ui')
        super(Eth, self).__init__()
        self.ui = Ui_life()
        self.ui.setupUi(self)
        self.ui.display.setDigitCount(7)
        self.ui.display.display(0000.00)
    def realprice(self):
        url = 'https://api.huobi.pro/market/trade?symbol=ethusdt'
        proxy = {"http": "http://127.0.0.1:889",
                 "https": "https://127.0.0.1:889"}
        response = requests.get(url, proxies=proxy)
        text = eval(response.text)
        ts = text['ts']
        price = text['tick']['data'][0]['price']
        # print(price)
        return price
    def dis(self):
        while True:
            self.ui.display.display(self.realprice())
            time.sleep(1)
    def main(self):
        thread=Thread(target=self.dis)
        thread.start()
app = QApplication([])
eth = Eth()
eth.show()
eth.main()
app.exec_()