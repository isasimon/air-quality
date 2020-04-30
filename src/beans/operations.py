from enum import Enum
from services.operations.mappings import Mappings
from services.operations.aggregations import Aggregations


class OperationsBeans(Enum):
    MAPPINGS = Mappings()
    AGGREGATIONS = Aggregations()
