from webob import Response

from src.property.service_layer import services
from src.property.service_layer.unit_of_work import PropertyUnitOfWork
from src.utils.entrypoints.api import API

app = API()


@app.route("/property")
class PropertyResource:
    def get(self, req):
        uow = PropertyUnitOfWork()
        params = req.json_body

        response = services.get_properties(
            uow=uow,
            status=params.get("status", ""),
            city=params.get("city", ""),
            year=params.get("year", "")
        )
        return Response(
            status=200, json=response, content_type='application/json'
        )
