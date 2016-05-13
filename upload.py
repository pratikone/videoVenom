#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, math
from PyQt4 import QtGui, QtCore
import requests
import simplejson
import upload_ui
import argparse
import uploadvideo as uv
import videoVimeo


# Shows the preview window showcasing the changes made in the editor window
class Upload(QtGui.QWizard) :

    closeApp = QtCore.pyqtSignal() #signal , slot to be with caller

    def __init__(self, ui):
        super(Upload, self).__init__()
        self.ui = ui
        self.list_of_syn = None
        self.youtubeObj = None
        

    def setup_connections(self) :
        self.ui.seedTagBtn.clicked.connect( self.populateTextBoxWithSynonyms )
        self.ui.youtubeBtn.clicked.connect( self.authenticateYoutube )
        self.ui.vimeoBtn.clicked.connect( self.authenticateVimeo )

    def getSynonyms( self, seedTag ):
        resp =  requests.get("http://suggestqueries.google.com/complete/search?client=youtube&ds=yt&client=firefox&q=" + str(seedTag))
        list_of_syn = simplejson.loads(str(resp.text))[1] # [0] is Query word
        return list_of_syn
        
    def populateTextBoxWithSynonyms( self ) :
        seedTag = self.ui.seedTagTextBox.text()
        self.list_of_syn = self.getSynonyms( seedTag )
        string_of_syn = ",".join( self.list_of_syn )
        self.ui.textEdit.setText( string_of_syn )

    def authenticateYoutube( self ):
        args = argparse.Namespace(file="",title="",description="",keywords="",category="",privacyStatus="",auth_host_name='localhost', auth_host_port=[8080, 8090],logging_level='ERROR', noauth_local_webserver=False)
        self.youtubeObj = uv.authenticateWithYoutube(args)
        if self.youtubeObj is not None :
            self.ui.youtubeBtn.setText("Auth successful")

    def authenticateVimeo(self) :
        videoVimeo.caller = self.caller
        videoVimeo.requestOAuth()
        self.ui.vimeoBtn.setText("Auth successful")



    def accept(self):  # gets triggered on exiting the wizard
        if self.list_of_syn : 
            self.caller.string_of_tags = str(self.ui.textEdit.toPlainText())
        else :
            self.caller.string_of_tags = None
        
        #add youtube, vimeo etc here
        self.caller.youtubeObj = self.youtubeObj
        self.caller.showPublishWidget()
        self.closeWidget()

    def closeEvent(self, event) :
        self.closeWidget()

    def closeWidget(self) :
        self.closeApp.emit()
        self.close()







def showUpload( caller  ) :
    ui = upload_ui.Ui_Wizard()
    widget = Upload( ui )
    ui.setupUi(widget)
    widget.setup_connections()
    widget.caller = caller
    if caller is not None :
        widget.setGeometry( caller.geometry() )
        widget.show()
        widget.caller.hide()
    widget.show()
    return widget



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = showUpload(None)
    sys.exit(app.exec_())


     
