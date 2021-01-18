# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Stego_mainhbavDv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import img_rc
import img_rc
import img_rc

class Ui_Stego_main(object):
    def MSGIF(self):
        self.MSMovie = QMovie("Hide_under_MS_office.gif")
        self.MSOfficeGIF.setMovie(self.MSMovie)
        self.MSMovie.start()

    def HIDEADSGIF(self):
        pass

    def HIDINWINRGif(self):
        pass

    def HIdeINHtml(self):
        self.HTMLGIFF = QMovie("HTML.gif")
        self.HTMLGIF.setMovie(self.HTMLGIFF)
        self.HTMLGIFF.start()
    def setupUi(self, Stego_main):
        if not Stego_main.objectName():
            Stego_main.setObjectName(u"Stego_main")
        Stego_main.resize(1122, 700)
        Stego_main.setMinimumSize(QSize(1000, 700))
        Stego_main.setStyleSheet(u"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
""
                        "    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:chec"
                        "ked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
""
                        "    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
" "
                        " border: none;\n"
"  outline: none;\n"
"    image: url(:/dark_blue/img/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/dark_blue/img/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bot"
                        "tom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 2px 2px 25px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"Q"
                        "Menu::indicator:non-exclusive:checked {\n"
"    image: url(:/dark_blue/img/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/dark_blue/img/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/dark_blue/img/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/dark_blue/img/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAb"
                        "stractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border:"
                        " 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
""
                        "{\n"
"    border-image: url(:/dark_blue/img/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
""
                        "\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/dark_blue/img/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/dark_blue/img/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"   "
                        " subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/dark_blue/img/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background-color: #302F2F;\n"
"\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    s"
                        "pacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    background-color: #302F2F;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/dark_blue/img/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vert"
                        "ical {\n"
"    image: url(:/dark_blue/img/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/dark_blue/img/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/dark_blue/img/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 4px;\n"
"    /* outline: none; */\n"
"    /* min-width: 40px; */\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color"
                        ": #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background"
                        "-color: #3d8ec9;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparen"
                        "t;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
""
                        "}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/dark_blue/img/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/dark_blue/img/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/dark_blue/img/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
""
                        "    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
""
                        "    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px "
                        "transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/dark_blue/img/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/dark_blue/img/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/dark_blue/img/close.png);\n"
"    titlebar-normal-icon: url(:/dark_blue/img/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius"
                        ": 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
"    border: 1px solid #444;\n"
"    background-color: silver;\n"
"    border-radius: 3px;\n"
"    margin-left: 3px;\n"
"    color: black;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"    background: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: "
                        "url(:/dark_blue/img/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/dark_blue/img/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/dark_blue/img/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/dark_blue/img/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/dark_blue/img/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:ho"
                        "ver, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height"
                        ": 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    /*  background-color: transparent; */\n"
"    border: 2px transparent #4A4949;\n"
"    border-radius: 4px;\n"
"    background-color: dimgray;\n"
"    margin: 2px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
" border-radius: 4px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 2px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"    QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 2px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mo"
                        "de */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 4px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHea"
                        "derView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::"
                        "only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/dark_blue/img/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/dark_blue/img/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tab"
                        "s */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #AAA;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: silver;\n"
"    border-radius: 5px;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: black;\n"
"}\n"
"\n"
"QMessageBox {\n"
"    messagebox-critical-icon	: url(:/dark_blue/img/critical.png);\n"
"    messagebox-information-icon	: url(:/dark_blue/img/information.png);\n"
"    messagebox-question-icon	: url(:/dark_blue/img/question.png);\n"
""
                        "    messagebox-warning-icon:    : url(:/dark_blue/img/warning.png);\n"
"}\n"
"\n"
"ColorButton::enabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"ColorButton::disabled {\n"
"    border-radius: 0px;\n"
"    border: 1px solid #AAAAAA;\n"
"}")
        self.centralwidget = QWidget(Stego_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_left_menu = QFrame(self.centralwidget)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setEnabled(True)
        self.frame_left_menu.setGeometry(QRect(5, 5, 91, 687))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMaximumSize(QSize(100, 16777215))
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(7, 7, 7, 7)
        self.Home_BTN = QPushButton(self.frame_left_menu)
        self.Home_BTN.setObjectName(u"Home_BTN")
        icon = QIcon()
        icon.addFile(u":/img/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home_BTN.setIcon(icon)
        self.Home_BTN.setIconSize(QSize(47, 43))
        self.Home_BTN.setFlat(True)

        self.verticalLayout_5.addWidget(self.Home_BTN)

        self.img_BTN = QPushButton(self.frame_left_menu)
        self.img_BTN.setObjectName(u"img_BTN")
        self.img_BTN.setMouseTracking(False)
        icon1 = QIcon()
        icon1.addFile(u":/img/img.png", QSize(), QIcon.Normal, QIcon.Off)
        self.img_BTN.setIcon(icon1)
        self.img_BTN.setIconSize(QSize(47, 42))
        self.img_BTN.setFlat(True)

        self.verticalLayout_5.addWidget(self.img_BTN)

        self.video_BTN = QPushButton(self.frame_left_menu)
        self.video_BTN.setObjectName(u"video_BTN")
        icon2 = QIcon()
        icon2.addFile(u":/img/video.png", QSize(), QIcon.Normal, QIcon.Off)
        self.video_BTN.setIcon(icon2)
        self.video_BTN.setIconSize(QSize(47, 42))

        self.verticalLayout_5.addWidget(self.video_BTN)

        self.audio_BTN = QPushButton(self.frame_left_menu)
        self.audio_BTN.setObjectName(u"audio_BTN")
        icon3 = QIcon()
        icon3.addFile(u":/img/audio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.audio_BTN.setIcon(icon3)
        self.audio_BTN.setIconSize(QSize(47, 42))

        self.verticalLayout_5.addWidget(self.audio_BTN)

        self.txt_BTN = QPushButton(self.frame_left_menu)
        self.txt_BTN.setObjectName(u"txt_BTN")
        icon4 = QIcon()
        icon4.addFile(u":/img/txt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.txt_BTN.setIcon(icon4)
        self.txt_BTN.setIconSize(QSize(47, 42))

        self.verticalLayout_5.addWidget(self.txt_BTN)

        self.exe_BTN = QPushButton(self.frame_left_menu)
        self.exe_BTN.setObjectName(u"exe_BTN")
        icon5 = QIcon()
        icon5.addFile(u":/img/exe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exe_BTN.setIcon(icon5)
        self.exe_BTN.setIconSize(QSize(47, 42))

        self.verticalLayout_5.addWidget(self.exe_BTN)

        self.pdf_BTN = QPushButton(self.frame_left_menu)
        self.pdf_BTN.setObjectName(u"pdf_BTN")
        icon6 = QIcon()
        icon6.addFile(u":/img/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pdf_BTN.setIcon(icon6)
        self.pdf_BTN.setIconSize(QSize(47, 42))

        self.verticalLayout_5.addWidget(self.pdf_BTN)

        self.More_BTN = QPushButton(self.frame_left_menu)
        self.More_BTN.setObjectName(u"More_BTN")
        icon7 = QIcon()
        icon7.addFile(u":/img/more.png", QSize(), QIcon.Normal, QIcon.Off)
        self.More_BTN.setIcon(icon7)
        self.More_BTN.setIconSize(QSize(47, 42))

        self.verticalLayout_5.addWidget(self.More_BTN)

        self.Main_Frame = QFrame(self.centralwidget)
        self.Main_Frame.setObjectName(u"Main_Frame")
        self.Main_Frame.setGeometry(QRect(111, 5, 1000, 700))
        self.Main_Frame.setMinimumSize(QSize(900, 700))
        self.Main_Frame.setLayoutDirection(Qt.LeftToRight)
        self.Main_Frame.setFrameShape(QFrame.NoFrame)
        self.Main_Frame.setFrameShadow(QFrame.Raised)
        self.Video_frame = QFrame(self.Main_Frame)
        self.Video_frame.setObjectName(u"Video_frame")
        self.Video_frame.setGeometry(QRect(10, 11, 985, 670))
        self.Video_frame.setFrameShape(QFrame.StyledPanel)
        self.Video_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.Video_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_7 = QFrame(self.Video_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 70))
        self.frame_7.setMaximumSize(QSize(200, 100))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 14, 5, 14)
        self.DeEggerTool_BTN = QPushButton(self.frame_7)
        self.DeEggerTool_BTN.setObjectName(u"DeEggerTool_BTN")
        self.DeEggerTool_BTN.setMinimumSize(QSize(0, 70))
        self.DeEggerTool_BTN.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.DeEggerTool_BTN.setFont(font)

        self.verticalLayout_8.addWidget(self.DeEggerTool_BTN)


        self.horizontalLayout_15.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.Video_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 70))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setMouseTracking(False)
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 10, 5, 10)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 80))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_25 = QLabel(self.frame_9)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 70))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_25.setFont(font1)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(50, 50))
        self.label_26.setMouseTracking(True)
        self.label_26.setPixmap(QPixmap(u":/img/help.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(False)

        self.horizontalLayout_16.addWidget(self.label_26)


        self.verticalLayout_9.addWidget(self.frame_9)


        self.horizontalLayout_15.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.Audio_frame = QFrame(self.Main_Frame)
        self.Audio_frame.setObjectName(u"Audio_frame")
        self.Audio_frame.setGeometry(QRect(10, 11, 985, 670))
        self.Audio_frame.setFrameShape(QFrame.StyledPanel)
        self.Audio_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Audio_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_10 = QFrame(self.Audio_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(200, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Mp3StegoTool_BTN = QPushButton(self.frame_10)
        self.Mp3StegoTool_BTN.setObjectName(u"Mp3StegoTool_BTN")
        self.Mp3StegoTool_BTN.setMaximumSize(QSize(16777215, 70))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.Mp3StegoTool_BTN.setFont(font2)

        self.verticalLayout_10.addWidget(self.Mp3StegoTool_BTN)

        self.DeepSoundTool_Btn = QPushButton(self.frame_10)
        self.DeepSoundTool_Btn.setObjectName(u"DeepSoundTool_Btn")
        self.DeepSoundTool_Btn.setMaximumSize(QSize(16777215, 70))
        self.DeepSoundTool_Btn.setFont(font2)

        self.verticalLayout_10.addWidget(self.DeepSoundTool_Btn)

        self.StegHideTool_BTN = QPushButton(self.frame_10)
        self.StegHideTool_BTN.setObjectName(u"StegHideTool_BTN")
        self.StegHideTool_BTN.setMaximumSize(QSize(16777215, 70))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.StegHideTool_BTN.setFont(font3)

        self.verticalLayout_10.addWidget(self.StegHideTool_BTN)


        self.horizontalLayout_17.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.Audio_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMouseTracking(False)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_27 = QLabel(self.frame_12)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 70))
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(50, 50))
        self.label_28.setMouseTracking(True)
        self.label_28.setPixmap(QPixmap(u":/img/help.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_28.setWordWrap(False)

        self.horizontalLayout_18.addWidget(self.label_28)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 80))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_29 = QLabel(self.frame_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 70))
        self.label_29.setFont(font1)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(50, 50))
        self.label_30.setMouseTracking(True)
        self.label_30.setPixmap(QPixmap(u":/img/help.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_30.setWordWrap(False)

        self.horizontalLayout_19.addWidget(self.label_30)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_33 = QLabel(self.frame_15)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 70))
        self.label_33.setFont(font1)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_15)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(50, 50))
        self.label_34.setMouseTracking(True)
        self.label_34.setPixmap(QPixmap(u":/img/help.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_34.setWordWrap(False)

        self.horizontalLayout_21.addWidget(self.label_34)


        self.verticalLayout_11.addWidget(self.frame_15)


        self.horizontalLayout_17.addWidget(self.frame_11)

        self.LSB_Frame = QFrame(self.Main_Frame)
        self.LSB_Frame.setObjectName(u"LSB_Frame")
        self.LSB_Frame.setEnabled(True)
        self.LSB_Frame.setGeometry(QRect(10, 11, 985, 670))
        self.LSB_Frame.setFrameShape(QFrame.StyledPanel)
        self.LSB_Frame.setFrameShadow(QFrame.Raised)
        self.LSB_Frame.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.LSB_Frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.LSB_Frame)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_3.setFont(font4)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.frame_secretTxt = QFrame(self.LSB_Frame)
        self.frame_secretTxt.setObjectName(u"frame_secretTxt")
        self.frame_secretTxt.setMinimumSize(QSize(0, 60))
        self.frame_secretTxt.setMaximumSize(QSize(16777215, 50))
        self.frame_secretTxt.setFrameShape(QFrame.StyledPanel)
        self.frame_secretTxt.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_secretTxt)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.Message_txt = QTextEdit(self.frame_secretTxt)
        self.Message_txt.setObjectName(u"Message_txt")

        self.horizontalLayout_2.addWidget(self.Message_txt)


        self.verticalLayout.addWidget(self.frame_secretTxt)

        self.frame_Img = QFrame(self.LSB_Frame)
        self.frame_Img.setObjectName(u"frame_Img")
        self.frame_Img.setEnabled(True)
        self.frame_Img.setFrameShape(QFrame.StyledPanel)
        self.frame_Img.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_Img)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Browse_frame = QFrame(self.frame_Img)
        self.Browse_frame.setObjectName(u"Browse_frame")
        self.Browse_frame.setMinimumSize(QSize(0, 50))
        self.Browse_frame.setMaximumSize(QSize(16777215, 50))
        self.Browse_frame.setFrameShape(QFrame.StyledPanel)
        self.Browse_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Browse_frame)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.PathFile = QLineEdit(self.Browse_frame)
        self.PathFile.setObjectName(u"PathFile")
        self.PathFile.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.PathFile)

        self.Browse_Btn = QPushButton(self.Browse_frame)
        self.Browse_Btn.setObjectName(u"Browse_Btn")
        self.Browse_Btn.setMinimumSize(QSize(40, 20))

        self.horizontalLayout_3.addWidget(self.Browse_Btn)


        self.verticalLayout_2.addWidget(self.Browse_frame)

        self.Hide_BTN = QPushButton(self.frame_Img)
        self.Hide_BTN.setObjectName(u"Hide_BTN")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Hide_BTN.sizePolicy().hasHeightForWidth())
        self.Hide_BTN.setSizePolicy(sizePolicy1)
        self.Hide_BTN.setMaximumSize(QSize(150, 60))
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setWeight(75)
        self.Hide_BTN.setFont(font5)

        self.verticalLayout_2.addWidget(self.Hide_BTN, 0, Qt.AlignHCenter)

        self.frame_showIMG = QFrame(self.frame_Img)
        self.frame_showIMG.setObjectName(u"frame_showIMG")
        self.frame_showIMG.setFrameShape(QFrame.StyledPanel)
        self.frame_showIMG.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_showIMG)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_imgView_1 = QFrame(self.frame_showIMG)
        self.frame_imgView_1.setObjectName(u"frame_imgView_1")
        self.frame_imgView_1.setMinimumSize(QSize(485, 429))
        self.frame_imgView_1.setMaximumSize(QSize(485, 429))
        self.frame_imgView_1.setFrameShape(QFrame.StyledPanel)
        self.frame_imgView_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_imgView_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_imgView_1)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_31 = QLabel(self.frame_imgView_1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(461, 382))
        self.label_31.setFrameShape(QFrame.NoFrame)
        self.label_31.setScaledContents(True)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_31)


        self.horizontalLayout_4.addWidget(self.frame_imgView_1)

        self.frame_imgView_2 = QFrame(self.frame_showIMG)
        self.frame_imgView_2.setObjectName(u"frame_imgView_2")
        self.frame_imgView_2.setMinimumSize(QSize(484, 429))
        self.frame_imgView_2.setMaximumSize(QSize(484, 429))
        self.frame_imgView_2.setFrameShape(QFrame.StyledPanel)
        self.frame_imgView_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_imgView_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_imgView_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_32 = QLabel(self.frame_imgView_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(460, 382))
        self.label_32.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_32)


        self.horizontalLayout_4.addWidget(self.frame_imgView_2)


        self.verticalLayout_2.addWidget(self.frame_showIMG)


        self.verticalLayout.addWidget(self.frame_Img)

        self.ImagesTools_BTN = QPushButton(self.LSB_Frame)
        self.ImagesTools_BTN.setObjectName(u"ImagesTools_BTN")
        self.ImagesTools_BTN.setFont(font5)

        self.verticalLayout.addWidget(self.ImagesTools_BTN)

        self.TXT_frame = QFrame(self.Main_Frame)
        self.TXT_frame.setObjectName(u"TXT_frame")
        self.TXT_frame.setGeometry(QRect(10, 11, 985, 670))
        self.TXT_frame.setFrameShape(QFrame.StyledPanel)
        self.TXT_frame.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.TXT_frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(12, 12, 192, 100))
        self.frame_14.setMinimumSize(QSize(0, 100))
        self.frame_14.setMaximumSize(QSize(200, 100))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 14, 5, 14)
        self.MSOffice_BTN = QPushButton(self.frame_14)
        self.MSOffice_BTN.setObjectName(u"MSOffice_BTN")
        self.MSOffice_BTN.setMaximumSize(QSize(16777215, 70))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        self.MSOffice_BTN.setFont(font6)

        self.verticalLayout_12.addWidget(self.MSOffice_BTN)

        self.frame_16 = QFrame(self.TXT_frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(211, 12, 762, 98))
        self.frame_16.setMinimumSize(QSize(0, 70))
        self.frame_16.setMaximumSize(QSize(16777215, 100))
        self.frame_16.setMouseTracking(False)
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 10, 5, 10)
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 80))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_35 = QLabel(self.frame_17)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(16777215, 70))
        self.label_35.setFont(font1)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_17)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(50, 50))
        self.label_36.setMouseTracking(True)
        self.label_36.setPixmap(QPixmap(u":/img/help.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_36.setWordWrap(False)

        self.horizontalLayout_22.addWidget(self.label_36)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.MSOfficeGIF = QLabel(self.TXT_frame)
        self.MSOfficeGIF.setObjectName(u"MSOfficeGIF")
        self.MSOfficeGIF.setGeometry(QRect(12, 120, 961, 541))
        self.MSOfficeGIF.setScaledContents(True)
        self.MSOfficeGIF.setAlignment(Qt.AlignCenter)
        self.EXE_frame = QFrame(self.Main_Frame)
        self.EXE_frame.setObjectName(u"EXE_frame")
        self.EXE_frame.setGeometry(QRect(10, 11, 985, 670))
        self.EXE_frame.setFont(font1)
        self.EXE_frame.setFrameShape(QFrame.StyledPanel)
        self.EXE_frame.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.EXE_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(12, 12, 192, 100))
        self.frame_18.setMinimumSize(QSize(0, 100))
        self.frame_18.setMaximumSize(QSize(200, 100))
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_18)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 14, 5, 14)
        self.OurSecret_BTN = QPushButton(self.frame_18)
        self.OurSecret_BTN.setObjectName(u"OurSecret_BTN")
        self.OurSecret_BTN.setMaximumSize(QSize(16777215, 70))
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.OurSecret_BTN.setFont(font7)

        self.verticalLayout_14.addWidget(self.OurSecret_BTN)

        self.frame_19 = QFrame(self.EXE_frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(211, 12, 762, 98))
        self.frame_19.setMinimumSize(QSize(0, 70))
        self.frame_19.setMaximumSize(QSize(16777215, 100))
        self.frame_19.setMouseTracking(False)
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_19)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 10, 5, 10)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 80))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_37 = QLabel(self.frame_20)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 70))
        self.label_37.setFont(font1)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_20)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(50, 50))
        self.label_38.setMouseTracking(True)
        self.label_38.setPixmap(QPixmap(u":/img/help.png"))
        self.label_38.setScaledContents(True)
        self.label_38.setAlignment(Qt.AlignCenter)
        self.label_38.setWordWrap(False)

        self.horizontalLayout_23.addWidget(self.label_38)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.Hello_Message = QLabel(self.Main_Frame)
        self.Hello_Message.setObjectName(u"Hello_Message")
        self.Hello_Message.setGeometry(QRect(20, 20, 985, 670))
        font8 = QFont()
        font8.setPointSize(48)
        font8.setBold(True)
        font8.setWeight(75)
        font8.setStrikeOut(False)
        self.Hello_Message.setFont(font8)
        self.Hello_Message.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.Main_Frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(248, 409, 521, 37))
        font9 = QFont()
        font9.setPointSize(11)
        self.label_4.setFont(font9)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.Logo = QLabel(self.Main_Frame)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(360, 80, 221, 191))
        self.Logo.setPixmap(QPixmap(u":/img/logo.png"))
        self.Logo.setScaledContents(True)
        self.IMG_frame = QFrame(self.Main_Frame)
        self.IMG_frame.setObjectName(u"IMG_frame")
        self.IMG_frame.setGeometry(QRect(10, 11, 985, 670))
        self.IMG_frame.setFrameShape(QFrame.StyledPanel)
        self.IMG_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.IMG_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.IMG_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.GifShufTool_BTN = QPushButton(self.frame)
        self.GifShufTool_BTN.setObjectName(u"GifShufTool_BTN")
        self.GifShufTool_BTN.setMaximumSize(QSize(16777215, 70))
        self.GifShufTool_BTN.setFont(font3)

        self.verticalLayout_6.addWidget(self.GifShufTool_BTN)

        self.STool_BTN = QPushButton(self.frame)
        self.STool_BTN.setObjectName(u"STool_BTN")
        self.STool_BTN.setMaximumSize(QSize(16777215, 70))
        self.STool_BTN.setFont(font7)

        self.verticalLayout_6.addWidget(self.STool_BTN)

        self.XiaoStego_BTN = QPushButton(self.frame)
        self.XiaoStego_BTN.setObjectName(u"XiaoStego_BTN")
        self.XiaoStego_BTN.setMaximumSize(QSize(16777215, 70))
        self.XiaoStego_BTN.setFont(font3)

        self.verticalLayout_6.addWidget(self.XiaoStego_BTN)

        self.StegoXPlus_BTN = QPushButton(self.frame)
        self.StegoXPlus_BTN.setObjectName(u"StegoXPlus_BTN")
        self.StegoXPlus_BTN.setMaximumSize(QSize(16777215, 70))
        self.StegoXPlus_BTN.setFont(font7)

        self.verticalLayout_6.addWidget(self.StegoXPlus_BTN)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.IMG_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMouseTracking(False)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 70))
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(50, 50))
        self.label_20.setMouseTracking(True)
        self.label_20.setPixmap(QPixmap(u":/img/help.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setWordWrap(False)

        self.horizontalLayout_12.addWidget(self.label_20)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 70))
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(50, 50))
        self.label_22.setMouseTracking(True)
        self.label_22.setPixmap(QPixmap(u":/img/help.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_22.setWordWrap(False)

        self.horizontalLayout_13.addWidget(self.label_22)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 80))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 70))
        self.label_23.setFont(font1)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(50, 50))
        self.label_24.setMouseTracking(True)
        self.label_24.setPixmap(QPixmap(u":/img/help.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setWordWrap(False)

        self.horizontalLayout_14.addWidget(self.label_24)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 70))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(50, 50))
        self.label_6.setMouseTracking(True)
        self.label_6.setPixmap(QPixmap(u":/img/help.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame_2)

        self.More_frame = QFrame(self.Main_Frame)
        self.More_frame.setObjectName(u"More_frame")
        self.More_frame.setEnabled(True)
        self.More_frame.setGeometry(QRect(10, 11, 985, 670))
        self.More_frame.setFrameShape(QFrame.StyledPanel)
        self.More_frame.setFrameShadow(QFrame.Raised)
        self.frame_24 = QFrame(self.More_frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(12, 12, 200, 646))
        self.frame_24.setMaximumSize(QSize(200, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_24)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.DetectingAdsFiles_BTN = QPushButton(self.frame_24)
        self.DetectingAdsFiles_BTN.setObjectName(u"DetectingAdsFiles_BTN")
        self.DetectingAdsFiles_BTN.setMaximumSize(QSize(16777215, 70))
        self.DetectingAdsFiles_BTN.setFont(font6)

        self.verticalLayout_18.addWidget(self.DetectingAdsFiles_BTN)

        self.DeskEncryption_BTN = QPushButton(self.frame_24)
        self.DeskEncryption_BTN.setObjectName(u"DeskEncryption_BTN")
        self.DeskEncryption_BTN.setMaximumSize(QSize(16777215, 70))
        self.DeskEncryption_BTN.setFont(font2)

        self.verticalLayout_18.addWidget(self.DeskEncryption_BTN)

        self.HideINAds_BTN = QPushButton(self.frame_24)
        self.HideINAds_BTN.setObjectName(u"HideINAds_BTN")
        self.HideINAds_BTN.setMaximumSize(QSize(16777215, 70))
        self.HideINAds_BTN.setFont(font4)

        self.verticalLayout_18.addWidget(self.HideINAds_BTN)

        self.HideINWinRegistry_BTN = QPushButton(self.frame_24)
        self.HideINWinRegistry_BTN.setObjectName(u"HideINWinRegistry_BTN")
        self.HideINWinRegistry_BTN.setMaximumSize(QSize(16777215, 70))
        self.HideINWinRegistry_BTN.setFont(font6)

        self.verticalLayout_18.addWidget(self.HideINWinRegistry_BTN)

        self.PassSafe_BTN = QPushButton(self.frame_24)
        self.PassSafe_BTN.setObjectName(u"PassSafe_BTN")
        self.PassSafe_BTN.setMaximumSize(QSize(16777215, 70))
        self.PassSafe_BTN.setFont(font6)

        self.verticalLayout_18.addWidget(self.PassSafe_BTN)

        self.STG_BTN = QPushButton(self.frame_24)
        self.STG_BTN.setObjectName(u"STG_BTN")
        self.STG_BTN.setMaximumSize(QSize(16777215, 70))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.STG_BTN.setFont(font10)

        self.verticalLayout_18.addWidget(self.STG_BTN)

        self.Thumbnail_BTN = QPushButton(self.frame_24)
        self.Thumbnail_BTN.setObjectName(u"Thumbnail_BTN")
        self.Thumbnail_BTN.setMaximumSize(QSize(16777215, 70))
        self.Thumbnail_BTN.setFont(font6)

        self.verticalLayout_18.addWidget(self.Thumbnail_BTN)

        self.frame_25 = QFrame(self.More_frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(219, 12, 754, 646))
        self.frame_25.setMouseTracking(False)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.ADS_TXT_Frame = QFrame(self.frame_25)
        self.ADS_TXT_Frame.setObjectName(u"ADS_TXT_Frame")
        self.ADS_TXT_Frame.setGeometry(QRect(12, 23, 720, 70))
        self.ADS_TXT_Frame.setMaximumSize(QSize(16777215, 80))
        self.ADS_TXT_Frame.setFrameShape(QFrame.StyledPanel)
        self.ADS_TXT_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.ADS_TXT_Frame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.ADS_TXT_Frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 70))
        self.label_41.setFont(font1)
        self.label_41.setScaledContents(True)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_41, 0, Qt.AlignVCenter)

        self.label_42 = QLabel(self.ADS_TXT_Frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(50, 50))
        self.label_42.setMouseTracking(True)
        self.label_42.setPixmap(QPixmap(u":/img/help.png"))
        self.label_42.setScaledContents(True)
        self.label_42.setAlignment(Qt.AlignCenter)
        self.label_42.setWordWrap(False)

        self.horizontalLayout_25.addWidget(self.label_42)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(12, 111, 720, 70))
        self.frame_27.setMaximumSize(QSize(16777215, 80))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_43 = QLabel(self.frame_27)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 70))
        font11 = QFont()
        font11.setPointSize(8)
        self.label_43.setFont(font11)
        self.label_43.setScaledContents(True)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_43)

        self.label_44 = QLabel(self.frame_27)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(50, 50))
        self.label_44.setMouseTracking(True)
        self.label_44.setPixmap(QPixmap(u":/img/help.png"))
        self.label_44.setScaledContents(True)
        self.label_44.setAlignment(Qt.AlignCenter)
        self.label_44.setWordWrap(False)

        self.horizontalLayout_26.addWidget(self.label_44)

        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(12, 199, 720, 70))
        self.frame_28.setMaximumSize(QSize(16777215, 80))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_28)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(16777215, 70))
        self.label_45.setFont(font1)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_45)

        self.label_46 = QLabel(self.frame_28)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(50, 50))
        self.label_46.setMouseTracking(True)
        self.label_46.setPixmap(QPixmap(u":/img/help.png"))
        self.label_46.setScaledContents(True)
        self.label_46.setAlignment(Qt.AlignCenter)
        self.label_46.setWordWrap(False)

        self.horizontalLayout_27.addWidget(self.label_46)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(12, 287, 720, 70))
        self.frame_29.setMaximumSize(QSize(16777215, 80))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_47 = QLabel(self.frame_29)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 70))
        self.label_47.setFont(font1)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_29)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(50, 50))
        self.label_48.setMouseTracking(True)
        self.label_48.setPixmap(QPixmap(u":/img/help.png"))
        self.label_48.setScaledContents(True)
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_48.setWordWrap(False)

        self.horizontalLayout_28.addWidget(self.label_48)

        self.ADS_BTN_Frame = QFrame(self.frame_25)
        self.ADS_BTN_Frame.setObjectName(u"ADS_BTN_Frame")
        self.ADS_BTN_Frame.setGeometry(QRect(10, 23, 720, 70))
        self.ADS_BTN_Frame.setFrameShape(QFrame.StyledPanel)
        self.ADS_BTN_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.ADS_BTN_Frame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.ADSViewer_BTN = QPushButton(self.ADS_BTN_Frame)
        self.ADSViewer_BTN.setObjectName(u"ADSViewer_BTN")
        self.ADSViewer_BTN.setMaximumSize(QSize(16777215, 70))
        self.ADSViewer_BTN.setFont(font3)

        self.horizontalLayout_29.addWidget(self.ADSViewer_BTN)

        self.GMARTool_BTN = QPushButton(self.ADS_BTN_Frame)
        self.GMARTool_BTN.setObjectName(u"GMARTool_BTN")
        self.GMARTool_BTN.setMaximumSize(QSize(16777215, 70))
        self.GMARTool_BTN.setFont(font3)

        self.horizontalLayout_29.addWidget(self.GMARTool_BTN)

        self.lads_BTN = QPushButton(self.ADS_BTN_Frame)
        self.lads_BTN.setObjectName(u"lads_BTN")
        self.lads_BTN.setMaximumSize(QSize(16777215, 70))
        self.lads_BTN.setFont(font3)

        self.horizontalLayout_29.addWidget(self.lads_BTN)

        self.frame_32 = QFrame(self.frame_25)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(12, 463, 720, 70))
        self.frame_32.setMaximumSize(QSize(16777215, 80))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_53 = QLabel(self.frame_32)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(16777215, 70))
        self.label_53.setFont(font11)
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_53)

        self.label_54 = QLabel(self.frame_32)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(50, 50))
        self.label_54.setMouseTracking(True)
        self.label_54.setPixmap(QPixmap(u":/img/help.png"))
        self.label_54.setScaledContents(True)
        self.label_54.setAlignment(Qt.AlignCenter)
        self.label_54.setWordWrap(False)

        self.horizontalLayout_32.addWidget(self.label_54)

        self.frame_31 = QFrame(self.frame_25)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(12, 375, 720, 70))
        self.frame_31.setMaximumSize(QSize(16777215, 80))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_51 = QLabel(self.frame_31)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 70))
        self.label_51.setFont(font1)
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_51)

        self.label_52 = QLabel(self.frame_31)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(50, 50))
        self.label_52.setMouseTracking(True)
        self.label_52.setPixmap(QPixmap(u":/img/help.png"))
        self.label_52.setScaledContents(True)
        self.label_52.setAlignment(Qt.AlignCenter)
        self.label_52.setWordWrap(False)

        self.horizontalLayout_31.addWidget(self.label_52)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(12, 551, 720, 70))
        self.frame_30.setMaximumSize(QSize(16777215, 80))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_49 = QLabel(self.frame_30)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 70))
        self.label_49.setFont(font11)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_49)

        self.label_50 = QLabel(self.frame_30)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(50, 50))
        self.label_50.setMouseTracking(True)
        self.label_50.setPixmap(QPixmap(u":/img/help.png"))
        self.label_50.setScaledContents(True)
        self.label_50.setAlignment(Qt.AlignCenter)
        self.label_50.setWordWrap(False)

        self.horizontalLayout_30.addWidget(self.label_50)

        self.HideAdsGIF = QLabel(self.More_frame)
        self.HideAdsGIF.setObjectName(u"HideAdsGIF")
        self.HideAdsGIF.setGeometry(QRect(219, 12, 754, 646))
        self.HideAdsGIF.setScaledContents(True)
        self.HideAdsGIF.setAlignment(Qt.AlignCenter)
        self.HideRegistryGIF = QLabel(self.More_frame)
        self.HideRegistryGIF.setObjectName(u"HideRegistryGIF")
        self.HideRegistryGIF.setGeometry(QRect(219, 12, 754, 646))
        self.HideRegistryGIF.setScaledContents(True)
        self.HideRegistryGIF.setAlignment(Qt.AlignCenter)
        self.PDF_frame = QFrame(self.Main_Frame)
        self.PDF_frame.setObjectName(u"PDF_frame")
        self.PDF_frame.setGeometry(QRect(10, 11, 985, 670))
        self.PDF_frame.setFont(font1)
        self.PDF_frame.setFrameShape(QFrame.StyledPanel)
        self.PDF_frame.setFrameShadow(QFrame.Raised)
        self.frame_21 = QFrame(self.PDF_frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(12, 12, 192, 100))
        self.frame_21.setMinimumSize(QSize(0, 100))
        self.frame_21.setMaximumSize(QSize(200, 100))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_21)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 14, 5, 14)
        self.wbStego4open_BTN = QPushButton(self.frame_21)
        self.wbStego4open_BTN.setObjectName(u"wbStego4open_BTN")
        self.wbStego4open_BTN.setMaximumSize(QSize(16777215, 70))
        self.wbStego4open_BTN.setFont(font3)

        self.verticalLayout_16.addWidget(self.wbStego4open_BTN)

        self.frame_22 = QFrame(self.PDF_frame)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(219, 20, 762, 98))
        self.frame_22.setMinimumSize(QSize(0, 70))
        self.frame_22.setMaximumSize(QSize(16777215, 100))
        self.frame_22.setMouseTracking(False)
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_22)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 10, 5, 10)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 80))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_39 = QLabel(self.frame_23)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(16777215, 70))
        self.label_39.setFont(font1)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_23)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(50, 50))
        self.label_40.setMouseTracking(True)
        self.label_40.setPixmap(QPixmap(u":/img/help.png"))
        self.label_40.setScaledContents(True)
        self.label_40.setAlignment(Qt.AlignCenter)
        self.label_40.setWordWrap(False)

        self.horizontalLayout_24.addWidget(self.label_40)


        self.verticalLayout_17.addWidget(self.frame_23)

        self.frame_26 = QFrame(self.PDF_frame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(12, 114, 192, 100))
        self.frame_26.setMinimumSize(QSize(0, 100))
        self.frame_26.setMaximumSize(QSize(200, 100))
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_26)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 14, 5, 14)
        self.OurSecret_BTN_2 = QPushButton(self.frame_26)
        self.OurSecret_BTN_2.setObjectName(u"OurSecret_BTN_2")
        self.OurSecret_BTN_2.setMaximumSize(QSize(16777215, 70))
        self.OurSecret_BTN_2.setFont(font7)

        self.verticalLayout_19.addWidget(self.OurSecret_BTN_2)

        self.frame_33 = QFrame(self.PDF_frame)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(219, 114, 762, 98))
        self.frame_33.setMinimumSize(QSize(0, 70))
        self.frame_33.setMaximumSize(QSize(16777215, 100))
        self.frame_33.setMouseTracking(False)
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_33)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 10, 5, 10)
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 80))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_55 = QLabel(self.frame_34)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(16777215, 70))
        self.label_55.setFont(font1)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_55)

        self.label_56 = QLabel(self.frame_34)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(50, 50))
        self.label_56.setMouseTracking(True)
        self.label_56.setPixmap(QPixmap(u":/img/help.png"))
        self.label_56.setScaledContents(True)
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_56.setWordWrap(False)

        self.horizontalLayout_33.addWidget(self.label_56)


        self.verticalLayout_20.addWidget(self.frame_34)

        self.frame_37 = QFrame(self.PDF_frame)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(12, 220, 192, 100))
        self.frame_37.setMinimumSize(QSize(0, 100))
        self.frame_37.setMaximumSize(QSize(200, 100))
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_37)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 14, 5, 14)
        self.HTML_BTN = QPushButton(self.frame_37)
        self.HTML_BTN.setObjectName(u"HTML_BTN")
        self.HTML_BTN.setMaximumSize(QSize(16777215, 70))
        self.HTML_BTN.setFont(font7)

        self.verticalLayout_22.addWidget(self.HTML_BTN)

        self.frame_35 = QFrame(self.PDF_frame)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(219, 220, 762, 98))
        self.frame_35.setMinimumSize(QSize(0, 70))
        self.frame_35.setMaximumSize(QSize(16777215, 100))
        self.frame_35.setMouseTracking(False)
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_35)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 10, 5, 10)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 80))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_57 = QLabel(self.frame_36)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(16777215, 70))
        font12 = QFont()
        font12.setFamily(u"MS Sans Serif")
        font12.setPointSize(9)
        self.label_57.setFont(font12)
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_57)

        self.label_58 = QLabel(self.frame_36)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(50, 50))
        self.label_58.setMouseTracking(True)
        self.label_58.setPixmap(QPixmap(u":/img/help.png"))
        self.label_58.setScaledContents(True)
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_58.setWordWrap(False)

        self.horizontalLayout_34.addWidget(self.label_58)


        self.verticalLayout_21.addWidget(self.frame_36)

        self.HTMLGIF = QLabel(self.PDF_frame)
        self.HTMLGIF.setObjectName(u"HTMLGIF")
        self.HTMLGIF.setGeometry(QRect(12, 327, 971, 341))
        self.HTMLGIF.setScaledContents(True)
        self.HTMLGIF.setAlignment(Qt.AlignCenter)
        self.Video_frame.raise_()
        self.Audio_frame.raise_()
        self.LSB_Frame.raise_()
        self.EXE_frame.raise_()
        self.Hello_Message.raise_()
        self.label_4.raise_()
        self.Logo.raise_()
        self.IMG_frame.raise_()
        self.More_frame.raise_()
        self.TXT_frame.raise_()
        self.PDF_frame.raise_()
        Stego_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stego_main)

        QMetaObject.connectSlotsByName(Stego_main)
    # setupUi

    def retranslateUi(self, Stego_main):
        Stego_main.setWindowTitle(QCoreApplication.translate("Stego_main", u"Stego Text", None))
        self.Home_BTN.setText("")
#if QT_CONFIG(tooltip)
        self.img_BTN.setToolTip(QCoreApplication.translate("Stego_main", u"Image", None))
#endif // QT_CONFIG(tooltip)
        self.img_BTN.setText("")
#if QT_CONFIG(tooltip)
        self.video_BTN.setToolTip(QCoreApplication.translate("Stego_main", u"Video", None))
#endif // QT_CONFIG(tooltip)
        self.video_BTN.setText("")
#if QT_CONFIG(tooltip)
        self.audio_BTN.setToolTip(QCoreApplication.translate("Stego_main", u"Audio", None))
#endif // QT_CONFIG(tooltip)
        self.audio_BTN.setText("")
#if QT_CONFIG(tooltip)
        self.txt_BTN.setToolTip(QCoreApplication.translate("Stego_main", u"MS Offise", None))
#endif // QT_CONFIG(tooltip)
        self.txt_BTN.setText("")
#if QT_CONFIG(tooltip)
        self.exe_BTN.setToolTip(QCoreApplication.translate("Stego_main", u"EXE", None))
#endif // QT_CONFIG(tooltip)
        self.exe_BTN.setText("")
#if QT_CONFIG(tooltip)
        self.pdf_BTN.setToolTip(QCoreApplication.translate("Stego_main", u"PDF", None))
#endif // QT_CONFIG(tooltip)
        self.pdf_BTN.setText("")
#if QT_CONFIG(tooltip)
        self.More_BTN.setToolTip(QCoreApplication.translate("Stego_main", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.More_BTN.setText("")
        self.DeEggerTool_BTN.setText(QCoreApplication.translate("Stego_main", u"DeEgger Embadder tool", None))
#if QT_CONFIG(tooltip)
        self.frame_8.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("Stego_main", u"DeEgger Embedder is a small software application whose purpose is to help you hide your sensitive files\n"
" from prying eyes by embedding them into other media items,\n"
" such as AVI, JPG, PNG, MP3, or other file format.", None))
#if QT_CONFIG(tooltip)
        self.label_26.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_26.setText("")
        self.Mp3StegoTool_BTN.setText(QCoreApplication.translate("Stego_main", u"Mp3Stego Tool", None))
        self.DeepSoundTool_Btn.setText(QCoreApplication.translate("Stego_main", u"Deep Sound tool", None))
        self.StegHideTool_BTN.setText(QCoreApplication.translate("Stego_main", u"Steghide Tool", None))
#if QT_CONFIG(tooltip)
        self.frame_11.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("Stego_main", u"MP3Stego is a typical steganographic tool for MP3 audio,\n"
" which embeds secret message into MP3 audio according to the parity of the block length. ", None))
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("Stego_main", u"DeepSound is an audio steganography tool\n"
" and audio converter that hides secret data into audio files, \n"
"the application also enables you to extract secret files directly from audio files or audio CD tracks.", None))
#if QT_CONFIG(tooltip)
        self.label_30.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_30.setText("")
        self.label_33.setText(QCoreApplication.translate("Stego_main", u"Steghide is a steganography program that is able to hide data in various kinds of image\n"
"- and audio-files. The color- respectivly sample-frequencies \n"
"are not changed thus making the embedding resistant against first-order statistical tests.", None))
#if QT_CONFIG(tooltip)
        self.label_34.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_34.setText("")
        self.label_3.setText(QCoreApplication.translate("Stego_main", u"LSB Stego", None))
        self.Message_txt.setPlaceholderText(QCoreApplication.translate("Stego_main", u"Enter your secret message", None))
        self.PathFile.setPlaceholderText(QCoreApplication.translate("Stego_main", u"File Path", None))
        self.Browse_Btn.setText(QCoreApplication.translate("Stego_main", u"browse", None))
        self.Hide_BTN.setText(QCoreApplication.translate("Stego_main", u"Hide", None))
        self.label.setText(QCoreApplication.translate("Stego_main", u"Before", None))
        self.label_31.setText("")
        self.label_2.setText(QCoreApplication.translate("Stego_main", u"After", None))
        self.label_32.setText("")
        self.ImagesTools_BTN.setText(QCoreApplication.translate("Stego_main", u"Hide Image tools", None))
        self.MSOffice_BTN.setText(QCoreApplication.translate("Stego_main", u"Hide under MS Office", None))
#if QT_CONFIG(tooltip)
        self.frame_16.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("Stego_main", u"All hiding techniques presented in this section can be implemented\n"
" on all MS Office versions that are based on OOXML file structure like\n"
" MS Office versions 2007\u2013 2013", None))
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_36.setText("")
        self.MSOfficeGIF.setText("")
        self.OurSecret_BTN.setText(QCoreApplication.translate("Stego_main", u"OurSecret", None))
#if QT_CONFIG(tooltip)
        self.frame_19.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_37.setText(QCoreApplication.translate("Stego_main", u"OurSecret is powerful data hider and protector which will put your private files in a secure location.\n"
" Data transmissions are vital and became a necessity nowadays.", None))
#if QT_CONFIG(tooltip)
        self.label_38.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_38.setText("")
        self.Hello_Message.setText(QCoreApplication.translate("Stego_main", u"Welcome to Stego Pro", None))
        self.label_4.setText(QCoreApplication.translate("Stego_main", u"This program is a collection of data hiding tools", None))
        self.Logo.setText("")
        self.GifShufTool_BTN.setText(QCoreApplication.translate("Stego_main", u"Gifshuffle Tool", None))
#if QT_CONFIG(tooltip)
        self.STool_BTN.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.STool_BTN.setText(QCoreApplication.translate("Stego_main", u"S Tool", None))
        self.XiaoStego_BTN.setText(QCoreApplication.translate("Stego_main", u"Xiao Stego tool", None))
        self.StegoXPlus_BTN.setText(QCoreApplication.translate("Stego_main", u"Stego X Plus", None))
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("Stego_main", u"gifshuffle  is a program for hiding messages in GIF images by shuffling the colourmap.\n"
"       A shuffled image is visibly indistinguishable from the original. gifshuffle works with all\n"
"       GIF images, including those with transparency and animation.", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("Stego_main", u"S-Tools is a steganography tool that hides files in BMP, GIF, and WAV files.\n"
" You open up a copy of S-Tools and drag pictures and sounds across to it.\n"
" To hide files you just drag them over open sound/picture windows.", None))
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("Stego_main", u"Xiao Steganography is a great, free Windows software, being part of the category\n"
" Security software with subcategory Encryption and has been created by Nakasoft.\n"
" It's available for users with the operating system Windows 98 and prior versions", None))
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_24.setText("")
        self.label_5.setText(QCoreApplication.translate("Stego_main", u"SteganographX Plus is another small tool that lets you hide your confidential data inside \n"
"a BMP image. It also does not need any installation and is of only 496 KB in size.", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_6.setText("")
        self.DetectingAdsFiles_BTN.setText(QCoreApplication.translate("Stego_main", u"Detecting ADS Files", None))
        self.DeskEncryption_BTN.setText(QCoreApplication.translate("Stego_main", u"Desk Encryption", None))
        self.HideINAds_BTN.setText(QCoreApplication.translate("Stego_main", u"Hide in Ads", None))
        self.HideINWinRegistry_BTN.setText(QCoreApplication.translate("Stego_main", u"Hidding in Win\n"
" Registry", None))
        self.PassSafe_BTN.setText(QCoreApplication.translate("Stego_main", u"Password Safe-Tool ", None))
        self.STG_BTN.setText(QCoreApplication.translate("Stego_main", u"STG Cache Audit", None))
        self.Thumbnail_BTN.setText(QCoreApplication.translate("Stego_main", u"Thumbnail Database\n"
" Viewer", None))
#if QT_CONFIG(tooltip)
        self.frame_25.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_41.setText(QCoreApplication.translate("Stego_main", u"Feature In NTFS, a file consists of different data streams.\n"
"The primary unnamed stream (default stream)\n"
" that contains the visible data that we expect to see in a file after opening it.\n"
"", None))
#if QT_CONFIG(tooltip)
        self.label_42.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_42.setText("")
        self.label_43.setText(QCoreApplication.translate("Stego_main", u"VeraCrypt is a source-available freeware utility used for on-the-fly encryption (OTFE).\n"
" It can create a virtual encrypted disk within a file or encrypt a partition\n"
" or (in Windows) the entire storage device with pre-boot authentication.", None))
#if QT_CONFIG(tooltip)
        self.label_44.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_44.setText("")
        self.label_45.setText(QCoreApplication.translate("Stego_main", u"Feature In NTFS, a file consists of different data streams.\n"
"The primary unnamed stream (default stream)\n"
" that contains the visible data that we expect to see in a file after opening it.", None))
#if QT_CONFIG(tooltip)
        self.label_46.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_46.setText("")
        self.label_47.setText(QCoreApplication.translate("Stego_main", u"Is a technology included in Microsoft Windows that can create backup\n"
" copies or snapshots of computer files or volumes, even when they are in use.", None))
#if QT_CONFIG(tooltip)
        self.label_48.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_48.setText("")
        self.ADSViewer_BTN.setText(QCoreApplication.translate("Stego_main", u"ADS Viewer", None))
        self.GMARTool_BTN.setText(QCoreApplication.translate("Stego_main", u"GMAR Tool", None))
        self.lads_BTN.setText(QCoreApplication.translate("Stego_main", u"lads Viewer", None))
        self.label_53.setText(QCoreApplication.translate("Stego_main", u"STG Cache Audit is an advanced cache, cookie, and history viewer\n"
" That runs on Windows and that allows you to investigate web\n"
" surfing habits of a suspect machine.", None))
#if QT_CONFIG(tooltip)
        self.label_54.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_54.setText("")
        self.label_51.setText(QCoreApplication.translate("Stego_main", u"We can make our password more secure using Password safe tool \n"
"Is a tool to secure your password and make it stronger than you write.", None))
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_52.setText("")
        self.label_49.setText(QCoreApplication.translate("Stego_main", u"Thumbnails are another type of cached information that can be analyzed on a suspect computer\n"
"Thumbnails are found in Windows Operating Systems and are intended to allow a\n"
"quick view of files residing in a folder", None))
#if QT_CONFIG(tooltip)
        self.label_50.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_50.setText("")
        self.HideAdsGIF.setText("")
        self.HideRegistryGIF.setText("")
        self.wbStego4open_BTN.setText(QCoreApplication.translate("Stego_main", u"wbStego4open", None))
#if QT_CONFIG(tooltip)
        self.frame_22.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_39.setText(QCoreApplication.translate("Stego_main", u"wbStego is a steganography tool and hides data in bitmaps, text and HTML files.\n"
" wbStego is published under GNU GPL for Windows and Linux.", None))
#if QT_CONFIG(tooltip)
        self.label_40.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_40.setText("")
        self.OurSecret_BTN_2.setText(QCoreApplication.translate("Stego_main", u"OurSecret", None))
#if QT_CONFIG(tooltip)
        self.frame_33.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_55.setText(QCoreApplication.translate("Stego_main", u"OurSecret is powerful data hider and protector which will put your private files in a secure location.\n"
" Data transmissions are vital and became a necessity nowadays.", None))
#if QT_CONFIG(tooltip)
        self.label_56.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_56.setText("")
        self.HTML_BTN.setText(QCoreApplication.translate("Stego_main", u"HTML", None))
#if QT_CONFIG(tooltip)
        self.frame_35.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_57.setText(QCoreApplication.translate("Stego_main", u"DATA HIDDEN USING XML COMMENTS and tages\n"
"DATA HIDDEN BY MODIFYING HTML ATTRIBUTE\n"
"WRITTEN STATE", None))
#if QT_CONFIG(tooltip)
        self.label_58.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_58.setText("")
        self.HTMLGIF.setText("")
    # retranslateUi

        self.ADSMovie = QMovie("Hide_in_ADS.gif")
        self.HideAdsGIF.setMovie(self.ADSMovie)
        self.ADSMovie.start()

        self.WINMovie = QMovie("HIdding_in_win_registry.gif")
        self.HideRegistryGIF.setMovie(self.WINMovie)
        self.WINMovie.start()


