@pyinstaller -w -F .\main.py -p .\venv\Lib\site-packages\
@pause
@copy .\dist\main.exe C:\Users\%USERNAME%\Desktop\SysMonitor.exe