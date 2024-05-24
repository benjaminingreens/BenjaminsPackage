import os

def navigate_to(target_directory):
    print(f"\nReceived command to navigate to directory named: {target_directory}")
    print(f"\nCurrent Directory: {os.getcwd()}")

    current_path = os.getcwd()

    # Iterate up the directory tree
    while True:
        # Check if the target directory exists in the current path
        if target_directory in os.listdir(current_path):
            os.chdir(os.path.join(current_path, target_directory))
            print(f"\nSuccessfully moved to: {os.getcwd()}")
            break
        else:
            # Move up one level in the directory tree
            parent_path = os.path.dirname(current_path)
            
            # If the parent path is the same as the current path, we have reached the root
            if parent_path == current_path:
                print(f"\nError: '{target_directory}' directory not found.")
                break

            current_path = parent_path
