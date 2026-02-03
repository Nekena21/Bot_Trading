@echo off
chcp 65001 > nul
cls

echo ==========================================
echo     BOT_TRADING - Screen Watcher
echo ==========================================
echo.
echo Vérification de l'environnement...
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERREUR: Python n'est pas installé ou non trouvé dans PATH
    echo.
    echo Téléchargez Python 3.10+ depuis https://www.python.org
    echo Assurez-vous de cocher "Add Python to PATH" lors de l'installation
    echo.
    pause
    exit /b 1
)

echo ✅ Python détecté

REM Vérifier si les dépendances sont installées
python -c "import cv2, numpy, mss, pyautogui, PIL, playsound" >nul 2>&1
if errorlevel 1 (
    echo.
    echo 📦 Installation des dépendances requises...
    echo.
    python -m pip install --upgrade pip -q
    python -m pip install opencv-python numpy mss pyautogui pandas pillow playsound -q
    if errorlevel 1 (
        echo.
        echo ❌ ERREUR: L'installation des dépendances a échoué
        echo Vérifiez votre connexion Internet et essayez à nouveau
        pause
        exit /b 1
    )
    echo ✅ Dépendances installées avec succès
) else (
    echo ✅ Toutes les dépendances sont déjà installées
)

echo.
echo ==========================================
echo     Démarrage du Bot...
echo ==========================================
echo.
echo 📌 Instructions importantes:
echo.
echo 1. Assurez-vous que Pocket Option est ouvert
echo 2. Positionnez le graphique au même endroit que lors de la config
echo 3. Ne déplacez pas la fenêtre pendant le fonctionnement
echo 4. Gardez un zoom constant
echo.
echo Pour arrêter le bot: appuyez sur Ctrl + C
echo.
echo ==========================================
echo.

REM Lancer le bot
python trading_bot_cv\main.py

if errorlevel 1 (
    echo.
    echo ❌ ERREUR: Le bot s'est arrêté avec une erreur
    echo.
    pause
    exit /b 1
)

pause
