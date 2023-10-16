'''Due to the requirements for crawling data, please be careful to turn off the VPN when running the program'''
from windows import Windows

windows = Windows()  # Create instance
windows.build_windows()  # initialization window
windows.start()  # Start window
