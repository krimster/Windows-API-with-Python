
import ctypes
from ctypes.wintypes import HANDLE,DWORD,LPWSTR,LPBYTE,WORD,LPVOID,BOOL


#
# Structure for Process Info
# https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-process_information
#
class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD)
    ]

#
# Structure for Startup Info
# https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfow
#
class STARTUP_INFO(ctypes.Structure):
    _fields_ = [
        ("cb", DWORD),
        ("lpReserved", LPWSTR),
        ("lpDesktop", LPWSTR),
        ("lpTitle", LPWSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
    ]

#
# Structure for Security Attributes
# https://learn.microsoft.com/en-us/windows/win32/api/wtypesbase/ns-wtypesbase-security_attributes
#
class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = (
        ("nLength", DWORD),
        ("lpSecurityDescriptor", LPVOID),
        ("bInheritHandle", BOOL),
    )


#
# Structure for DNS_CACHE_ENTRY
#
class DNS_CACHE_ENTRY(ctypes.Structure):
    pass

PDNS_CACHE_ENTRY = ctypes.POINTER(DNS_CACHE_ENTRY)

DNS_CACHE_ENTRY._fields_ = [
    ("pNext", PDNS_CACHE_ENTRY),
    ("recName", LPWSTR),
    ("wType", WORD),
    ("wDataLength", WORD),
    ("dwFlags", DWORD),
]


#
# Structure for LUID
#
class LUID(ctypes.Structure):
    _fields_= [
        ("LowPart", DWORD),
        ("HighPart", DWORD),
    ]


#
# Structure for LUID_AND_ATTRIBUTES
#
class LUID_AND_ATTRIBUTES(ctypes.Structure):
    _fields_= [
        ("Luid", LUID),
        ("Attributes", DWORD),
    ]


#
# Structure for PRIVILEGE_SET
#
class PRIVILEGE_SET(ctypes.Structure):
    _fields_= [
        ("PrivilegeCount", DWORD),
        ("Control", DWORD),
        ("Privileges", LUID_AND_ATTRIBUTES)
    ]