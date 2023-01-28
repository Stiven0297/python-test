import dataclasses
from typing import Optional, List, Dict, Any

from src.property.service_layer.unit_of_work import \
    AbstractPropertyUnitOfWork


def get_properties(
    uow: AbstractPropertyUnitOfWork,
    status: Optional[str] = None,
    city: Optional[str] = None,
    year: Optional[int] = None,

) -> List[Dict[str, Any]]:
    properties = uow.properties.filter(status, city, year)
    return list(map(lambda property: dataclasses.asdict(property), properties))
