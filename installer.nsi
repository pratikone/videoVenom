; example1.nsi
;
; This script is perhaps one of the simplest NSIs you can make. All of the
; optional settings are left to their default settings. The installer simply 
; prompts the user asking them where to install, and drops a copy of example1.nsi
; there. 

;--------------------------------

; The name of the installer
Name "Video Venom installer"

; The file to write
OutFile "videoVenom_installer.exe"

; The default installation directory
InstallDir $DESKTOP\videoVenom

; Request application privileges for Windows Vista
RequestExecutionLevel user

;--------------------------------

; Pages

Page directory
Page instfiles

;--------------------------------

; The stuff to install
Section "" ;No components page, name is not important

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  # create the uninstaller
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  # create a shortcut named "video venom" in the start menu programs directory
  # point the new shortcut at the program uninstaller
  
  ; Put file there
  File /r "build\*.*"
  File /r "dist\*.*"

  CreateShortCut "$SMPROGRAMS\Video Venom.lnk" "$INSTDIR\window\window.exe"  
  CreateShortCut "$SMPROGRAMS\Uninstall Video Venom.lnk" "$INSTDIR\uninstall.exe"  

  
SectionEnd ; end the section

# uninstaller section start
Section "uninstall"
 
    # first, delete the uninstaller
    Delete "$INSTDIR\uninstall.exe"
 
    # second, remove the link from the start menu
    Delete "$SMPROGRAMS\Video Venom.lnk"
    Delete "$SMPROGRAMS\Uninstall Video Venom.lnk"
 	RMDir /r "$INSTDIR\window"
# uninstaller section end
SectionEnd