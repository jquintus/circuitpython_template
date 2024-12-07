import storage
# In order to change the name used to display the filesystem of the board
# 1. Change NEW_NAME to whatever you want to be displayed
# 2. Rename this file to boot.py
# 3. Do a hard reset of the board (typically pressing the reset button on the board works)
# 4. When the board boots back up it should be visible under the new name
# 5. You can delete/rename this file at this point. You don't need to run it again.
# Reference: https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy
#
# NB: The name must be 11 characters or less! 
# This is a limitation of the filesystem. You will receive an error if you choose a
# name longer than 11 characters.

storage.remount("/", readonly=False)

m = storage.getmount("/")
m.label = "NEW_NAME"

storage.remount("/", readonly=False)

storage.enable_usb_drive()