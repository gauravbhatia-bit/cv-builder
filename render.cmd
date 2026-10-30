@echo off
REM Render a CV HTML to PDF.  Usage:  render out\Gaurav_Bhatia_CV_Enpal.html
REM No argument renders every HTML in out\ plus the base template.
REM [EMAIL] and [PHONE] placeholders are filled from private\contact.md, which is never committed.
setlocal
set CHROME=%ProgramFiles%\Google\Chrome\Application\chrome.exe
if not exist "%CHROME%" set CHROME=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe
if not exist "%CHROME%" echo Chrome not found - open the HTML and press Ctrl+P instead. & exit /b 1
if not exist "%~dp0private\contact.md" echo WARNING: private\contact.md missing - the PDF will show [EMAIL] and [PHONE].

if not "%~1"=="" ( call :one "%~f1" & exit /b )
call :one "%~dp0templates\base.html"
for %%f in ("%~dp0out\*.html") do call :one "%%~ff"
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
  "$pic = @(Get-ChildItem -Path '%~dp0private\photo.jpg','%~dp0private\photo.jpeg','%~dp0private\photo.png' -ErrorAction SilentlyContinue)[0];" ^
  "if ($pic) { $b64 = [Convert]::ToBase64String([IO.File]::ReadAllBytes($pic.FullName));" ^
  "  $mime = if ($pic.Extension -eq '.png') { 'image/png' } else { 'image/jpeg' };" ^
  "  $h = $h -replace '\[PHOTO\]', ('<img class=\"photo\" src=\"data:' + $mime + ';base64,' + $b64 + '\" alt=\"\">') }" ^
  "else { $h = $h -replace '\[PHOTO\]', '' }" ^
  "[IO.File]::WriteAllText('%TEMP%\cvrender.html', $h, (New-Object Text.UTF8Encoding $false))"
if exist "%TEMP%\cvrender.html" set SRC=%TEMP%\cvrender.html
"%CHROME%" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="%~dp0out\%~n1.pdf" "file:///%SRC%" 2>nul
del "%TEMP%\cvrender.html" 2>nul
echo   out\%~n1.pdf
exit /b
