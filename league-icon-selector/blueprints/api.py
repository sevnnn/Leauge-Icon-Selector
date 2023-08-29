from io import BytesIO
from typing import Tuple

from flask import Blueprint, Response, current_app, send_file

from ..extensions.LCUCommunicator.lcu_communicator import LCUCommunicator

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/icon/<int:icon_id>", methods=["POST"])
def set_icon(icon_id: int) -> Response:
    lcu_communicator = current_app.extensions["lcu_communicator"]
    if not lcu_communicator or not isinstance(lcu_communicator, LCUCommunicator):
        return Response(status=500)

    lcu_communicator.set_icon(icon_id)

    return Response(status=204)


@bp.route("/icon/<int:icon_id>", methods=["GET"])
def get_icon(icon_id: int) -> Response:
    lcu_communicator = current_app.extensions["lcu_communicator"]
    if not lcu_communicator or not isinstance(lcu_communicator, LCUCommunicator):
        return Response(status=500)

    return send_file(
        BytesIO(lcu_communicator.get_image_bytes_for_icon_id(icon_id)),
        mimetype="image/jpg",
    )
