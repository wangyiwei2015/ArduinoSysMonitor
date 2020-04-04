@echo off
set msg=%1
if "%msg%"=="" (
    set /p msg="Commit Message with quotation marks: "
)
git add *
git commit -m %msg%
git push