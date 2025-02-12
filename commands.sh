# STEPS TO GET THE PROJECT RUNNING:

# 1. cd to the project directory
# 2. ./commands.sh

# 3. Run this command to create Environment Folder
    python3 -m venv venv
    # If windows
    python -m venv venv

# 4. Run this command to activate Environment Folder
    source venv/bin/activate
    # If windows
    .\venv\Scripts\activate

# 5. Run this command to install requirements
    pip install -r requirements.txt

# 6. Run this command to build the docker image and start the container:
    docker compose up --build
    # or, to run it in background
    docker compose up --d

#  ALTERNATIVE COMMANDS:
    # - Run this command to run the project
    fastapi run main.py
    # For Development
    fastapi dev main.py

    # - Run this command to stop the project
        # Hotkeys: ctrl + c
