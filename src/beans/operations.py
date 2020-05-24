from enum import Enum
from services.repository.openaq.operations.mappings import Mappings
from services.repository.openaq.operations.aggregations import Aggregations


class OperationsBeans(Enum):
    MAPPINGS = Mappings()
    AGGREGATIONS = Aggregations()
