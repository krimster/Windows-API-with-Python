# Example 10 – AdjustTokenPrivileges

## Overview

This example demonstrates how to modify the state of a privilege in a process access token using the Win32 `AdjustTokenPrivileges` API.

The example:

1. Finds a target window.
2. Retrieves the associated process ID.
3. Opens the target process.
4. Opens the process access token.
5. Looks up the LUID for a specified privilege.
6. Checks whether the privilege is currently enabled.
7. Toggles the privilege (enable/disable).
8. Handles the special `ERROR_NOT_ALL_ASSIGNED` condition.

This example builds upon the previous token-related examples (`OpenProcessToken` and `PrivilegeCheck`).

---

## Windows APIs Used

- `FindWindowW`
- `GetWindowThreadProcessId`
- `OpenProcess`
- `OpenProcessToken`
- `LookupPrivilegeValueW`
- `PrivilegeCheck`
- `AdjustTokenPrivileges`
- `CloseHandle`

---

## Concepts Covered

- Windows access tokens
- Token privileges
- Locally Unique Identifiers (LUIDs)
- Enabling and disabling privileges
- Access rights
- Win32 error handling
- Resource cleanup

---

## Example Output

```text
Enter window name: Task Manager

Privilege : SeDebugPrivilege
State     : Enabled

Privilege successfully disabled.
```

Or, when enabling a disabled privilege:

```text
Enter window name: Some Application

Privilege : SeDebugPrivilege
State     : Disabled

Privilege successfully enabled.
```

If the privilege is not present in the token:

```text
Enter window name: x64dbg

Privilege : SeDebugPrivilege
State     : Not Present

SeDebugPrivilege is not present in this token.
```

---

## Notes

### `AdjustTokenPrivileges` can succeed even when the privilege is absent

One of the most common pitfalls when using `AdjustTokenPrivileges` is assuming that a non-zero return value means the requested privilege was successfully modified.

After a successful call, always check:

```python
ctypes.get_last_error()
```

If the value is:

```text
ERROR_NOT_ALL_ASSIGNED (1300)
```

the requested privilege was **not present** in the target token and therefore could not be enabled or disabled.

---

## Running the Example

From the repository root:

```bash
python -m examples.example_10_privilege_adjust.privilege_adjust
```

---

## References

- https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges
- https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-privilegecheck
- https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-lookupprivilegevaluew
- https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens