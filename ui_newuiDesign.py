# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newuiDesignhdFdzy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(802, 496)
        MainWindow.setMinimumSize(QSize(802, 496))
        MainWindow.setMaximumSize(QSize(914, 613))
        MainWindow.setStyleSheet(u"border-radius:20px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-radius:20px;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BaseFrame = QFrame(self.centralwidget)
        self.BaseFrame.setObjectName(u"BaseFrame")
        self.BaseFrame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius:12px;")
        self.BaseFrame.setFrameShape(QFrame.StyledPanel)
        self.BaseFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.BaseFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar_2 = QFrame(self.BaseFrame)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 22))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"\n"
"	border-image:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	background-color: qlineargradient(spread:pad, x1:0.506, y1:0, x2:0.488, y2:0.556818, stop:0 rgba(0, 0, 0, 255), stop:0.363636 rgba(132, 132, 132, 123), stop:0.619318 rgba(165, 165, 165, 90), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius:12px;\n"
"\n"
"\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.TopDragFrame = QFrame(self.TitleBar_2)
        self.TopDragFrame.setObjectName(u"TopDragFrame")
        self.TopDragFrame.setCursor(QCursor(Qt.SizeAllCursor))
        self.TopDragFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.TopDragFrame.setFrameShape(QFrame.StyledPanel)
        self.TopDragFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.TopDragFrame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.TopDragFrame)

        self.frame_3 = QFrame(self.TitleBar_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 25))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(u"border-image:none;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.Minimizebtn = QPushButton(self.frame_3)
        self.Minimizebtn.setObjectName(u"Minimizebtn")
        sizePolicy1.setHeightForWidth(self.Minimizebtn.sizePolicy().hasHeightForWidth())
        self.Minimizebtn.setSizePolicy(sizePolicy1)
        self.Minimizebtn.setMaximumSize(QSize(14, 14))
        self.Minimizebtn.setToolTipDuration(-1)
        self.Minimizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:7px;\n"
"	\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.Minimizebtn)

        self.Maximizebtn = QPushButton(self.frame_3)
        self.Maximizebtn.setObjectName(u"Maximizebtn")
        sizePolicy1.setHeightForWidth(self.Maximizebtn.sizePolicy().hasHeightForWidth())
        self.Maximizebtn.setSizePolicy(sizePolicy1)
        self.Maximizebtn.setMaximumSize(QSize(14, 14))
        self.Maximizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Maximizebtn)

        self.CloseButton = QPushButton(self.frame_3)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy1.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy1)
        self.CloseButton.setMaximumSize(QSize(14, 14))
        self.CloseButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.CloseButton)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.TitleBar_2)

        self.ContentFrame = QFrame(self.BaseFrame)
        self.ContentFrame.setObjectName(u"ContentFrame")
        self.ContentFrame.setStyleSheet(u"border-radius:0px;\n"
"border-bottom-right-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-right-radius:20px;\n"
"\n"
"\n"
"border-image: url(:/newPrefix/photo-1567095751004-aa51a2690368.jpeg);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 198), stop:1 rgba(255, 255, 255, 0));")
        self.ContentFrame.setFrameShape(QFrame.StyledPanel)
        self.ContentFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ContentFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftContent = QFrame(self.ContentFrame)
        self.LeftContent.setObjectName(u"LeftContent")
        self.LeftContent.setStyleSheet(u"background-color: rgb(162, 162, 162);\n"
"\n"
"border-image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.LeftContent.setFrameShape(QFrame.StyledPanel)
        self.LeftContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.LeftContent)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.InnerContentBase = QFrame(self.LeftContent)
        self.InnerContentBase.setObjectName(u"InnerContentBase")
        self.InnerContentBase.setMinimumSize(QSize(311, 441))
        self.InnerContentBase.setMaximumSize(QSize(311, 441))
        self.InnerContentBase.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(31, 31, 31);\n"
"border-radius:0px;\n"
"border-bottom-left-radius:50px;\n"
"border-top-left-radius:50px;\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}")
        self.InnerContentBase.setFrameShape(QFrame.StyledPanel)
        self.InnerContentBase.setFrameShadow(QFrame.Raised)
        self.userAccountFrame = QFrame(self.InnerContentBase)
        self.userAccountFrame.setObjectName(u"userAccountFrame")
        self.userAccountFrame.setGeometry(QRect(10, 10, 291, 79))
        self.userAccountFrame.setStyleSheet(u"background-image:none;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.126, y2:0.863636, stop:0 rgba(35, 32, 38, 152), stop:1 rgba(18, 0, 27, 232));\n"
"border-radius:0px;\n"
"border-bottom-right-radius:50px;\n"
"border-top-left-radius:50px;\n"
"")
        self.userAccountFrame.setFrameShape(QFrame.StyledPanel)
        self.userAccountFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.userAccountFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AccountButton = QPushButton(self.userAccountFrame)
        self.AccountButton.setObjectName(u"AccountButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AccountButton.sizePolicy().hasHeightForWidth())
        self.AccountButton.setSizePolicy(sizePolicy2)
        self.AccountButton.setMinimumSize(QSize(71, 61))
        self.AccountButton.setMaximumSize(QSize(71, 61))
        self.AccountButton.setStyleSheet(u"QPushButton{\n"
"/*  border-bottom-right-radius:49px; */\n"
"/* border-top-left-radius:49px; */\n"
"\n"
"border-top-right-radius:0px;\n"
"border-top-left-radius:30px;\n"
"\n"
"border-bottom-right-radius:30px;\n"
"border-bottom-left-radius:0px;\n"
"\n"
"	background-color: rgb(19, 20, 26);\n"
"border-style:inset;\n"
"border-width:1px;\n"
"	border-color: rgb(255, 170, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"	border-right-color: rgb(247, 173, 24);\n"
"	border-right-color: rgb(255, 170, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(31, 32, 39,225);\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/preferences-desktop-user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AccountButton.setIcon(icon)
        self.AccountButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.AccountButton)

        self.userAccountFrame_2 = QFrame(self.InnerContentBase)
        self.userAccountFrame_2.setObjectName(u"userAccountFrame_2")
        self.userAccountFrame_2.setGeometry(QRect(10, 100, 281, 321))
        self.userAccountFrame_2.setStyleSheet(u"background-color: rgb(134, 134, 134);\n"
"\n"
"border-radius:0px;\n"
"border-bottom-left-radius:50px;\n"
"border-top-right-radius:50px;\n"
"\n"
"border-width:2px;\n"
"border-style:inset;\n"
"border-color: rgb(255, 170, 0);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.537, y1:1, x2:0.532, y2:0, stop:0 rgba(0, 0, 0, 178), stop:1 rgba(255, 255, 255, 0));")
        self.userAccountFrame_2.setFrameShape(QFrame.StyledPanel)
        self.userAccountFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.userAccountFrame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 9, -1)
        self.ButtonsFrame = QFrame(self.userAccountFrame_2)
        self.ButtonsFrame.setObjectName(u"ButtonsFrame")
        self.ButtonsFrame.setStyleSheet(u"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 198), stop:1 rgba(255, 255, 255, 0));")
        self.ButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ButtonsFrame)
        self.verticalLayout_3.setSpacing(18)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 14, 12, -1)
        self.ChangeEmailBtn = QPushButton(self.ButtonsFrame)
        self.ChangeEmailBtn.setObjectName(u"ChangeEmailBtn")
        self.ChangeEmailBtn.setMinimumSize(QSize(181, 41))
        font = QFont()
        font.setFamily(u"NotoSerifTamilSlanted Medium")
        font.setPointSize(10)
        self.ChangeEmailBtn.setFont(font)
        self.ChangeEmailBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(234, 234, 234);\n"
"	background-color: rgb(29, 25, 29);\n"
"background-image:none;\n"
"border-radius:0px;\n"
"\n"
"border-radius:20px;\n"
"border-top-left-radius:0px;\n"
"\n"
"\n"
"border-width:2px;\n"
"border-style:inset;\n"
"border-color: rgb(255, 170, 0);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.ChangeEmailBtn)

        self.ClearSavedData = QPushButton(self.ButtonsFrame)
        self.ClearSavedData.setObjectName(u"ClearSavedData")
        self.ClearSavedData.setMinimumSize(QSize(181, 41))
        self.ClearSavedData.setFont(font)
        self.ClearSavedData.setStyleSheet(u"QPushButton{\n"
"	color: rgb(234, 234, 234);\n"
"	background-color: rgb(29, 25, 29);\n"
"background-image:none;\n"
"border-radius:0px;\n"
"\n"
"border-radius:20px;\n"
"border-top-right-radius:0px;\n"
"\n"
"\n"
"\n"
"border-width:2px;\n"
"border-style:inset;\n"
"border-color: rgb(255, 170, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.ClearSavedData)

        self.ContactDeveloperBtn = QPushButton(self.ButtonsFrame)
        self.ContactDeveloperBtn.setObjectName(u"ContactDeveloperBtn")
        self.ContactDeveloperBtn.setMinimumSize(QSize(181, 41))
        self.ContactDeveloperBtn.setFont(font)
        self.ContactDeveloperBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(234, 234, 234);\n"
"	background-color: rgb(29, 25, 29);\n"
"background-image:none;\n"
"border-radius:0px;\n"
"\n"
"border-radius:20px;\n"
"border-bottom-left-radius:0px;\n"
"\n"
"\n"
"\n"
"border-width:2px;\n"
"border-style:inset;\n"
"border-color: rgb(255, 170, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.ContactDeveloperBtn)

        self.paddingframe = QFrame(self.ButtonsFrame)
        self.paddingframe.setObjectName(u"paddingframe")
        self.paddingframe.setStyleSheet(u"background-image:none;\n"
"border:none;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.paddingframe.setFrameShape(QFrame.StyledPanel)
        self.paddingframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.paddingframe)


        self.verticalLayout_4.addWidget(self.ButtonsFrame)


        self.verticalLayout_5.addWidget(self.InnerContentBase)


        self.horizontalLayout_2.addWidget(self.LeftContent)

        self.frame_4 = QFrame(self.ContentFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border-image:none;\n"
"background-color: rgb(162, 162, 162);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 31, -1, 8)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"image: url(:/newPrefix/1370307-middle.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(141, 141, 141);\n"
"background-color: none;\n"
"\n"
"color: qlineargradient(spread:pad, x1:0, y1:0.659, x2:1, y2:0.688, stop:0 rgba(195, 65, 195, 255), stop:1 rgba(255, 85, 85, 255));")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label)

        self.ContactDeveloperBtn_2 = QPushButton(self.frame_4)
        self.ContactDeveloperBtn_2.setObjectName(u"ContactDeveloperBtn_2")
        self.ContactDeveloperBtn_2.setMinimumSize(QSize(181, 41))
        font2 = QFont()
        font2.setFamily(u"octicons")
        font2.setPointSize(12)
        self.ContactDeveloperBtn_2.setFont(font2)
        self.ContactDeveloperBtn_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(234, 234, 234);\n"
"	background-color: rgb(29, 25, 29);\n"
"background-image:none;\n"
"border-radius:0px;\n"
"\n"
"border-radius:20px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"\n"
"\n"
"border-width:2px;\n"
"border-style:inset;\n"
"border-color: rgb(255, 170, 0);\n"
"	background-color: rgba(255, 85, 0,150);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 85, 0,50);\n"
"\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"\n"
"background-color: rgba(255, 85, 0,50);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.ContactDeveloperBtn_2)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.ContentFrame)

        self.BottomMarginFrame = QFrame(self.BaseFrame)
        self.BottomMarginFrame.setObjectName(u"BottomMarginFrame")
        sizePolicy.setHeightForWidth(self.BottomMarginFrame.sizePolicy().hasHeightForWidth())
        self.BottomMarginFrame.setSizePolicy(sizePolicy)
        self.BottomMarginFrame.setMinimumSize(QSize(0, 18))
        self.BottomMarginFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(24, 25, 33);\n"
"}")
        self.BottomMarginFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomMarginFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.BottomMarginFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BottomDrag = QFrame(self.BottomMarginFrame)
        self.BottomDrag.setObjectName(u"BottomDrag")
        self.BottomDrag.setStyleSheet(u"background-color: rgb(85, 255, 255);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.BottomDrag.setFrameShape(QFrame.StyledPanel)
        self.BottomDrag.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.BottomDrag)

        self.QSizeGrip_botto_right = QFrame(self.BottomMarginFrame)
        self.QSizeGrip_botto_right.setObjectName(u"QSizeGrip_botto_right")
        sizePolicy1.setHeightForWidth(self.QSizeGrip_botto_right.sizePolicy().hasHeightForWidth())
        self.QSizeGrip_botto_right.setSizePolicy(sizePolicy1)
        self.QSizeGrip_botto_right.setMinimumSize(QSize(22, 18))
        self.QSizeGrip_botto_right.setCursor(QCursor(Qt.ArrowCursor))
        self.QSizeGrip_botto_right.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"image: url(:/newPrefix/Utility Icons/arrow-down-right.svg);\n"
"background-color: rgb(24, 25, 33);")
        self.QSizeGrip_botto_right.setFrameShape(QFrame.StyledPanel)
        self.QSizeGrip_botto_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.QSizeGrip_botto_right)


        self.verticalLayout.addWidget(self.BottomMarginFrame)


        self.horizontalLayout.addWidget(self.BaseFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Minimizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Minimize</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.Maximizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Maximize</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Close</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CloseButton.setText("")
        self.AccountButton.setText("")
        self.ChangeEmailBtn.setText(QCoreApplication.translate("MainWindow", u"Change Email / Password", None))
        self.ClearSavedData.setText(QCoreApplication.translate("MainWindow", u"Clear Saved Data", None))
        self.ContactDeveloperBtn.setText(QCoreApplication.translate("MainWindow", u"Contact Developer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff557f;\">M</span><span style=\" color:#ff557f;\">eeting</span><span style=\" font-weight:600; color:#ff557f;\"> J</span><span style=\" color:#ff557f;\">oiner</span></p></body></html>", None))
        self.ContactDeveloperBtn_2.setText(QCoreApplication.translate("MainWindow", u"Join Meeting", None))
    # retranslateUi

