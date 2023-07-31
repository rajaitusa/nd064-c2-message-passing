from datetime import datetime
from app.udaconnect.schemas import (ConnectionSchema)
from app.udaconnect.services import ConnectionService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Project for people connection through geo location.")


@api.route("/persons/<person_id>/connection")
@api.param("start_date", "Enter start date", _in="query")
@api.param("end_date", "Enter end date", _in="query")
@api.param("distance", "Proximity of  user (meters)", _in="query")
class ConnectionDataResource(Resource):
    @responds(schema=ConnectionSchema, many=True)
    def get(self, person_id) -> ConnectionSchema:
        start_date: datetime = datetime.strptime(
            request.args["start_date"], DATE_FORMAT
        )
        end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
        distance: Optional[int] = request.args.get("distance", 5)

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance,
        )
        return results
