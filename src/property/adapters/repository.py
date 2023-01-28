import abc
from typing import TypeVar, Generic, Optional, List, Dict, Any

import mysql.connector

from src.property.domain.models import Property

_M = TypeVar("_M")


class AbstractRepository(abc.ABC, Generic[_M]):
    @abc.abstractmethod
    def filter(self, *args, **kwargs) -> List[Optional[_M]]:
        ...


class AbstractReadRepository(AbstractRepository):
    @abc.abstractmethod
    def to_domain(
        self, orm: Dict[str, Any], *args, **kwargs
    ) -> _M:
        ...


class AbstractPropertyRepository(AbstractReadRepository):
    @abc.abstractmethod
    def filter(
        self,
        status: Optional[str],
        city: Optional[str],
        year: Optional[int]
    ) -> List[Optional[_M]]:
        ...


class PropertyRepository(AbstractPropertyRepository):
    def __init__(self):
        self.connector = mysql.connector.connect(
            host="3.130.126.210",
            port=3309,
            user="pruebas",
            password="VGbt3Day5R",
            database="habi_db"
        )

    def filter(
        self,
        status: Optional[str] = None,
        city: Optional[str] = None,
        year: Optional[int] = None
    ) -> List[Optional[Property]]:
        cursor = self.connector.cursor()
        query = f"""SELECT p.id, MAX(sh.update_date) AS date, p.address, 
        p.city, s.id AS status_id, s.name AS status_name, 
        s.label AS status_label, p.price, p.description 
        FROM property p 
        INNER JOIN status_history sh ON p.id = sh.property_id
        INNER JOIN status s ON s.id = sh.status_id
        WHERE p.`year` LIKE '%{year}%' AND p.city LIKE '%{city}%'
        GROUP BY p.id 
        ORDER BY p.id, sh.update_date 
        DESC """
        cursor.execute(query)
        raw_result = cursor.fetchall()
        result = []

        if status is not None:
            result = [
                property for property in raw_result if property[5] == status
            ]
        else:
            result = [
                property
                for property in raw_result
                if (
                    property[5] == 'pre_venta'
                    or property[5] == 'en_venta'
                    or property[5] == 'vendido'
                )
            ]

        return list(map(lambda property: Property(
            address=property[2],
            city=property[3],
            price=property[7],
            description=property[8],
            status=property[5]
        ), result))

    def to_domain(self, orm: Dict[str, Any], *args, **kwargs) -> _M:
        pass
