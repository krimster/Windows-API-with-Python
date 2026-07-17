"""
Reusable helper functions used throughout the examples.

These functions encapsulate common Win32 tasks such as locating
windows, retrieving process IDs, and opening process handles.
"""

import ctypes
from ctypes import wintypes
from ctypes.wintypes import DWORD
from ctypes import POINTER, byref

from common.winapi import user32, kernel32, advapi32
import common.prototypes  # Registers all API prototypes
import common.constants as constants
from common.structures import (
    SECURITY_ATTRIBUTES,
    STARTUP_INFO,
    PROCESS_INFORMATION,
    DNS_CACHE_ENTRY,
    LUID,
    LUID_AND_ATTRIBUTES,
    PRIVILEGE_SET,
    TOKEN_PRIVILEGES,
)


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


def lookup_privilege_value(privilege_name: str) -> structures.LUID:
    luid = LUID()

    if not advapi32.LookupPrivilegeValueW(None, privilege_name, ctypes.byref(luid)):
        raise RuntimeError(
            f"LookupPrivilegeValueW failed!. Error: {ctypes.get_last_error()}"
        )

    return luid


def check_privilege(
    token: wintypes.HANDLE,
    luid: LUID,
    privilege_name: str,
    attributes: wintypes.DWORD = constants.SE_PRIVILEGE_ENABLED,
) -> bool:
    """Return True if the specified privilege is enabled in the token."""

    privilege_set = PRIVILEGE_SET()
    privilege_set.PrivilegeCount = 1
    privilege_set.Control = 0
    privilege_set.Privileges.Luid = luid
    privilege_set.Privileges.Attributes = attributes

    result = wintypes.BOOL()

    success = advapi32.PrivilegeCheck(
        token,
        ctypes.byref(privilege_set),
        ctypes.byref(result),
    )

    if not success:
        raise RuntimeError(
            f"PrivilegeCheck failed. Error: {ctypes.get_last_error()}"
        )

    if result.value:
        print("Privilege {0}: enabled".format(privilege_name))    
    else:
        print("Privilege {0}: disabled".format(privilege_name))
          
    return bool(result.value)


def adjust_privilege(
    token: wintypes.HANDLE,
    luid: LUID,
    attributes: wintypes.DWORD,
):
    disable_all_privileges = False
    token_privileges = TOKEN_PRIVILEGES()

    buffer_length = ctypes.sizeof(token_privileges)
    previous_state = TOKEN_PRIVILEGES()
    return_length = wintypes.DWORD()

    token_privileges.PrivilegeCount = 1
    token_privileges.Privileges.Luid = luid
    token_privileges.Privileges.Attributes = attributes

    print(f"New attribute: {token_privileges.Privileges.Attributes:#x}")

    success = advapi32.AdjustTokenPrivileges(
        token,
        disable_all_privileges,
        ctypes.byref(token_privileges),
        buffer_length,
        ctypes.byref(previous_state),
        ctypes.byref(return_length)
    )

    if not success:
        raise RuntimeError(
            f"AdjustTokenPrivileges failed. Error: {ctypes.get_last_error()}"
        )

    error = ctypes.get_last_error()
    print(error)

    if error == constants.ERROR_NOT_ALL_ASSIGNED:
        raise RuntimeError(
            f"Status: {privilege_name} is not present in this token."
        )

    print(f"Previous count : {previous_state.PrivilegeCount}")

    if previous_state.PrivilegeCount:
        print(f"Previous attr  : {previous_state.Privileges.Attributes:#x}")
    
    print("Token flipped")



def get_current_process()-> wintypes.HANDLE:
    return kernel32.GetCurrentProcess()


def open_current_process_token(access: int) -> wintypes.HANDLE:
    return open_process_token(kernel32.GetCurrentProcess(), access)