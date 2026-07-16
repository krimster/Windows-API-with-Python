import ctypes

user32 = ctypes.WinDLL("user32", use_last_error=True)
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
dnsapi = ctypes.WinDLL("dnsapi.dll", use_last_error=True)
advapi32 = ctypes.WinDLL("advapi32.dll", use_last_error=True)