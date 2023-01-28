from typing import Optional

from src.property.adapters.repository import AbstractPropertyRepository, _M
from src.property.domain.models import Property
from src.property.service_layer import services
from src.property.service_layer.unit_of_work import \
    AbstractPropertyUnitOfWork


class FakePropertyRepository(AbstractPropertyRepository):

    def __init__(self):
        self.properties = [
            Property(
                address="Calle abc # 1 - 2",
                city="pereira",
                price=10000000,
                description="Hermoso apartamento en el centro de la ciudad",
                status="pre_venta"
            ),
            Property(
                address="Calle efg # 4 - 6",
                city="bogota",
                price=20000000,
                description="Hermoso apartamento en el norte de la ciudad",
                status="en_venta"
            ),
            Property(
                address="Calle xcv # 44 - 69",
                city="bogota",
                price=30000000,
                description="Apartamento en el norte de la ciudad year 2020",
                status="en_venta"
            )
        ]

    def filter(
        self,
        status: Optional[str],
        city: Optional[str],
        year: Optional[int]
    ) -> list[Optional[Property]]:
        properties = []

        if status:
            properties.extend(
                [
                    property
                    for property in self.properties
                    if property.status == status
                ]
            )
        if city:
            properties.extend(
                [
                    property
                    for property in self.properties
                    if property.city == city
                ]
            )
        if year:
            properties.extend(
                [
                    property
                    for property in self.properties
                    if property.description.__contains__("2020")
                ]
            )
        if not status and not city and not year:
            properties = self.properties

        return properties

    def to_domain(
        self, orm: dict[str, any], *args, **kwargs
    ) -> _M:
        pass


class FakePropertyUnitOfWork(AbstractPropertyUnitOfWork):
    properties = FakePropertyRepository()


def test_get_all_properties():
    uow = FakePropertyUnitOfWork()
    properties = services.get_properties(uow=uow)
    assert len(properties) == 3
    for i in range(len(properties)):
        assert properties[i]["address"] == uow.properties.properties[i].address


def test_get_filter_status_properties():
    uow = FakePropertyUnitOfWork()
    properties = services.get_properties(uow=uow, status="pre_venta")
    assert len(properties) == 1
    assert properties[0]["status"] == uow.properties.properties[0].status


def test_get_filter_city_properties():
    uow = FakePropertyUnitOfWork()
    properties = services.get_properties(uow=uow, city="pereira")
    assert len(properties) == 1
    assert properties[0]["city"] == uow.properties.properties[0].city


def test_get_filter_properties():
    uow = FakePropertyUnitOfWork()
    properties = services.get_properties(uow=uow, year=2010)
    assert len(properties) == 1
    assert properties[0]["address"] == uow.properties.properties[2].address


def test_get_filter_satus_and_year_properties():
    uow = FakePropertyUnitOfWork()
    properties = services.get_properties(
        uow=uow, status="pre_venta", year=2020
    )
    assert len(properties) == 2
    assert properties[0]["status"] == uow.properties.properties[0].status
    assert properties[1]["address"] == uow.properties.properties[2].address


def test_get_filter_satus_and_year_and_city_properties():
    uow = FakePropertyUnitOfWork()
    properties = services.get_properties(
        uow=uow, status="pre_venta", year=2020, city="pereira"
    )
    assert len(properties) == 3