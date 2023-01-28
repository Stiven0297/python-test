import abc

from src.property.adapters import repository


class AbstractPropertyUnitOfWork(abc.ABC):
    properties = repository.AbstractPropertyRepository


class PropertyUnitOfWork(AbstractPropertyUnitOfWork):
    properties = repository.PropertyRepository()
