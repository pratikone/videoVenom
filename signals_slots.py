import sys
import os
import basic_ui
import signals_slots
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon 


class Signal_Slots :

    def __init__(self) :
        pass

    def open_file( self, window, ui) :
        file = QtGui.QFileDialog.getOpenFileName(window, 'Open movie file')
        unified_file = os.path.normpath(unicode(file)) 
        mediaSource = Phonon.MediaSource( unified_file )
        ui.videoPlayer.load( mediaSource )
        print unified_file

    def start_playback( self, window, ui ) :
        ui.videoPlayer.play()

    def stop_playback( self, window, ui ) :
        ui.videoPlayer.stop()

 