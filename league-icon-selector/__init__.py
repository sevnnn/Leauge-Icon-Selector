from base64 import b64encode
from json import load

from flask import Flask

from .blueprints import api as api_blueprint
from .blueprints import frontend as frontend_blueprint
from .extensions.LCUCommunicator.lcu_communicator import LCUCommunicator


def create_app() -> Flask:
    app = Flask(__name__)
    create_config(app)
    load_extensions(app)
    register_blueprints(app)

    return app


def create_config(app: Flask) -> None:
    app.config.from_file("..\\config.json", load=load)
    app.config.update(LEAGUE_RUNNING=False)
    try:
        with open(f"{app.config.get('LEAGUE_PATH')}\\lockfile", "r") as lockfile:
            lockfile_params = lockfile.read().split(":")
            basic_auth_credentials = f"riot:{lockfile_params[3]}"
            app.config.update(
                LEAGUE_RUNNING=True,
                LCU_HOST=f"{lockfile_params[4]}://127.0.0.1:{lockfile_params[2]}",
                LCU_AUTH=f"Basic {b64encode(basic_auth_credentials.encode()).decode()}",
            )
    except FileNotFoundError:
        print("League Of Legends must be running for this application to work!")
        exit(2)


def load_extensions(app: Flask) -> None:
    app.extensions["lcu_communicator"] = LCUCommunicator(app)


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(frontend_blueprint.bp)
    app.register_blueprint(api_blueprint.bp)
