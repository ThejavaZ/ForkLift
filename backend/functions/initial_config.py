import os


def initial_config():
    
    if not os.path.exists(".venv"):
        os.system("python3 -m venv .venv")
    if not os.path.exists("requirements.txt"):
        with open("requirements.txt", "w") as f:
            f.write("opencv-python\nnumpy\nultralytics\npillow\npandas\n")
            
    dir = os.getcwd()

    os.system(f"source {dir}/.venv/bin/activate") if os.name != 'nt' else os.system(f"{dir}/.venv/Scripts/activate.ps1") # Activate virtual enviroment

    os.system("pip install -r requirements.txt") # Install requirements

    os.system("cls") if os.name == "nt" else os.system("clear")