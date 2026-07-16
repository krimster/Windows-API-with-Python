
import ctypes
from ctypes import wintypes

from common.winapi import user32, kernel32, dnsapi, advapi32

from common.structures import (
    SECURITY_ATTRIBUTES,
    STARTUP_INFO,
    PROCESS_INFORMATION,
    DNS_CACHE_ENTRY,
    LUID,
    LUID_AND_ATTRIBUTES,
    PRIVILEGE_SET,
)


# HWND FindWindowW(
#   [in, optional] LPCWSTR lpClassName,
#   [in, optional] LPCWSTR lpWindowName
# );

user32.FindWindowW.argtypes = (
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
)

user32.FindWindowW.restype = wintypes.HWND


# DWORD GetWindowThreadProcessId(
#   [in]            HWND    hWnd,
#   [out, optional] LPDWORD lpdwProcessId
# );

user32.GetWindowThreadProcessId.argtypes = (
    wintypes.HWND,
    wintypes.LPDWORD,
)

user32.GetWindowThreadProcessId.restype = wintypes.DWORD


# HANDLE OpenProcess(
#   [in] DWORD dwDesiredAccess,
#   [in] BOOL  bInheritHandle,
#   [in] DWORD dwProcessId
# );

kernel32.OpenProcess.argtypes = (
    wintypes.DWORD,
    wintypes.BOOL,
    wintypes.DWORD,
)

kernel32.OpenProcess.restype = wintypes.HANDLE


# BOOL TerminateProcess(
#   [in] HANDLE hProcess,
#   [in] UINT   uExitCode
# );

kernel32.TerminateProcess.argtypes = (
    wintypes.HANDLE,
    wintypes.UINT,
)

kernel32.TerminateProcess.restype = wintypes.BOOL

# BOOL CloseHandle(
#   [in] HANDLE hObject
# );

kernel32.CloseHandle.argtypes = (
    wintypes.HANDLE,
)

kernel32.CloseHandle.restype = wintypes.BOOL


# BOOL CreateProcessW(
#   [in, optional]      LPCWSTR               lpApplicationName,
#   [in, out, optional] LPWSTR                lpCommandLine,
#   [in, optional]      LPSECURITY_ATTRIBUTES lpProcessAttributes,
#   [in, optional]      LPSECURITY_ATTRIBUTES lpThreadAttributes,
#   [in]                BOOL                  bInheritHandles,
#   [in]                DWORD                 dwCreationFlags,
#   [in, optional]      LPVOID                lpEnvironment,
#   [in, optional]      LPCWSTR               lpCurrentDirectory,
#   [in]                LPSTARTUPINFOW        lpStartupInfo,
#   [out]               LPPROCESS_INFORMATION lpProcessInformation
# );

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


# BOOL OpenProcessToken(
#   [in]  HANDLE  ProcessHandle,
#   [in]  DWORD   DesiredAccess,
#   [out] PHANDLE TokenHandle
# );

kernel32.OpenProcessToken.argtypes = (
    wintypes.HANDLE,
    wintypes.DWORD,
    wintypes.PHANDLE,
)

kernel32.OpenProcessToken.restype = wintypes.BOOL


# BOOL LookupPrivilegeValueW(
#   [in, optional] LPCWSTR lpSystemName,
#   [in]           LPCWSTR lpName,
#   [out]          PLUID   lpLuid
# );

advapi32.LookupPrivilegeValueW.argtypes = (
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
    ctypes.POINTER(LUID)
    
)

advapi32.LookupPrivilegeValueW.restype = wintypes.BOOL


# BOOL PrivilegeCheck(
#   [in]      HANDLE         ClientToken,
#   in, out] PPRIVILEGE_SET RequiredPrivileges,
#   [out]     LPBOOL         pfResult
#  )

advapi32.PrivilegeCheck.argtypes = (
    wintypes.HANDLE,
    ctypes.POINTER(PRIVILEGE_SET),
    ctypes.POINTER(wintypes.BOOL),
)

advapi32.PrivilegeCheck.restype = wintypes.BOOL
