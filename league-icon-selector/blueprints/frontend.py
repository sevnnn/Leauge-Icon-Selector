from flask import Blueprint, current_app, render_template

bp = Blueprint("frontend", __name__)


@bp.route("/", methods=["GET"])
def index() -> str:
    return render_template(
        "icon-selector.jinja",
        owned_icons=current_app.extensions["lcu_communicator"].get_owned_icons(),
        current_icon=current_app.extensions["lcu_communicator"].get_current_icon(),
    )
