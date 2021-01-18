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
from ui_LadsGui import Ui_LadsGUI
from stegano import lsb
from ui_Mp3Hide import Ui_AudioGUI_form
from os import startfile
import  urllib.request
import webbrowser

import subprocess

## GLOBAL
counter = 0

## FORM CENTRAL / POS SPLASH
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Stego_main()
        self.ui.setupUi(self)
        self.FilePath = ''
        self.MessageTXT = ''
        self.secret = ''
        self.movie = QMovie("")

        # Hide All frames to visable it when click button
        self.ui.LSB_Frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Video_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(False)
        self.ui.ADS_BTN_Frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)



        #All Buttuns function




        self.ui.Browse_Btn.clicked.connect(lambda: self.OpenfileExplorer())

        self.ui.Hide_BTN.clicked.connect(lambda: self.LSBHide())
        self.ui.STool_BTN.clicked.connect(lambda: self.OpenStool())
        self.ui.XiaoStego_BTN.clicked.connect(lambda: self.Openxiaotool())
        self.ui.StegoXPlus_BTN.clicked.connect(lambda: self.Openstegoxplustool())
        self.GifTool = GifShufWindow()
        self.ui.GifShufTool_BTN.clicked.connect(lambda: self.OpenGIFTool())
        self.ui.DeEggerTool_BTN.clicked.connect(lambda: self.openDeEggerTool())
        self.ui.DeepSoundTool_Btn.clicked.connect(lambda: self.openDeepTool())
        self.ui.OurSecret_BTN.clicked.connect(lambda: self.OpenOurSecret())
        self.ui.OurSecret_BTN_2.clicked.connect(lambda: self.OpenOurSecret())
        self.ui.wbStego4open_BTN.clicked.connect(lambda: self.openBWOtool())
        self.ui.DetectingAdsFiles_BTN.clicked.connect(lambda: self.OpenADSFrame())
        self.ui.ADSViewer_BTN.clicked.connect(lambda: self.OpenADSViewer())
        self.ui.GMARTool_BTN.clicked.connect(lambda : self.OpenGamer())
        self.ui.DeskEncryption_BTN.clicked.connect(lambda: self.OpenVaraCrypt())
        self.ui.PassSafe_BTN.clicked.connect(lambda : self.OpenPasswordSafe())
        self.ui.STG_BTN.clicked.connect(lambda: self.OpenSTG())
        self.ui.Thumbnail_BTN.clicked.connect(lambda: self.OpenThumbnail())
        self.ui.HideINAds_BTN.clicked.connect(lambda : self.ADSGIF())
        self.ui.HideINWinRegistry_BTN.clicked.connect(lambda : self.WINGIF())
        self.ui.MSOffice_BTN.clicked.connect(lambda : self.ui.MSGIF())
        self.ui.HTML_BTN.clicked.connect(lambda : self.ui.HIdeINHtml())

        #Open home frame
        self.ui.Home_BTN.clicked.connect(lambda : self.OpenHome())
        #Open IMG Frame
        self.ui.ImagesTools_BTN.clicked.connect(lambda :self.OpenIMGFrame())

        #Lsb Show frame
        self.ui.img_BTN.clicked.connect(lambda : self.OpenLsbTool())

        #video frame show
        self.ui.video_BTN.clicked.connect(lambda: self.OpenVideoFrame())

        #Audio form show
        self.ui.audio_BTN.clicked.connect(lambda: self.OpenAudioFrame())

        #Txt form show
        self.ui.txt_BTN.clicked.connect(lambda: self.OpenTXTFrame())

        #Exe form show
        self.ui.exe_BTN.clicked.connect(lambda: self.OpenEXEFrame())

        #pdf form show
        self.ui.pdf_BTN.clicked.connect(lambda: self.OpenPDFFrame())

        #more form show
        self.ui.More_BTN.clicked.connect(lambda: self.OpenMoreFrame())

        #Lads Gui
        self.GUILADS = LadsGUIWindow()
        self.ui.lads_BTN.clicked.connect(lambda : self.GUILADS.show())

        #Audio CLi GUI
        self.ui.Mp3StegoTool_BTN.clicked.connect(lambda : self.GUIAudioMp3())
        self.ui.StegHideTool_BTN.clicked.connect(lambda : self.GUIAudioSteg())



    #Mp3stego Gui
    def GUIAudioMp3(self):
        self.AudioGui = AudioCLIWindow()
        self.AudioGui.show()
        self.AudioGui.ui.Mp3Encode.setVisible(True)
    #StegHide Gui
    def GUIAudioSteg(self):
        self.AudioGUI = AudioCLIWindow()
        self.AudioGUI.show()
        self.AudioGUI.ui.StighideEncode.setVisible(True)

    #Lsb Function to hide massage in image
    def LSBHide(self):
        self.MessageTXT = self.ui.Message_txt.toPlainText()
        self.FilePath = self.ui.PathFile.text()
        self.secret = lsb.hide(self.FilePath,self.MessageTXT)
        self.secret.save('F:\Sego Project\Sego Project\Gif output\secret_image.jpg')
        self.ui.label_32.setPixmap(QtGui.QPixmap('F:\Sego Project\Sego Project\Gif output\secret_image.jpg'))
        self.ui.Message_txt.clear()
        self.ui.PathFile.clear()


    #Function to Open Stool
    def OpenStool(self):
        subprocess.call('F:\Sego Project\Tools\S-Tools\s-tools4\S-Tools.exe')

    #Functoion to open xiaotool
    def Openxiaotool(self):
        subprocess.call('C:\Program Files (x86)\Xiao Stenography\Xiao_Steg.exe')

     #Function to open stego_x_plus
    def Openstegoxplustool(self):
        subprocess.call('F:\Sego Project\Tools\SteganographyX Plus\StgP.exe')



    #Function to open GIF tool
    def OpenGIFTool(self):
        self.GifTool.show()


     #Function to open DeEgger tool
    def openDeEggerTool(self):
        subprocess.call('C:\Program Files (x86)\ZASI\DeEgger Embedder\DE.exe')


     #Function to open DeepTool
    def openDeepTool(self):
        subprocess.call('C:\Program Files (x86)\DeepSound 2.0\DS.exe')

    #Function to open Oursecret
    def OpenOurSecret(self):
        subprocess.call('F:\Sego Project\OurSecret.exe')


    #Function to open BWOtool
    def openBWOtool(self):
        #subprocess.call('F:\Sego Project\Tools\wbs43open-win32\wbs43open-win32\wbStego4.3open.exe')
        webbrowser.open("http://www.bailer.at/wbstego/pr_4ixopen.htm")

    #Function to open ADS
    def OpenADSFrame(self):
        self.ui.ADS_TXT_Frame.setVisible(False)
        self.ui.ADS_BTN_Frame.setVisible(True)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)


    #Function to open ADS_VIewer
    def OpenADSViewer(self):
        subprocess.call('C:\Program Files\SoftecDesign\ADSViewer\ADSView.exe')
    #Function to open Gmer
    def OpenGamer(self):
        startfile('F:\Sego Project\Tools\gmer.exe')

    #Function to open vara_crypt
    def OpenVaraCrypt(self):
        subprocess.call('F:\Sego Project\Data Hiding - LAB\Data Hiding - LAB\Section 8\Tools\VeraCrypt\VeraCrypt.exe')
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
     #Function to open Password_safe
    def OpenPasswordSafe(self):
        subprocess.call('C:\Program Files\Password Safe\pwsafe.exe')
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
     #Function to open STG
    def OpenSTG(self):
        subprocess.call('C:\Program Files (x86)\stg\CacheAudit\cacheaudit.exe')
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
     #Function to open thumbnail
    def OpenThumbnail(self):
        subprocess.call('F:\Sego Project\Data Hiding - LAB\Data Hiding - LAB\Section 9\Tools\Thumbnail Database Viewer\ThumbViewer.exe')
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)

    #FUnction to open FileExplorer
    def OpenfileExplorer(self):
        self.FilePath = QFileDialog.getOpenFileName(self,'Open folder','F:\Sego Project\Sego Project','JPEG (*.JPG)')
        self.ui.PathFile.setText(self.FilePath[0])
        self.ui.label_31.setPixmap(QtGui.QPixmap(self.FilePath[0]))
    #Fuction to open ADS_GIF
    def ADSGIF(self):
        self.ui.HideAdsGIF.setVisible(True)
        self.ui.HideRegistryGIF.setVisible(False)
        #Function to open WIN_GIF
    def WINGIF(self):
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(True)
     #FUnction to open home
    def OpenHome(self):
        self.ui.Hello_Message.setVisible(True)
        self.ui.label_4.setVisible(True)
        self.ui.Logo.setVisible(True)
        self.ui.LSB_Frame.setVisible(False)
        self.ui.Video_frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
     #Function to open lsb_tool
    def OpenLsbTool(self):
        self.ui.Hello_Message.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.Logo.setVisible(False)
        self.ui.LSB_Frame.setVisible(True)
        self.ui.Video_frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
        #Function to open IMG FRame
    def OpenIMGFrame(self):
        self.ui.Hello_Message.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.Logo.setVisible(False)
        self.ui.LSB_Frame.setVisible(False)
        self.ui.IMG_frame.setVisible(True)
        self.ui.Video_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
        #Function to open video frame
    def OpenVideoFrame(self):
        self.ui.Hello_Message.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.Logo.setVisible(False)
        self.ui.LSB_Frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Video_frame.setVisible(True)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
        # Function to open audio frame
    def OpenAudioFrame(self):
        self.ui.Hello_Message.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.Logo.setVisible(False)
        self.ui.LSB_Frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Video_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(True)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
        # Function to open txtFrame frame
    def OpenTXTFrame(self):
        self.ui.Hello_Message.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.Logo.setVisible(False)
        self.ui.LSB_Frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Video_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(True)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)


    # Function to open exe frame
    def OpenEXEFrame(self):
        self.ui.Hello_Message.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.Logo.setVisible(False)
        self.ui.LSB_Frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Video_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(True)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
        # Function to open PDF frame
    def OpenPDFFrame(self):
        self.ui.Hello_Message.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.Logo.setVisible(False)
        self.ui.LSB_Frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Video_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(True)
        self.ui.More_frame.setVisible(False)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)
    # Function to open more frame
    def OpenMoreFrame(self):
        self.ui.Hello_Message.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.ADS_BTN_Frame.setVisible(False)
        self.ui.ADS_TXT_Frame.setVisible(True)
        self.ui.Logo.setVisible(False)
        self.ui.LSB_Frame.setVisible(False)
        self.ui.IMG_frame.setVisible(False)
        self.ui.Video_frame.setVisible(False)
        self.ui.Audio_frame.setVisible(False)
        self.ui.TXT_frame.setVisible(False)
        self.ui.EXE_frame.setVisible(False)
        self.ui.PDF_frame.setVisible(False)
        self.ui.More_frame.setVisible(True)
        self.ui.HideAdsGIF.setVisible(False)
        self.ui.HideRegistryGIF.setVisible(False)

#GifShuf Form Class
class GifShufWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_GifShuf_form()
        self.ui.setupUi(self)
        self.fname = ''
        self.ClearData = ''
        self.SecretMessage = ''
        self.ui.Message_txt.clear()
        self.ui.Path_txt.clear()
        self.ui.Browse_Btn.clicked.connect(lambda : self.OpenfileExplorer())
        self.ui.GIFHide_BTN.clicked.connect(lambda : self.HideData())
        self.ui.DecodeGif_BTN.clicked.connect(lambda : self.getData())

    def OpenfileExplorer(self):
        self.fname = QFileDialog.getOpenFileName(self,'Open file','F:\Sego Project\Sego Project','GIF files (*.gif)')
        self.ui.Path_txt.setText(self.fname[0])
    def HideData(self):
        self.SecretMessage = self.ui.Message_txt.toPlainText()
        self.FilePath = self.ui.Path_txt.text()
        self.ui.Message_txt.clear()
        self.ui.Path_txt.clear()
        subprocess.Popen(['F:\Sego Project\Tools\GIFShuff-Tool\GIFSHUF.exe',
                          '-CS',
                          '-m',
                          self.SecretMessage,
                          '-p',
                          'pass',
                          self.FilePath,
                          'F:\Sego Project\Sego Project\Gif output\output2027.gif',
                          ])
        self.ui.Gifshulff_Stutus.setText('Done')

    def getData(self):
        self.FilePath = self.ui.Path_txt.text()
        self.ClearData= subprocess.getoutput(['F:\Sego Project\Tools\GIFShuff-Tool\GIFSHUF.exe',
                                  '-C',
                                  '-p',
                                  'pass',
                                  self.FilePath,
                                  ])
        self.ui.Gifshulff_Stutus.setText(self.ClearData)
        self.ui.Path_txt.clear()
#LADS From Class
class LadsGUIWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LadsGUI()
        self.ui.setupUi(self)
        self.PathFolder = ''
        self.Output = ''
        self.ui.pushButton.clicked.connect(lambda : self.View())
    def View(self):
        self.PathFolder = self.ui.PathFolder.text()
        self.Output = subprocess.getoutput(['F:\Sego Project\Data Hiding - LAB\Data Hiding - LAB\Section 9\Tools\lads\lads.exe',self.PathFolder])
        self.ui.textEdit.setText(self.Output)
#Mp3Stego and Steghide From Class
class AudioCLIWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui  = Ui_AudioGUI_form()
        self.ui.setupUi(self)
        self.ui.Stutus.setText('_')
        self.ui.Mp3Encode.setVisible(False)
        self.ui.StighideEncode.setVisible(False)
        self.WavPath = ''
        self.TxtPath = ''
        self.ui.CBrowse_BTN.clicked.connect(lambda : self.OpenWavExplorer())
        self.ui.Browse_Btn.clicked.connect(lambda : self.OpenTxtExplorer())
        self.ui.Mp3Encode.clicked.connect(lambda : self.Mp3Encode())
        self.ui.StighideEncode.clicked.connect(lambda : self.SteghideEncode())


    def OpenWavExplorer(self):
        self.wavname = QFileDialog.getOpenFileName(self,'Open wav file','F:\Sego Project\Sego Project','GIF files (*.wav)')
        self.ui.SelectCarrier.setText(self.wavname[0])
    def OpenTxtExplorer(self):
        self.txtname = QFileDialog.getOpenFileName(self,'Open file','F:\Sego Project\Sego Project','GIF files (*.txt)')
        self.ui.Path_txt.setText(self.txtname[0])

    def SteghideEncode(self):
        self.WavPath = self.ui.SelectCarrier.text()
        self.TxtPath = self.ui.Path_txt.text()
        subprocess.Popen(['F:\Sego Project\steghide\steghide.exe',
                          'embed',
                          '-cf',
                          self.WavPath,
                          '-ef',
                          self.TxtPath,
                          '-p',
                          '"password"'
                          ])
        self.ui.Stutus.setText('Done')
    def Mp3Encode(self):
        self.WavPath = self.ui.SelectCarrier.text()
        self.TxtPath = self.ui.Path_txt.text()
        subprocess.Popen(['F:\Sego Project\MP3Stego_1_1_19\MP3Stego\Encode.exe',
                          '-E',
                          self.TxtPath,
                          '-P',
                          'pass',
                          self.WavPath,
                          'F:\Sego Project\Sego Project\Gif output/out.MP3'
                          ])
        self.ui.Stutus.setText('Message Hiden')




## FORM SPLAH
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        """
        ## CREATE DROP SHADOWN EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        ## SET DROP SHADOWN EFFECT IN FRAME
        self.ui.dropShowdan.setGraphicsEffect(self.shadow)
        """
        # QTIMER START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(100)


        # CHANGE DESCRIPTION / labelSubName
        QtCore.QTimer.singleShot(1000, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\"> EXPLOITS</font>"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\"> DATABASE</font>"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\"> USER INTERFACE</font>"))

        ## SHOW MAIN WINDOWS
        self.show()
    def progress(self):
        global counter

        #SET VALUE TO PROGRESS
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEM AND OPEN THING
        if counter > 100:
            self.timer.stop()
            ## CREATE FORM CENTRAL
            self.main = MainWindow()
            ## SET DROP SHADOWN EFFECT IN FRAME
            #self.main.ui.frame.setGraphicsEffect(self.shadow)
            ## SHOW MAIN WINDOWS / FORM CENTRAL
            self.main.show()
            self.close()
        counter+=3




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())