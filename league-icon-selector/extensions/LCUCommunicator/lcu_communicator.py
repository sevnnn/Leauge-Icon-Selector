from typing import List, Optional

from flask import Flask
from requests import Response, get, put
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from .DTO.IconDTO import IconDTO


class LCUCommunicator:
    GET_ICONS_ENDPOINT = "/lol-catalog/v1/items/SUMMONER_ICON"
    GET_CURRENT_SUMMONER_ENDPOINT = "/lol-summoner/v1/current-summoner"
    SET_ICON_ENDPOINT = "/lol-summoner/v1/current-summoner/icon"
    GET_ICON_DETAILS_ENDPOINT = "/lol-catalog/v1/item-details"
    GET_ICON_IMAGE_ENDPOINT = "/lol-game-data/assets/v1/profile-icons/%s.jpg"

    def __init__(self, app: Flask) -> None:
        disable_warnings(InsecureRequestWarning)
        self.host = app.config.get("LCU_HOST")
        self.auth = app.config.get("LCU_AUTH")
        self.owned_icons: List[IconDTO]

    def __api_get_request(
        self, endpoint: str, query_params: Optional[dict] = None
    ) -> Response:
        response = get(
            f"{self.host}{endpoint}",
            headers={"Authorization": self.auth},  # type: ignore
            params=query_params,
            verify=False,
        )

        return response

    def __api_put_request(self, endpoint: str, body: Optional[dict] = None) -> Response:
        response = put(
            f"{self.host}{endpoint}",
            headers={"Authorization": self.auth},  # type: ignore
            json=body,
            verify=False,
        )

        return response

    def get_owned_icons(self) -> List[IconDTO]:
        icons_raw = self.__api_get_request(self.GET_ICONS_ENDPOINT).json()
        icons_list: List[IconDTO] = []
        for icon_data in icons_raw:
            if icon_data["owned"] == False:
                continue

            icons_list.append(IconDTO(icon_data["itemId"], icon_data["name"]))
        self.owned_icons = icons_list

        return icons_list

    def get_current_icon(self) -> IconDTO:
        current_summoner = self.__api_get_request(
            self.GET_CURRENT_SUMMONER_ENDPOINT
        ).json()
        current_icon_name = self.__api_get_request(
            self.GET_ICON_DETAILS_ENDPOINT,
            {
                "inventoryType": "SUMMONER_ICON",
                "itemId": current_summoner["profileIconId"],
            },
        ).json()
        return IconDTO(
            current_summoner["profileIconId"], current_icon_name["item"]["name"]
        )

    def set_icon(self, icon_id: int) -> None:
        self.__api_put_request(self.SET_ICON_ENDPOINT, {"profileIconId": icon_id})

    def get_image_bytes_for_icon_id(self, icon_id: int) -> bytes:
        return self.__api_get_request(
            self.GET_ICON_IMAGE_ENDPOINT % str(icon_id)
        ).content
