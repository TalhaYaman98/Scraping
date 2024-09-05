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
        self.setWindowIcon(QIcon("resim.png"))
        self.setWindowTitle("Veri Kazıma")
        self.setToolTip("Devam Et")
        self.ui.pushButton.clicked.connect(self.bilgisayar)
        self.ui.pushButton_2.clicked.connect(self.telefon)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def bilgisayar(self):
        if self.ui.radioButton.isChecked():
            self.vbb()
        elif self.ui.radioButton_2.isChecked():
            self.ggb()
    def telefon(self):
        if self.ui.radioButton.isChecked():
            self.vbt()
        elif self.ui.radioButton_2.isChecked():
            self.ggt()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def vbb(self):
        url = "https://www.vatanbilgisayar.com/laptop/"
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        li = int(self.ui.lineEdit.text())
        veriisim = soup.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"}).find_all("div",{"class":"product-list__product-name"},limit=li)
        verifiyat = soup.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"}).find_all("span",{"class":"product-list__price"},limit=li)
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        sayac1=0
        sayac2=0
        isim = ""
        fiyat = ""
        for i in veriisim:
            sayac1 += 1
            isim = i.text.strip()
            textisim = str(sayac1) + " : " + isim
            self.ui.listWidget.addItem(textisim)
        for j in verifiyat:
            sayac2 += 1
            fiyat = j.text.strip()
            textfiyat = str(sayac2) + " : " + fiyat
            self.ui.listWidget_2.addItem(textfiyat)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def vbt(self):
        url = "https://www.vatanbilgisayar.com/cep-telefonu-modelleri/"
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        li = int(self.ui.lineEdit.text())
        veriisim = soup.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"}).find_all("div",{"class":"product-list__product-name"},limit=li)
        verifiyat = soup.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"}).find_all("span",{"class":"product-list__price"},limit=li)
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        sayac1=0
        sayac2=0
        isim = ""
        fiyat = ""
        for i in veriisim:
            sayac1 += 1
            isim = i.text.strip()
            textisim = str(sayac1) + " : " + isim
            self.ui.listWidget.addItem(textisim)
        for j in verifiyat:
            sayac2 += 1
            fiyat = j.text.strip()
            textfiyat = str(sayac2) + " : " + fiyat
            self.ui.listWidget_2.addItem(textfiyat)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ggb(self):
        url = "https://www.gittigidiyor.com/bilgisayar-tablet/"
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        li = int(self.ui.lineEdit.text())
        veriisim = soup.find("div",{"class":"pmyvb0-0 jCCkZh"}).find_all("h3",{"class":"medium"},limit=li)
        verifiyat = soup.find("div",{"class":"pmyvb0-0 jCCkZh"}).find_all("span",{"class":"buy-price"},limit=li)
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        sayac1=0
        sayac2=0
        isim = ""
        fiyat = ""
        for i in veriisim:
            sayac1 += 1
            isim = i.text.strip()
            textisim = str(sayac1) + " : " + isim
            self.ui.listWidget.addItem(textisim)
        for j in verifiyat:
            sayac2 += 1
            fiyat = j.text.strip()
            textfiyat = str(sayac2) + " : " + fiyat
            self.ui.listWidget_2.addItem(textfiyat)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ggt(self):
        url = "https://www.gittigidiyor.com/cep-telefonu/"
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        li = int(self.ui.lineEdit.text())
        veriisim = soup.find("div",{"class":"pmyvb0-0 jCCkZh"}).find_all("h3",{"class":"medium"},limit=li)
        verifiyat = soup.find("div",{"class":"pmyvb0-0 jCCkZh"}).find_all("span",{"class":"buy-price"},limit=li)
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        sayac1=0
        sayac2=0
        isim = ""
        fiyat = ""
        for i in veriisim:
            sayac1 += 1
            isim = i.text.strip()
            textisim = str(sayac1) + " : " + isim
            self.ui.listWidget.addItem(textisim)
        for j in verifiyat:
            sayac2 += 1
            fiyat = j.text.strip()
            textfiyat = str(sayac2) + " : " + fiyat
            self.ui.listWidget_2.addItem(textfiyat)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

deft=QApplication(sys.argv)
penc=hesap()
penc.show()
deft.exec_()