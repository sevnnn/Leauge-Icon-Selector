from flask import Blueprint, Response, current_app, render_template

from ..extensions.LCUCommunicator.lcu_communicator import LCUCommunicator

bp = Blueprint("frontend", __name__)


@bp.route("/", methods=["GET"])
def index() -> Response:
    lcu_communicator = current_app.extensions["lcu_communicator"]
    if not lcu_communicator or not isinstance(lcu_communicator, LCUCommunicator):
        return Response(status=500)

    return Response(
        render_template(
            "icon-selector.jinja",
            owned_icons=lcu_communicator.get_owned_icons(),
            current_icon=lcu_communicator.get_current_icon(),
        )
    )
