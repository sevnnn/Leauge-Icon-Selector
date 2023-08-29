from io import BytesIO
from typing import Tuple

from flask import Blueprint, Response, current_app, send_file

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/icon/<int:icon_id>", methods=["POST"])
def set_icon(icon_id: int) -> Tuple[str, int]:
    current_app.extensions["lcu_communicator"].set_icon(icon_id)

    return "", 204


@bp.route("/icon/<int:icon_id>", methods=["GET"])
def get_icon(icon_id: int) -> Response:
    return send_file(
        BytesIO(
            current_app.extensions["lcu_communicator"].get_image_bytes_for_icon_id(
                icon_id
            )
        ),
        mimetype="image/jpg",
    )
