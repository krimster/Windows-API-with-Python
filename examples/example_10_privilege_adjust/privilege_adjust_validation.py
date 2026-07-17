import ctypes

from ctypes import wintypes

from common.winapi import kernel32,user32,advapi32
import common.prototypes  # Registers all API prototypes

from common import constants
from common import helpers
from common import structures

def main() -> None:
    """Adjust privileges associated with a primary access token for a running process."""

    try:
        privilege_name = "SeDebugPrivilege"

        # current process path
        token = helpers.open_current_process_token(
            constants.TOKEN_ALL_ACCESS
        )

        luid = helpers.lookup_privilege_value(
            privilege_name
        )

        print("Initial state:")
        helpers.check_privilege(token, luid, privilege_name)

        helpers.adjust_privilege(
            token,
            luid,
            constants.SE_PRIVILEGE_DISABLED
        )

        print("After disabling:")
        helpers.check_privilege(token, luid, privilege_name)


        helpers.adjust_privilege(
            token,
            luid,
            constants.SE_PRIVILEGE_ENABLED
        )

        print("After enabling:")
        helpers.check_privilege(token, luid, privilege_name)

    except RuntimeError as e:
        print(e)
        raise SystemExit(1)

if __name__ == "__main__":
    main()