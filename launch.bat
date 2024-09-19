@echo off

if exist .venv\ (
    echo Activating environment.
    call .venv/Scripts/activate.bat
) else (
    echo Creating environment...

    py -m venv .venv

    echo Activating environment.
    call .venv/Scripts/activate.bat

    echo Installing requirements...

    pip install -r ./requirements.txt
)

echo Launching the game!

py ./src/main.py

pause