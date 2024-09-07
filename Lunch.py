import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from Interface import Ui_MainWindow
import requests
from bs4 import BeautifulSoup

class hesap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("resim.png"))  # Set the window icon
        self.setWindowTitle("Veri Kazıma")  # Set the window title
        self.setToolTip("Devam Et")  # Set a tooltip for the window
        self.ui.pushButton.clicked.connect(self.bilgisayar)  # Connect the "Computer" button
        self.ui.pushButton_2.clicked.connect(self.telefon)  # Connect the "Phone" button

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bilgisayar(self):
        # Determine which radio button is checked and call the corresponding method
        if self.ui.radioButton.isChecked():
            self.vbb()  # Call method for "Vatan Bilgisayar"
        elif self.ui.radioButton_2.isChecked():
            self.ggb()  # Call method for "GittiGidiyor"
    
    def telefon(self):
        # Determine which radio button is checked and call the corresponding method
        if self.ui.radioButton.isChecked():
            self.vbt()  # Call method for "Vatan Bilgisayar"
        elif self.ui.radioButton_2.isChecked():
            self.ggt()  # Call method for "GittiGidiyor"

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def vbb(self):
        # Scrape data from the "Vatan Bilgisayar" laptop page
        url = "https://www.vatanbilgisayar.com/laptop/"
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        li = int(self.ui.lineEdit.text())  # Number of items to retrieve
        veriisim = soup.find("div", {"class": "wrapper-product wrapper-product--list-page clearfix"}).find_all("div", {"class": "product-list__product-name"}, limit=li)
        verifiyat = soup.find("div", {"class": "wrapper-product wrapper-product--list-page clearfix"}).find_all("span", {"class": "product-list__price"}, limit=li)
        self.ui.listWidget.clear()  # Clear the list widget
        self.ui.listWidget_2.clear()  # Clear the price list widget
        sayac1 = 0
        sayac2 = 0
        isim = ""
        fiyat = ""
        for i in veriisim:
            sayac1 += 1
            isim = i.text.strip()
            textisim = str(sayac1) + " : " + isim
            self.ui.listWidget.addItem(textisim)  # Add item name to the list widget
        for j in verifiyat:
            sayac2 += 1
            fiyat = j.text.strip()
            textfiyat = str(sayac2) + " : " + fiyat
            self.ui.listWidget_2.addItem(textfiyat)  # Add item price to the list widget

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def vbt(self):
        # Scrape data from the "Vatan Bilgisayar" phone page
        url = "https://www.vatanbilgisayar.com/cep-telefonu-modelleri/"
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        li = int(self.ui.lineEdit.text())  # Number of items to retrieve
        veriisim = soup.find("div", {"class": "wrapper-product wrapper-product--list-page clearfix"}).find_all("div", {"class": "product-list__product-name"}, limit=li)
        verifiyat = soup.find("div", {"class": "wrapper-product wrapper-product--list-page clearfix"}).find_all("span", {"class": "product-list__price"}, limit=li)
        self.ui.listWidget.clear()  # Clear the list widget
        self.ui.listWidget_2.clear()  # Clear the price list widget
        sayac1 = 0
        sayac2 = 0
        isim = ""
        fiyat = ""
        for i in veriisim:
            sayac1 += 1
            isim = i.text.strip()
            textisim = str(sayac1) + " : " + isim
            self.ui.listWidget.addItem(textisim)  # Add item name to the list widget
        for j in verifiyat:
            sayac2 += 1
            fiyat = j.text.strip()
            textfiyat = str(sayac2) + " : " + fiyat
            self.ui.listWidget_2.addItem(textfiyat)  # Add item price to the list widget

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ggb(self):
        # Scrape data from the "GittiGidiyor" computer page
        url = "https://www.gittigidiyor.com/bilgisayar-tablet/"
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        li = int(self.ui.lineEdit.text())  # Number of items to retrieve
        veriisim = soup.find("div", {"class": "pmyvb0-0 jCCkZh"}).find_all("h3", {"class": "medium"}, limit=li)
        verifiyat = soup.find("div", {"class": "pmyvb0-0 jCCkZh"}).find_all("span", {"class": "buy-price"}, limit=li)
        self.ui.listWidget.clear()  # Clear the list widget
        self.ui.listWidget_2.clear()  # Clear the price list widget
        sayac1 = 0
        sayac2 = 0
        isim = ""
        fiyat = ""
        for i in veriisim:
            sayac1 += 1
            isim = i.text.strip()
            textisim = str(sayac1) + " : " + isim
            self.ui.listWidget.addItem(textisim)  # Add item name to the list widget
        for j in verifiyat:
            sayac2 += 1
            fiyat = j.text.strip()
            textfiyat = str(sayac2) + " : " + fiyat
            self.ui.listWidget_2.addItem(textfiyat)  # Add item price to the list widget

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ggt(self):
        # Scrape data from the "GittiGidiyor" phone page
        url = "https://www.gittigidiyor.com/cep-telefonu/"
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        li = int(self.ui.lineEdit.text())  # Number of items to retrieve
        veriisim = soup.find("div", {"class": "pmyvb0-0 jCCkZh"}).find_all("h3", {"class": "medium"}, limit=li)
        verifiyat = soup.find("div", {"class": "pmyvb0-0 jCCkZh"}).find_all("span", {"class": "buy-price"}, limit=li)
        self.ui.listWidget.clear()  # Clear the list widget
        self.ui.listWidget_2.clear()  # Clear the price list widget
        sayac1 = 0
        sayac2 = 0
        isim = ""
        fiyat = ""
        for i in veriisim:
            sayac1 += 1
            isim = i.text.strip()
            textisim = str(sayac1) + " : " + isim
            self.ui.listWidget.addItem(textisim)  # Add item name to the list widget
        for j in verifiyat:
            sayac2 += 1
            fiyat = j.text.strip()
            textfiyat = str(sayac2) + " : " + fiyat
            self.ui.listWidget_2.addItem(textfiyat)  # Add item price to the list widget

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

deft = QApplication(sys.argv)
penc = hesap()
penc.show()
deft.exec_()
