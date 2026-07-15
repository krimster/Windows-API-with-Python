
import ctypes
from ctypes import wintypes

from common.winapi import user32, kernel32, dnsapi

from common.structures import (
    SECURITY_ATTRIBUTES,
    STARTUP_INFO,
    PROCESS_INFORMATION,
    DNS_CACHE_ENTRY,
)

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

#
# CreateProcessW
#

LPSECURITY_ATTRIBUTES = ctypes.POINTER(SECURITY_ATTRIBUTES)

kernel32.CreateProcessW.argtypes = (
    wintypes.LPCWSTR,
    wintypes.LPWSTR,
    LPSECURITY_ATTRIBUTES,
    LPSECURITY_ATTRIBUTES,
    wintypes.BOOL,
    wintypes.DWORD,
    wintypes.LPVOID,
    wintypes.LPCWSTR,
    ctypes.POINTER(STARTUP_INFO),
    ctypes.POINTER(PROCESS_INFORMATION),
)

kernel32.CreateProcessW.restype = wintypes.BOOL


#
# DnsGetCacheDataTable
#

dnsapi.DnsGetCacheDataTable.argtypes = (
    ctypes.POINTER(DNS_CACHE_ENTRY),
)

dnsapi.DnsGetCacheDataTable.restype = wintypes.BOOL