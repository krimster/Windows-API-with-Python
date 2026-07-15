from ctypes import wintypes

from common.winapi import user32, kernel32

#
# FindWindowW
#

user32.FindWindowW.argtypes = (
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
)

user32.FindWindowW.restype = wintypes.HWND


#
# GetWindowThreadProcessId
#

user32.GetWindowThreadProcessId.argtypes = (
    wintypes.HWND,
    wintypes.LPDWORD,
)

user32.GetWindowThreadProcessId.restype = wintypes.DWORD


#
# OpenProcess
#

kernel32.OpenProcess.argtypes = (
    wintypes.DWORD,
    wintypes.BOOL,
    wintypes.DWORD,
)

kernel32.OpenProcess.restype = wintypes.HANDLE


#
# TerminateProcess
#

kernel32.TerminateProcess.argtypes = (
    wintypes.HANDLE,
    wintypes.UINT,
)

kernel32.TerminateProcess.restype = wintypes.BOOL

#
# CloseHandle
#

kernel32.CloseHandle.argtypes = (
    wintypes.HANDLE,
)

kernel32.CloseHandle.restype = wintypes.BOOL