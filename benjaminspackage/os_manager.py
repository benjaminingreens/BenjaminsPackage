import os

def navigtate_to(target_directory):
   
   # Initialize the target directory name
   target_directory = target_directory
   found = False

   print(f"\nReceived command to navitage to directory named: {target_directory}")
   print(f"\nCurrent Directory: {os.getcwd()}")

   # Start from the current directory and move up the tree until you find the target directory
   while True:
      # Get the current working directory
      current_directory = os.getcwd()
      # Split the current directory path
      path_parts = current_directory.split(os.sep)

      # Check if the target directory is in the current path
      if target_directory in path_parts:
         # Reconstruct the path up to the target directory
         index = path_parts.index(target_directory)
         target_path = os.sep.join(path_parts[: index + 1])
         # Change to the target directory
         os.chdir(target_path)
         found = True
         break
      else:
         # Move up one directory level
         os.chdir(os.path.dirname(current_directory))
         # If we've reached the root directory and haven't found the target, stop the loop
         if os.getcwd() == current_directory:
               break  # This means we cannot go up any further

   if not found:
      print(f"\nError: '{target_directory}' directory not found.")
   else:
      print(f"\nSuccesfully moved to: {os.getcwd()}")