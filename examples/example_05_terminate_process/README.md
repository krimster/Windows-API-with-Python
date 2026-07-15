# Example 05 - TerminateProcess

## Overview

This example demonstrates how to terminate a running process using the Win32 `TerminateProcess` function.

Building on the previous examples, we first locate a window using `FindWindowW`, retrieve the associated Process ID (PID) using `GetWindowThreadProcessId`, obtain a process handle with `OpenProcess`, and finally terminate the process using `TerminateProcess`.

> **Note**
>
> This example is intended for educational purposes to demonstrate interaction with the Windows API. Only terminate processes that you own or are explicitly authorized to manage.

---

## Learning Objectives

After completing this example you should understand how to:

- Locate a window using `FindWindowW`
- Retrieve the owning Process ID (PID)
- Open a process using `OpenProcess`
- Request the appropriate process access rights
- Terminate a process using `TerminateProcess`
- Handle Win32 API errors

---

## Windows APIs Used

| API | Purpose |
|------|---------|
| `FindWindowW` | Retrieves the handle (`HWND`) of an existing window. |
| `GetWindowThreadProcessId` | Retrieves the Process ID and Thread ID associated with a window. |
| `OpenProcess` | Opens a handle to a running process. |
| `TerminateProcess` | Terminates the specified process. |

---

## How It Works

1. Prompt the user for a window title.
2. Obtain the window handle (`HWND`).
3. Retrieve the Process ID (PID).
4. Open the target process with the required access rights.
5. Call `TerminateProcess()`.
6. Report whether the operation succeeded.

---

## Data Flow

```text
Window Title
      │
      ▼
FindWindowW()
      │
      ▼
    HWND
      │
      ▼
GetWindowThreadProcessId()
      │
      ▼
     PID
      │
      ▼
OpenProcess()
      │
      ▼
 Process Handle
      │
      ▼
TerminateProcess()
```

---

## Example Output

```text
Enter window title: Notepad

Process 1234 terminated successfully.
```

---

## Concepts Introduced

- Process termination
- Process access rights
- Process handles (`HANDLE`)
- Win32 error handling
- Reusable helper functions

---

## Behind the Scenes

Unlike many high-level programming languages, Windows does not operate directly on Process IDs when performing actions such as terminating a process.

Instead, a Process ID must first be converted into a **process handle** by calling `OpenProcess()`. The returned handle represents an open connection to the target process and includes the access rights requested by the caller.

`TerminateProcess()` does not accept a PID—it requires a valid process handle (`HANDLE`).

This two-step design allows Windows to perform access control before permitting operations on another process.

---

## Key Takeaways

This example demonstrates the typical workflow for interacting with another process through the Win32 API:

- Locate the target window.
- Obtain its Process ID.
- Open a process handle with the required permissions.
- Perform the desired operation using that handle.

Many Win32 APIs—including `ReadProcessMemory`, `WriteProcessMemory`, and `VirtualAllocEx`—follow this same pattern of first obtaining a process handle before interacting with the target process.

---

## Microsoft Documentation

- https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-findwindoww
- https://learn.microsoft.com/windows/win32/api/winuser/nf-winuser-getwindowthreadprocessid
- https://learn.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess
- https://learn.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess

