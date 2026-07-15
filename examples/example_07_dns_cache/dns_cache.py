"""
Example 07 - DnsGetCacheDataTable

Objective:
    Enumerate the Windows DNS Client Cache using the undocumented
    DnsGetCacheDataTable API.

Description:
    Demonstrates how to call an undocumented function exported by
    dnsapi.dll to traverse the Windows DNS cache as a linked list.

Windows APIs:
    - DnsGetCacheDataTable

Windows Structures:
    - DNS_CACHE_ENTRY

Concepts:
    - Undocumented Windows APIs
    - DNS Client Cache
    - Self-referential structures
    - Linked lists
    - Pointer traversal
    - ctypes pointers
    - Passing structures by reference

Reference:
    This API is undocumented and is not part of the official
    Microsoft Win32 SDK documentation.
"""

import ctypes

from common.winapi import kernel32,dnsapi
import common.prototypes  # Registers all API prototypes

from common import structures


def main() -> None:
    """Dump DNS cache table."""

    head = structures.DNS_CACHE_ENTRY()
    head.wDataLength = 1024

    response = dnsapi.DnsGetCacheDataTable(ctypes.byref(head))

    if not response:
        raise RuntimeError(...)

    entry = head.pNext

    while entry:
        print(f"{entry.contents.recName}")
        entry = entry.contents.pNext

if __name__ == "__main__":
    main()