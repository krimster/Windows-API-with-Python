# Example 08 - OpenProcessToken

## Overview

This example demonstrates how to obtain a handle to the access token associated with a running process using the **OpenProcessToken** Win32 API.

A Windows access token represents the security context of a process or thread and contains information such as the user account, group memberships, privileges, and integrity level. Many advanced Windows security operations—including privilege manipulation, impersonation, and spawning processes under different user contexts—begin by obtaining a process token.

This example builds on the previous lessons by:

* Finding a window by its title.
* Retrieving the owning process ID.
* Opening a handle to the target process.
* Obtaining a handle to the process access token.
* Properly releasing all acquired handles.

## Windows APIs Used

* `FindWindowW`
* `GetWindowThreadProcessId`
* `OpenProcess`
* `OpenProcessToken`
* `CloseHandle`

## Concepts Covered

* Windows access tokens
* Process security
* Process and token handles
* Access rights (`TOKEN_ALL_ACCESS`)
* Passing handles by reference with `ctypes`
* Resource management and handle cleanup

## Example Output

```text
Enter window name: notepad
[INFO] Process Token Handle: 0x00000000000001A8
```

## Learning Notes

This example introduces one of the most important concepts in Windows security programming: **access tokens**.

Unlike a process handle, which provides access to a process object, a token handle provides access to the security information associated with that process. Token handles are commonly used to:

* Enumerate user and group information.
* Query or enable privileges.
* Duplicate tokens.
* Perform user impersonation.
* Create processes under different security contexts.

These capabilities form the foundation of many administrative tools, authentication mechanisms, and security testing techniques.

## Cleanup

Both the process handle and the token handle are released using `CloseHandle` to avoid leaking kernel resources. Although these examples are short-lived programs, releasing handles is considered good practice and is essential when developing long-running applications or security tooling.

## References

* Microsoft Learn – OpenProcessToken
  https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken
