import pyautogui as pag
from pyscreeze import Point as ps_Point
from alias import Alias, AliasType


def alert_image_not_found() -> None:
    pag.alert(text="Image Not Found!", title="SelecText")  # type: ignore


def alert_alias_not_found() -> None:
    pag.alert(text="Alias Not Found!", title="SelecText")  # type: ignore


def locate_by_image_file(filename: str) -> ps_Point | None:
    try:
        return pag.locateCenterOnScreen(filename, minSearchTime=0, confidence=0.9)
    except pag.ImageNotFoundException:
        alert_image_not_found()


def main() -> None:
    # init
    aliases: dict[str, Alias] = {
        "w": Alias(AliasType.FILENAME, "windows button.png"),
        "m": Alias(AliasType.FILENAME, "make min button.png"),
    }

    input_text: str = pag.prompt(text="Press command here.", title="SelecText")  # type: ignore

    try:
        found_alias: Alias = aliases[input_text]
    except KeyError:
        alert_alias_not_found()
        exit()

    found_point: ps_Point | None = None
    match found_alias.type:
        case AliasType.FILENAME:
            found_point = locate_by_image_file(found_alias.content)

        case AliasType.OTHER_TEXT:
            pag.alert(text="Sorry, this feature isn't available yet!", title="SelecText")  # type: ignore

    pag.moveTo(found_point, duration=0.3)


if __name__ == "__main__":
    main()
