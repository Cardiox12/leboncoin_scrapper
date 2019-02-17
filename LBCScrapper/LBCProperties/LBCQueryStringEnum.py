from enum import Enum

class LBCQueryStringEnum(Enum):
    OLDER       = "&sort=time&order=asc"
    DECREASE    = "&sort=price&order=asc"
    INCREASE    = "&sort=price&order=desc"
    NEW_PAGE    = "&page="
    LOCATION    = "&locations="
    REAL_ESTATE = "&real_estate_type=2,1"

class LBCQueryStringCitiesEnum(Enum):
    AVIGNON     = "Avignon_84000"