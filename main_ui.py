# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'com_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(825, 631)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.frame = QFrame(self.Home)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(10, 10, 781, 291))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 241, 21))
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 50, 761, 71))
        self.frame_7.setFrameShape(QFrame.Shape.Box)
        self.frame_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.checkBox = QCheckBox(self.frame_7)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 20, 171, 31))
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setIconSize(QSize(20, 20))
        self.checkBox.setChecked(False)
        self.checkBox_2 = QCheckBox(self.frame_7)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(300, 20, 171, 31))
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setIconSize(QSize(20, 20))
        self.checkBox_2.setChecked(False)
        self.checkBox_3 = QCheckBox(self.frame_7)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(570, 20, 171, 31))
        self.checkBox_3.setAutoFillBackground(False)
        self.checkBox_3.setIconSize(QSize(20, 20))
        self.checkBox_3.setChecked(False)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 130, 761, 71))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 250, 741, 31))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setFrameShape(QFrame.Shape.WinPanel)
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 230, 81, 16))
        self.label_17.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_2 = QFrame(self.Home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 309, 781, 241))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 61, 21))
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 40, 761, 191))
        self.frame_6.setFrameShape(QFrame.Shape.Panel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 10, 81, 16))
        self.label_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 70, 191, 31))
        self.label_7.setFrameShape(QFrame.Shape.Box)
        self.label_7.setLineWidth(4)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 10, 141, 20))
        self.label_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 70, 191, 31))
        self.label_8.setFrameShape(QFrame.Shape.Box)
        self.label_8.setLineWidth(4)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 10, 91, 16))
        self.label_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 70, 191, 31))
        self.label_9.setFrameShape(QFrame.Shape.Box)
        self.label_9.setLineWidth(4)

        self.horizontalLayout.addWidget(self.frame_5)

        self.tabWidget.addTab(self.Home, "")
        self.Settingss = QWidget()
        self.Settingss.setObjectName(u"Settingss")
        self.frame_8 = QFrame(self.Settingss)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 50, 771, 198))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_8)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer = QSpacerItem(661, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(2, QFormLayout.ItemRole.FieldRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(661, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(9, QFormLayout.ItemRole.FieldRole, self.verticalSpacer_2)

        self.textEdit_3 = QTextEdit(self.frame_8)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setAutoFillBackground(True)
        self.textEdit_3.setFrameShape(QFrame.Shape.Box)
        self.textEdit_3.setLineWidth(4)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.textEdit_3)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.textEdit = QTextEdit(self.frame_8)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setFrameShape(QFrame.Shape.Box)
        self.textEdit.setLineWidth(4)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.textEdit)

        self.textEdit_2 = QTextEdit(self.frame_8)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setAutoFillBackground(True)
        self.textEdit_2.setFrameShape(QFrame.Shape.Box)
        self.textEdit_2.setLineWidth(4)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.textEdit_2)

        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.label_16 = QLabel(self.Settingss)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 20, 241, 21))
        self.pushButton_2 = QPushButton(self.Settingss)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(310, 260, 181, 41))
        self.pushButton_3 = QPushButton(self.Settingss)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(600, 10, 171, 31))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentPrintPreview))
        self.pushButton_3.setIcon(icon)
        self.tabWidget.addTab(self.Settingss, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; text-decoration: underline;\">Select List of Comports to Find</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"RF Generator", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Analog Interface Hub", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Vacuum Gauge", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"FIND DEVICES ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Notifier</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; text-decoration: underline;\">Results</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">RF Generator</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Analog Interface Hub</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Vacuum Gauge</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">RF Generator :</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">RF Generator :</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">RF Generator :</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Settings</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Read ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settingss), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

