# Example 09 - PrivilegeCheck

## Overview

This example demonstrates how to determine whether a specific Windows privilege is enabled within the access token of a running process.

Windows uses **access tokens** to represent the security context of a process or thread. Each token contains a collection of privileges that control which privileged operations the process is permitted to perform.

The example performs the following steps:

1. Locate a target window by its title.
2. Obtain the owning process ID.
3. Open the target process.
4. Open the process access token.
5. Resolve a privilege name to its corresponding **Locally Unique Identifier (LUID)** using `LookupPrivilegeValueW`.
6. Build a `PRIVILEGE_SET` structure.
7. Call `PrivilegeCheck` to determine whether the privilege is enabled.
8. Release all acquired handles.

## Windows APIs Used

* `FindWindowW`
* `GetWindowThreadProcessId`
* `OpenProcess`
* `OpenProcessToken`
* `LookupPrivilegeValueW`
* `PrivilegeCheck`
* `CloseHandle`

## Windows Structures

* `LUID`
* `LUID_AND_ATTRIBUTES`
* `PRIVILEGE_SET`

## Concepts Covered

* Windows access tokens
* Security privileges
* Locally Unique Identifiers (LUIDs)
* Token privilege verification
* Passing structures by reference with `ctypes`
* Handle management
* Resource cleanup

## Example Output

```text
Enter window name: notepad

Enter privilege name: SeDebugPrivilege

Privilege Disabled: SeDebugPrivilege
```

or

```text
Enter window name: cmd

Enter privilege name: SeChangeNotifyPrivilege

Privilege Enabled: SeChangeNotifyPrivilege
```

## Learning Notes

Unlike user rights or group memberships, Windows privileges are identified internally by **Locally Unique Identifiers (LUIDs)** rather than by their textual names.

The `LookupPrivilegeValueW` API translates a privilege name (for example, `SeDebugPrivilege`) into its corresponding LUID. This LUID is then supplied to `PrivilegeCheck`, which determines whether the privilege is currently enabled in the target access token.

Being present in a token does not necessarily mean a privilege is enabled. Some privileges exist within a token but remain disabled until explicitly enabled by the operating system or the application.

Understanding how Windows privileges are represented and queried is an important foundation for later topics such as privilege adjustment, token duplication, and user impersonation.

## Cleanup

Both the process handle and the token handle are released using `CloseHandle` once they are no longer required.

Proper handle cleanup prevents resource leaks and is considered good practice when interacting with the Windows API.

## References

* Microsoft Learn – LookupPrivilegeValueW
  https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-lookupprivilegevaluew

* Microsoft Learn – PrivilegeCheck
  https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-privilegecheck
