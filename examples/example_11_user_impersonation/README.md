# Example 11 – User Impersonation

## Objective

Demonstrate how to duplicate the primary access token of a running process and create a new process executing under the security context of the target user.

This example combines the concepts introduced throughout the previous security examples into a complete user impersonation workflow.

---

## Windows APIs

- FindWindowW
- GetWindowThreadProcessId
- OpenProcess
- OpenProcessToken
- GetCurrentProcess
- LookupPrivilegeValueW
- PrivilegeCheck
- AdjustTokenPrivileges
- DuplicateTokenEx
- CreateProcessWithTokenW
- CloseHandle

---

## Concepts Demonstrated

- Windows access tokens
- Primary vs impersonation tokens
- Access token privileges
- LUIDs (Locally Unique Identifiers)
- Security impersonation levels
- Token duplication
- Creating processes using an existing token
- Handle management
- Principle of least privilege

---

## Workflow

The example performs the following operations:

1. Locate a target process by its window title.
2. Obtain the process identifier.
3. Open the target process.
4. Open the target process access token.
5. Open the current process access token.
6. Verify that the current process has the required privileges.
7. Enable **SeDebugPrivilege** if necessary.
8. Duplicate the target process token using `DuplicateTokenEx`.
9. Create a new process using the duplicated primary token with `CreateProcessWithTokenW`.
10. Close all opened handles.

---

## Process Flow

```text
FindWindowW
      │
      ▼
GetWindowThreadProcessId
      │
      ▼
OpenProcess
      │
      ▼
OpenProcessToken
      │
      ▼
Target Access Token
      │
      ├──────────────┐
      │              │
      ▼              ▼
PrivilegeCheck   AdjustTokenPrivileges
      │
      ▼
DuplicateTokenEx
      │
      ▼
Primary Token
      │
      ▼
CreateProcessWithTokenW
      │
      ▼
New Process
```
---

## Expected Output

Enter window name: Windows PowerShell

Privilege SeDebugPrivilege: enabled

DuplicateTokenEx success

Original token   : 0x1e8
Duplicate token  : 0x208

Created process successfully.


## Notes
DuplicateTokenEx requires a primary token when creating a new process.
The calling process must possess the necessary privileges (typically SeImpersonatePrivilege or SeDebugPrivilege, depending on the scenario).
The example uses Unicode (W) versions of the Win32 APIs.
All handles obtained from the operating system are released using CloseHandle.