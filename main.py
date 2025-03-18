import pyautogui


def main() -> None:
    commands: dict[str, str] = {"w": "windows button.png", "m": "make min button.png"}

    terget: str = pyautogui.prompt(text="Press command here.", title="SelecText")  # type: ignore

    try:
        pyautogui.moveTo(
            pyautogui.locateCenterOnScreen(
                commands[terget],
                minSearchTime=0,  # confidence=0.5
            ),
            duration=0.3,
        )
    except KeyError:
        pyautogui.alert(text="Command Not Found!", title="SelecText")  # type:ignore
    except pyautogui.ImageNotFoundException:
        pyautogui.alert(text="Image Not Found!", title="SelecText")  # type:ignore


if __name__ == "__main__":
    main()
