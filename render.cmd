@echo off
REM Render a CV HTML to PDF.  Usage:  render out\Gaurav_Bhatia_CV_Enpal.html
REM  render roles   renders the eight ready-made role CVs in roles\
REM No argument renders every HTML in out\ plus the base template.
REM [EMAIL] and [PHONE] placeholders are filled from private\contact.md, which is never committed.
REM The photo comes from assets\photo.jpg (public) and is embedded so the PDF carries it.
setlocal
set CHROME=%ProgramFiles%\Google\Chrome\Application\chrome.exe
if not exist "%CHROME%" set CHROME=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe
if not exist "%CHROME%" echo Chrome not found - open the HTML and press Ctrl+P instead. & exit /b 1
if not exist "%~dp0private\contact.md" echo WARNING: private\contact.md missing - the PDF will show [EMAIL] and [PHONE].

if /i "%~1"=="roles" goto roles
if not "%~1"=="" ( call :one "%~f1" & exit /b )
call :one "%~dp0templates\base.html"
for %%f in ("%~dp0out\*.html") do call :one "%%~ff"
exit /b

:roles
for %%f in ("%~dp0roles\*.html") do call :one "%%~ff"
exit /b

:one
set SRC=%~1
powershell -NoProfile -Command ^
  "$c = Get-Content -Raw -Encoding UTF8 '%~dp0private\contact.md' -ErrorAction SilentlyContinue;" ^
  "$mail = [regex]::Match($c,'\|\s*Email\s*\|\s*([^|]+?)\s*\|').Groups[1].Value;" ^
  "$tel  = [regex]::Match($c,'\|\s*Mobile\s*\|\s*([^|]+?)\s*\|').Groups[1].Value;" ^
  "$h = Get-Content -Raw -Encoding UTF8 '%~1';" ^
  "if ($mail) { $h = $h -replace '\[EMAIL\]', ('<a href=\"mailto:' + $mail + '\">' + $mail + '</a>') }" ^
  "if ($tel)  { $h = $h -replace '\[PHONE\]', $tel }" ^
  "$pic = '%~dp0assets\photo.jpg';" ^
  "if (Test-Path $pic) { $b64 = [Convert]::ToBase64String([IO.File]::ReadAllBytes($pic));" ^
  "  $h = $h.Replace('../assets/photo.jpg', 'data:image/jpeg;base64,' + $b64) }" ^
  "[IO.File]::WriteAllText('%TEMP%\cvrender.html', $h, (New-Object Text.UTF8Encoding $false))"
if exist "%TEMP%\cvrender.html" set SRC=%TEMP%\cvrender.html
"%CHROME%" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="%~dp0out\%~n1.pdf" "file:///%SRC%" 2>nul
del "%TEMP%\cvrender.html" 2>nul
echo   out\%~n1.pdf
exit /b
