@echo off
if "%1" == "-restart" goto restart
tasklist | find "python" 
if "%errorlevel%" == "0" (
    start C:\security.bat
	taskkill /f /im pythonw.exe >nul
    exit
)
title Zynth Securitas ^| Made by: Zipp
taskkill /f /im explorer.exe >nul
taskkill /f /im discord.exe >nul
taskkill /f /im msedge.exe >nul
taskkill /f /im chrome.exe >nul
taskkill /f /im opera.exe >nul
taskkill /f /im javaw.exe >nul
taskkill /f /im MinecraftLauncher.exe >nul
if NOT exist "%temp%\restart7488593.dll" echo X > %temp%\restart7488593.dll
cls
echo.
echo.
call :banner
echo.
echo    [[91m![0m] Byl aktivovan bezpecnostni protokol
echo    [[91m![0m] Tento protokol byl aktivovan na vzdalene ovladani
echo.
echo    [[96mi[0m] Pro odemceni pocitace zadejte bezpecnostni heslo
set /p "pass=[0m   > "
goto encrypt


:restart
title Zynth Securitas ^| Made by: Zipp
taskkill /f /im explorer.exe >nul
taskkill /f /im discord.exe >nul
taskkill /f /im msedge.exe >nul
taskkill /f /im chrome.exe >nul
taskkill /f /im opera.exe >nul
taskkill /f /im javaw.exe >nul
taskkill /f /im MinecraftLauncher.exe >nul
cls
echo.
echo.
call :banner
echo.
echo    [[91m![0m] Byl aktivovan bezpecnostni protokol
echo    [[91m![0m] Tento protokol nebyl aktivovan na vzdalene ovladani
echo.
echo    [[91m![0m] Je dost mozne ze se protokol aktivoval protoze pocitac
echo        byl restartovan behem bezpecnostniho protokolu.
echo.
echo    [[96mi[0m] Pro odemceni pocitace zadejte bezpecnostni heslo
set /p "pass=[0m   > "
goto encrypt



:banner
echo                         [36m_____           _   _       ____                       _ _         
echo                        ^|__  /   _ _ __ ^| ^|_^| ^|__   / ___^|  ___  ___ _   _ _ __(_) ^|_ _   _ 
echo                          / / ^| ^| ^| '_ \^| __^| '_ \  \___ \ / _ \/ __^| ^| ^| ^| '__^| ^| __^| ^| ^| ^|
echo                         / /^| ^|_^| ^| ^| ^| ^| ^|_^| ^| ^| ^|  ___) ^|  __/ (__^| ^|_^| ^| ^|  ^| ^| ^|_^| ^|_^| ^|
echo                        /____\__, ^|_^| ^|_^|\__^|_^| ^|_^| ^|____/ \___^|\___^|\__,_^|_^|  ^|_^|\__^|\__, ^|
echo                             ^|___/                                                    ^|___/ [0m
exit /b 0

:encrypt
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
::set Encrypt=Nothing
(set CHAR[a]=UDFM45) & (set CHAR[b]=H21DGF) & (set CHAR[c]=FDH56D) & (set CHAR[d]=FGS546) & (set CHAR[e]=JUK4JH)
(set CHAR[f]=ERG54S) & (set CHAR[g]=T5H4FD) & (set CHAR[h]=RG641G) & (set CHAR[i]=RG4F4D) & (set CHAR[j]=RT56F6)
(set CHAR[k]=VCBC3B) & (set CHAR[l]=F8G9GF) & (set CHAR[m]=FD4CJS) & (set CHAR[n]=G423FG) & (set CHAR[o]=F45GC2)
(set CHAR[p]=TH5DF5) & (set CHAR[q]=CV4F6R) & (set CHAR[r]=XF64TS) & (set CHAR[s]=X78DGT) & (set CHAR[t]=TH74SJ)
(set CHAR[u]=BCX6DF) & (set CHAR[v]=FG65SD) & (set CHAR[w]=4KL45D) & (set CHAR[x]=GFH3F2) & (set CHAR[y]=GH56GF)
(set CHAR[z]=45T1FG) & (set CHAR[1]=D4G23D) & (set CHAR[2]=GB56FG) & (set CHAR[3]=SF45GF) & (set CHAR[4]=P4FF12)
(set CHAR[5]=F6DFG1) & (set CHAR[6]=56FG4G) & (set CHAR[7]=USGFDG) & (set CHAR[8]=FKHFDG) & (set CHAR[9]=IFGJH6)
(set CHAR[0]=87H8G7) & (set CHAR[@]=G25GHF) & (set CHAR[#]=45FGFH) & (set CHAR[$]=75FG45) & (set CHAR[*]=54GDH5)
(set CHAR[(]=45F465) & (set CHAR[.]=HG56FG) & (set CHAR[,]=DF56H4) & (set CHAR[-]=F5JHFH) & (set CHAR[ ]=SGF4HF)
(set CHAR[\]=45GH45) & (set CHAR[/]=56H45G)
set "Encrypt=%pass%"
cls
set Encrypt2=%Encrypt%
set "EncryptOut="
:encrypt2
set char=%Encrypt2:~0,1%
set Encrypt2=%Encrypt2:~1%
set EncryptOut=%EncryptOut%!CHAR[%char%]!
if not "%Encrypt2%"=="" goto encrypt2
if "%EncryptOut%" == "YOUR_KEY" goto unlock
echo X=MsgBox("Spatne heslo", 0+64, "Zynth Securitas") >> %temp%\msg.vbs
start %temp%\msg.vbs
timeout /t 0 /nobreak >nul
del %temp%\msg.vbs
timeout /t 2 /nobreak >nul
shutdown -s -t 0

:unlock
if exist "%temp%\restart7488593.dll" del %temp%\restart7488593.dll
echo X=MsgBox("Zarizeni bylo odemcen!", 0+64, "Zynth Securitas") >> %temp%\msg.vbs
start %temp%\msg.vbs
timeout /t 1 /nobreak >nul
del %temp%\msg.vbs
start explorer.exe
exit