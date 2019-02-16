from enum import Enum

class LBCQueryStringEnum(Enum):
    OLDER       = "&sort=time&order=asc"
    DECREASE    = "&sort=price&order=asc"
    INCREASE    = "&sort=price&order=desc"