# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disrJQnZe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_life(object):
    def setupUi(self, life):
        if not life.objectName():
            life.setObjectName(u"life")
        life.resize(225, 116)
        self.display = QLCDNumber(life)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(0, 0, 221, 111))

        self.retranslateUi(life)

        QMetaObject.connectSlotsByName(life)
    # setupUi

    def retranslateUi(self, life):
        life.setWindowTitle(QCoreApplication.translate("life", u"Form", None))
    # retranslateUi

