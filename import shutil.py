import shutil

# Path to the file in the sandbox environment
sandbox_path = "/mnt/data/master_33_sectors_full_sample.csv"

# Local path where you want to save the file
local_path = "master_33_sectors_full_sample.csv"

try:
    # Open the sandbox file and copy it to the local system
    with open(sandbox_path, 'rb') as sandbox_file:
        with open(local_path, 'wb') as local_file:
            shutil.copyfileobj(sandbox_file, local_file)
    print(f"File successfully downloaded to {local_path}")
except FileNotFoundError:
    print("The file does not exist in the sandbox environment.")
except PermissionError:
    print("Permission denied. Ensure you have access to the sandbox environment.")
except Exception as e:
    print(f"An error occurred: {e}")
