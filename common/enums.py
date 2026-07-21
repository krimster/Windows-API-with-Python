
from enum import IntEnum

#
# Structure for SECURITY_IMPERSONATION_LEVEL
#
class SECURITY_IMPERSONATION_LEVEL(IntEnum):
    Anonymous = 0
    Identification = 1
    Impersonation = 2
    Delegation = 3


#
# Structure for TOKEN_TYPE
#
class TOKEN_TYPE(IntEnum):
    TokenPrimary = 1
    TokenImpersonation = 2


#
# Logon Flags
#
class LogonFlags(IntEnum):
    WithProfile = 0x00000001
    NetCredentialsOnly = 0x00000002