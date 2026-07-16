"""
Reusable helper functions used throughout the examples.

These functions encapsulate common Win32 tasks such as locating
windows, retrieving process IDs, and opening process handles.
"""

import ctypes
from ctypes import wintypes
from ctypes.wintypes import DWORD
from ctypes import POINTER, byref

from common.winapi import user32, kernel32
import common.prototypes  # Registers all API prototypes
import common.constants as constants

#
# Window Helpers
#

def get_window_handle(window_title: str) -> wintypes.HWND:
    hWnd = user32.FindWindowW(None, window_title)

    if not hWnd:
        raise RuntimeError(
            f"Could not find window '{window_title}'. "
            f"Error: {ctypes.get_last_error()}"
        )

    return hWnd


#
# Process Helpers
#

def get_process_id(hWnd: wintypes.HWND) -> int:
    """Return the process ID associated with a window handle."""

    pid = wintypes.DWORD()

    # The function returns the thread ID and writes the process ID
    # to the output parameter.
    tid = user32.GetWindowThreadProcessId(
        hWnd,
        byref(pid),
    )

    if tid == 0:
        raise RuntimeError(
            f"GetWindowThreadProcessId failed. Error: {ctypes.get_last_error()}"
        )

    return pid.value

def open_process(pid: int, access: int = constants.PROCESS_ALL_ACCESS) -> wintypes.HANDLE:
        
    hProcess = kernel32.OpenProcess(
        access,
        False,
        pid,
    )

    if not hProcess:
       raise RuntimeError(
            f"Could not open process '{pid}'. "
            f"Error: {ctypes.get_last_error()}"
        )

    return hProcess


def open_process_token(hProcess, access):
    token = wintypes.HANDLE()

    if not kernel32.OpenProcessToken(
        hProcess,
        access,
        ctypes.byref(token)
    ):
        raise RuntimeError(
            f"OpenProcessToken failed!. Error: {ctypes.get_last_error()}"
        )

    return token