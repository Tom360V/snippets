; -----------------------------------------------------------------------------
; Description: Wait for notepad to open, enter a text and save the file (somewhere)
; Note: There is a nice loop which will do this forever :)
; -----------------------------------------------------------------------------

; -----------------------------------------------------------------------------
; Includes
; -----------------------------------------------------------------------------
#include <Date.au3>
#include <MsgBoxConstants.au3>

; -----------------------------------------------------------------------------
; My local variable
; -----------------------------------------------------------------------------
Local $title            = "TKE"
Local $language         = "NL"
Local $appName          = "Notepad"
Local $appTitle         = "Untitled"
Local $appSaveTitle     = "Save As"
Local $buttonSave       = "!s"
Local $newFilename      = "blabla"

; -----------------------------------------------------------------------------
; Overrule defaults when language is dutch
; -----------------------------------------------------------------------------
If "NL" == $language Then
   $appName         = "Kladblok"
   $appTitle        = "Naamloos"
   $appSaveTitle    = "Opslaan als"
   $buttonSave      = "!p"
EndIf

; -----------------------------------------------------------------------------
; Application
; -----------------------------------------------------------------------------

MsgBox($MB_OK, $title, "Please open " & $appName)

While 1
   WinWaitActive($appTitle & " - " & $appName)
   Send("This is some text, blablabla...." & @LF )
   Send("And yes i can save this file automatically!")

   ; Close window, with an unsavedd file. Notepad will ask to save the file
   WinClose($appTitle & " - " & $appName)

   ; Wait for save confirmation window and choose to save the file
   WinWaitActive($appName)
   Send($buttonSave)                                                                ; Click "Save", one wait to click a button

   ; Wait for "Save As" window, enter filename and press the save button
   WinWaitActive($appSaveTitle)
   $filename = $newFilename & StringReplace(_NowDate(), "-", "") & "_" & StringReplace(_NowTime(),":","") & ".txt"
   ControlSetText($appSaveTitle, "", "[CLASS:ComboBox; INSTANCE:1]", $filename)     ; Enter new filename
   ControlClick  ($appSaveTitle, "", "[CLASS:Button;   INSTANCE:2]")                ; Click "Save" button, another wait to click a button

   ; Close window, with a saved file
   WinClose($appTitle & " - " & $appName)
WEnd
