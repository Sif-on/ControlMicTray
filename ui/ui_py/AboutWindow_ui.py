# Form implementation generated from reading ui file 'ui/ui_py/AboutWindow.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        AboutWindow.resize(355, 290)
        AboutWindow.setMinimumSize(QtCore.QSize(355, 290))
        AboutWindow.setMaximumSize(QtCore.QSize(355, 290))
        font = QtGui.QFont()
        font.setPointSize(-1)
        AboutWindow.setFont(font)
        AboutWindow.setStyleSheet("QWidget {\n"
"    color: #BECBD1;\n"
"    background-color: #273238;\n"
"    border: 0;\n"
"    font-size:14px;\n"
"}")
        self.WebSiteLabel = QtWidgets.QLabel(AboutWindow)
        self.WebSiteLabel.setGeometry(QtCore.QRect(20, 70, 100, 16))
        self.WebSiteLabel.setObjectName("WebSiteLabel")
        self.ProgramVersionLabel = QtWidgets.QLabel(AboutWindow)
        self.ProgramVersionLabel.setGeometry(QtCore.QRect(20, 30, 100, 16))
        self.ProgramVersionLabel.setObjectName("ProgramVersionLabel")
        self.EmailLabel = QtWidgets.QLabel(AboutWindow)
        self.EmailLabel.setGeometry(QtCore.QRect(20, 110, 100, 16))
        self.EmailLabel.setObjectName("EmailLabel")
        self.ProgramVersion = QtWidgets.QLabel(AboutWindow)
        self.ProgramVersion.setGeometry(QtCore.QRect(140, 30, 130, 16))
        self.ProgramVersion.setObjectName("ProgramVersion")
        self.Logo = QtWidgets.QLabel(AboutWindow)
        self.Logo.setGeometry(QtCore.QRect(271, 20, 64, 64))
        self.Logo.setStyleSheet("")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("ui/ui_py\\../resources/Frame.svg"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.UrlPrivacyPolicy = QtWidgets.QPushButton(AboutWindow)
        self.UrlPrivacyPolicy.setGeometry(QtCore.QRect(53, 184, 250, 30))
        self.UrlPrivacyPolicy.setStyleSheet("QPushButton {\n"
"    color: #7D8A90;\n"
"    border-bottom: 1px solid #1F2A30;\n"
"}\n"
"QPushButton::hover {\n"
"    color: #CEDCDF;\n"
"    border-bottom: 1px solid #04BED5;\n"
"}")
        self.UrlPrivacyPolicy.setObjectName("UrlPrivacyPolicy")
        self.Copyright = QtWidgets.QLabel(AboutWindow)
        self.Copyright.setGeometry(QtCore.QRect(78, 224, 200, 40))
        self.Copyright.setStyleSheet("QLabel{\n"
"    color: #7D8A90;\n"
"    font-size:10px;\n"
"}")
        self.Copyright.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Copyright.setObjectName("Copyright")
        self.WebSite = QtWidgets.QPushButton(AboutWindow)
        self.WebSite.setGeometry(QtCore.QRect(140, 70, 130, 16))
        self.WebSite.setStyleSheet("QPushButton {\n"
"    color: #127D91;\n"
"    text-align: left;\n"
"}\n"
"QPushButton::hover {\n"
"    color: #04BED5;\n"
"}")
        self.WebSite.setObjectName("WebSite")
        self.Email = QtWidgets.QPushButton(AboutWindow)
        self.Email.setGeometry(QtCore.QRect(140, 110, 190, 16))
        self.Email.setStyleSheet("QPushButton {\n"
"    color: #127D91;\n"
"    text-align: left;\n"
"}\n"
"QPushButton::hover {\n"
"    color: #04BED5;\n"
"}")
        self.Email.setObjectName("Email")
        self.LogoFrame = QtWidgets.QLabel(AboutWindow)
        self.LogoFrame.setGeometry(QtCore.QRect(277, 26, 52, 52))
        self.LogoFrame.setStyleSheet("QLabel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.LogoFrame.setText("")
        self.LogoFrame.setPixmap(QtGui.QPixmap("ui/ui_py\\../resources/Microphone.svg"))
        self.LogoFrame.setScaledContents(True)
        self.LogoFrame.setObjectName("LogoFrame")

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "О программе"))
        self.WebSiteLabel.setText(_translate("AboutWindow", "Веб-сайт"))
        self.ProgramVersionLabel.setText(_translate("AboutWindow", "Версия"))
        self.EmailLabel.setText(_translate("AboutWindow", "Поддержка"))
        self.ProgramVersion.setText(_translate("AboutWindow", "2022.02.12"))
        self.UrlPrivacyPolicy.setText(_translate("AboutWindow", "Политика конфиденциальности"))
        self.Copyright.setText(_translate("AboutWindow", "Copyright © 2022\n"
"Simonovskiy & Lastivka\n"
"All rights reserved"))
        self.WebSite.setText(_translate("AboutWindow", "controlmictray.pp.ua"))
        self.Email.setText(_translate("AboutWindow", "info@controlmictray.pp.ua "))
