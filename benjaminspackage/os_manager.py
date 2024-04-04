import os

def navigate_to(target_directory):
   
   # Initialize the target directory name
   target_directory = target_directory

   print(f"\nReceived command to navitage to directory named: {target_directory}")
   print(f"\nCurrent Directory: {os.getcwd()}")

   try:
      os.chdir(target_directory)
   except:
      print(f"\nError: '{target_directory}' directory not found.")
   else:
      print(f"\nSuccesfully moved to: {os.getcwd()}")