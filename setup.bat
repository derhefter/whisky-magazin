@echo off
chcp 65001 >nul
echo.
echo  ══════════════════════════════════════════
echo   WHISKY MAGAZIN - INSTALLATION
echo  ══════════════════════════════════════════
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  FEHLER: Python ist nicht installiert!
    echo.
    echo  Bitte installiere Python von:
    echo  https://www.python.org/downloads/
    echo.
    echo  WICHTIG: Haken setzen bei "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo  Python gefunden:
python --version
echo.

cd /d "%~dp0"

echo  Erstelle virtuelle Umgebung...
if not exist "venv" (
    python -m venv venv
    echo  Virtuelle Umgebung erstellt!
) else (
    echo  Virtuelle Umgebung existiert bereits.
)
echo.

echo  Installiere Pakete...
call venv\Scripts\activate.bat
pip install -r requirements.txt --quiet
echo  Pakete installiert!
echo.

if not exist "config.json" (
    copy config.example.json config.json >nul
    echo  config.json erstellt!
    echo.
    echo  ══════════════════════════════════════════
    echo   NAECHSTER SCHRITT:
    echo  ══════════════════════════════════════════
    echo.
    echo  1. Oeffne config.json mit einem Texteditor
    echo  2. Ersetze "sk-DEIN_OPENAI_API_KEY" mit
    echo     deinem echten OpenAI API-Key
    echo  3. Speichern und dann starten.bat ausfuehren
    echo.
) else (
    echo  config.json existiert bereits.
    echo.
    echo  ══════════════════════════════════════════
    echo   INSTALLATION ABGESCHLOSSEN!
    echo  ══════════════════════════════════════════
    echo.
    echo  Starte mit: starten.bat
    echo.
)

if not exist "articles" mkdir articles
if not exist "site" mkdir site

pause
