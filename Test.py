import subprocess
"""
x= subprocess.getoutput(['F:\Sego Project\Data Hiding - LAB\Data Hiding - LAB\Section 9\Tools\lads\lads.exe',
                  'F:\\'
                  ])
print(x)
"""
import sys
import platform
from PySide2 import QtCore, QtGui,  QtWidgets
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtGui import QMovie
from PySide2.QtWidgets import *
from ui_Form_progress import Ui_SplashScreen
from ui_Stego_main import Ui_Stego_main
from ui_Gif_Hide import  Ui_GifShuf_form
from stegano import lsb
from os import startfile
import subprocess

file = str(QFileDialog.getExistingDirectory("F:\Sego Project\Sego Project"))
print(file)