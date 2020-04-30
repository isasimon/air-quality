from enum import Enum
from .mappings import Mappings
from .aggregations import Aggregations


class OperationsBeans(Enum):
    MAPPINGS = Mappings()
    AGGREGATIONS = Aggregations()
