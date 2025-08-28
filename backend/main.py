from functions.initial_config import initial_config

Test = 0 # 0 if it's test mode, 1 if it's production mode

if Test == 0:
    import os
    os.environ["TEST_MODE"] = "1"

if __name__ == "__main__":
    initial_config()