try:
     file = open("data.txt", "r")
     content = file.read()

except FileNotFoundError:
   print("The file was not found!")

else:
 print("The file has been read successfully.")

finally:
 print("Closing the file...")



# Code to close the file goes here