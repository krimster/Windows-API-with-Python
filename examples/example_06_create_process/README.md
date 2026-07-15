# Example 06 - CreateProcessW

## Overview

This example demonstrates how to create a new Windows process from Python using the Win32 `CreateProcessW` API through `ctypes`.

Unlike higher-level Python functions such as `subprocess.Popen()`, the Windows API provides direct control over the process creation workflow and requires the caller to provide several structures and parameters defined by the Windows SDK.

This example focuses on understanding how Python can interact directly with native Windows APIs and how complex Win32 structures are represented using `ctypes`.

---

## Learning Objectives

By completing this example, you will understand:

* How to call the Win32 `CreateProcessW` API from Python
* How Windows represents process creation parameters
* How to define and pass Win32 structures using `ctypes`
* How to pass structures by reference using `ctypes.byref()`
* How process and thread handles are returned by Windows
* The role of startup configuration during process creation

---

## Windows APIs Used

### CreateProcessW

Creates a new process and its primary thread.

Documentation:

https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw

---

## Windows Structures Used

### SECURITY_ATTRIBUTES

Defines security settings for the process and thread objects.

In this example, `None` is passed to allow Windows to use the default security descriptor.

---

### STARTUPINFOW

Contains startup configuration information for the new process.

Important fields used:

* `cb`

  * Size of the structure. Must be initialized before calling `CreateProcessW`.

* `dwFlags`

  * Controls startup behaviour.

* `wShowWindow`

  * Controls how the new window is displayed.

---

### PROCESS_INFORMATION

Receives information about the newly created process.

Contains:

* Process handle
* Primary thread handle
* Process ID
* Thread ID

---

## Key Concepts

### Win32 Structures and ctypes

Windows APIs are written in C and rely heavily on structures.

Python does not natively understand these structures, so they are recreated using `ctypes.Structure`.

Example:

```python
class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD)
    ]
```

---

### Passing Structures by Reference

The Windows API expects pointers to structures:

```cpp
LPSTARTUPINFOW lpStartupInfo
LPPROCESS_INFORMATION lpProcessInformation
```

In Python this is represented using:

```python
ctypes.byref()
```

Example:

```python
ctypes.byref(startup_info)
```

---

## Project Structure

The example uses shared components from the repository:

```
common/
├── constants.py
├── helpers.py
├── prototypes.py
├── structures.py
└── winapi.py
```

### winapi.py

Loads Windows DLLs.

### prototypes.py

Defines Win32 API function signatures using `argtypes` and `restype`.

### structures.py

Contains ctypes definitions for Windows structures.

### constants.py

Contains Windows API constants and flags.

---

## Running the Example

From the repository root:

```powershell
python -m examples.example_06_create_process.create_process
```

The example will create a new process using the Windows API.

---

## Notes

This example directly interacts with the Windows process creation API.

It is intended for educational purposes to demonstrate Windows API programming with Python and `ctypes`.

Only run examples from this repository in an environment where you have permission to create and manage processes.

---

## References

Microsoft Learn - CreateProcessW:

https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
