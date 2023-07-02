#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class HarmonicSeries(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Harmonik Seri Toplamı")
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Sayı Giriniz:"),1,0)
        
        self.sayi = QLineEdit()
        grid.addWidget(self.sayi,1,1,1,2)
        
        self.buton = QPushButton("Hesapla")
        self.buton.clicked.connect(self.hesapla)
        grid.addWidget(self.buton,2,2,1,1)
        
        self.sonuc = QLabel("")
        
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(grid)
        v_box.addStretch()
        
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        
        v_box.addWidget(self.sonuc)
        
        self.resize(300,300)
        self.setLayout(h_box)
        self.show()
        
    def hesapla(self):
        sayi = 0
        try: sayi = int(self.sayi.text())
        except: pass
        
        sonuc = 0
        i = 1
        if(sayi > 0):
            while(i <= sayi):
                sonuc += 1/i
                i += 1
            sonuc = round(sonuc,2)
            self.sonuc.setText("Harmonik serinin toplamı: {}".format(sonuc))
            
        elif(sayi == 0):
            self.sonuc.setText("1/0 Tanımsızdır.")
        else:
            self.sonuc.setText("Lütfen pozitif sayı giriniz.")
uygulama = QApplication(sys.argv)
pencere = HarmonicSeries()
sys.exit(uygulama.exec_())


# In[ ]:




