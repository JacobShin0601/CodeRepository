#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Home::Escape
Escape::`
CapsLock::RAlt
PgUp::#+s
PgDn::Delete


#MaxThreadsPerHotkey 3

^+=::
Toggle := !Toggle
Loop
{
	If (!Toggle)
		Break
	Click
	Sleep 83 ; Make this number higher for slower clicks, lower for faster.
}
Return


^+Space::
{
 Send, ^c
 Sleep 100
 Run, https://www.google.com/search?q=%clipboard%
 Return
}


^+d::
{
 Send, ^c
 Sleep 100
 Run, https://dict.naver.com/search.dict?dicQuery=%clipboard%&query=%clipboard%&target=dic&ie=utf8&query_utf=&isOnlyViewEE=
 Return
}

^+t::
{
 Send, ^c
 Run, https://translate.google.com.vn/?hl=en&sl=auto&tl=en&op=translate
 Return
}


;Auto select items which are shown in the monitor (after filtering out)
^+s::
{
 SendInput, {LAlt}
 Sleep 100
 SendInput, {H}
 Sleep 100
 SendInput, {F}
 Sleep 100
 SendInput, {D}
 Sleep 100
 SendInput, {S}
 Sleep 100
 SendInput, {Y}
 Sleep 100
 SendInput, {Enter}

 Return
}

;Merge cells
^+m::
{
 SendInput, {LAlt}
 Sleep 100
 SendInput, {H}
 Sleep 100
 SendInput, {M}
 Sleep 100
 SendInput, {M}
 Sleep 100
 SendInput, {Enter}

 Return
}

;Ordering - ascending
^+o::
{
 SendInput, {LAlt}
 Sleep 100
 SendInput, {A}
 Sleep 100
 SendInput, {S}
 Sleep 100
 SendInput, {A}

 Return
}

;Ordering - descending
^+l::
{
 SendInput, {LAlt}
 Sleep 100
 SendInput, {A}
 Sleep 100
 SendInput, {S}
 Sleep 100
 SendInput, {D}

 Return
}

;Ordering - Remove filter
^+p::
{
 SendInput, {LAlt}
 Sleep 100
 SendInput, {A}
 Sleep 100
 SendInput, {C}
 Sleep 100

 Return
}

;Insert row
^+u::
{
 SendInput, {LAlt}
 Sleep 100
 SendInput, {H}
 Sleep 100
 SendInput, {I}
 Sleep 100
 SendInput, {R}
 Sleep 100

 Return
}

;Insert column
^+i::
{
 SendInput, {LAlt}
 Sleep 100
 SendInput, {H}
 Sleep 100
 SendInput, {I}
 Sleep 100
 SendInput, {C}
 Sleep 100

 Return
}

;Delete row
^+j::
{
 SendInput, {LAlt}
 Sleep 100
 SendInput, {H}
 Sleep 100
 SendInput, {D}
 Sleep 100
 SendInput, {R}
 Sleep 100

 Return
}

;Delete column
^+k::
{
 SendInput, {LAlt}
 Sleep 100 
 SendInput, {H}
 Sleep 100
 SendInput, {D}
 Sleep 100
 SendInput, {C}
 Sleep 100

 Return
}


^+f::Run "C:\Program Files (x86)\Q-Dir\Q-Dir.exe"

;+NumpadAdd:: Send {Volume_Up}
;+NumpadSub:: Send {Volume_Down}
;break::Send {Volume_Mute}
;return



; https://docs.microsoft.com/de-de/windows/desktop/Intl/language-identifier-constants-and-strings
;F7:: SetDefaultKeyboardLang(0x02809) ; English
;PgUp:: SetDefaultKeyboardLang(0x412)  ; Korean
;PgDn:: SetDefaultKeyboardLang(0x804)  ; Chinese

; https://autohotkey.com/boards/viewtopic.php?f=6&t=18519
SetDefaultKeyboardLang(LocaleID){
	Static SPI_SETDEFAULTINPUTLANG := 0x005A, SPIF_SENDWININICHANGE := 2	
	Lan := DllCall("LoadKeyboardLayout", "Str", Format("{:08x}", LocaleID), "Int", 0)
	VarSetCapacity(binaryLocaleID, 4, 0)
	NumPut(LocaleID, binaryLocaleID)
	DllCall("SystemParametersInfo", "UInt", SPI_SETDEFAULTINPUTLANG, "UInt", 0, "UPtr", &binaryLocaleID, "UInt", SPIF_SENDWININICHANGE)	
	WinGet, windows, List
	Loop % windows {
		PostMessage 0x50, 0, % Lan, , % "ahk_id " windows%A_Index%
	}
}