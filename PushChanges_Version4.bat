@echo off
REM Automatischer Commit und Push mit Zeitstempel und Nummerierung

REM Hole das Datum im Format YYYY-MM-DD
for /f "tokens=2 delims= " %%a in ('date /t') do set mydate=%%a
REM Hole die Uhrzeit im Format HH-MM-SS
for /f "tokens=1-2 delims= " %%a in ('time /t') do set mytime=%%a_%%b

REM Zähle die Commits mit "Auto-Commit [Datum]" heute
git log --oneline --grep="Auto-Commit %mydate%" > tmp_commit_count.txt
set /a count=0
for /f %%x in (tmp_commit_count.txt) do set /a count+=1
set /a count+=1
del tmp_commit_count.txt

REM Zu Git hinzufügen
git add .

REM Commit mit Zeitstempel und Nummerierung
git commit -m "Auto-Commit %mydate% %mytime% #%count%"

REM Push zum Remote
git push

echo Push erfolgreich!
exit /b