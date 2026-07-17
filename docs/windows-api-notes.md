
### Observation
PrivilegeCheck reports whether a privilege is currently enabled in the token, not merely whether it is assigned. Task Manager (when elevated) enables SeDebugPrivilege, whereas an elevated Command Prompt and Python process have the privilege present but disabled.