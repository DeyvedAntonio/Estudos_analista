from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class Calculadora(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text="0",
                    pos_hint={"center_x": 0.1, "center_y": 0.1},
                ),
                MDRectangleFlatButton(
                    text="+/-",
                    pos_hint={"center_x": 0.3, "center_y": 0.1},
                ),
                MDRectangleFlatButton(
                    text="=",
                    pos_hint={"center_x": 0.4, "center_y": 0.1},
                ),
                MDRectangleFlatButton(
                    text="1",
                    pos_hint={"center_x": 0.1, "center_y": 0.2},
                ),
                MDRectangleFlatButton(
                    text="2",
                    pos_hint={"center_x": 0.2, "center_y": 0.2},
                ),
                MDRectangleFlatButton(
                    text="3",
                    pos_hint={"center_x": 0.3, "center_y": 0.2},
                ),
                MDRectangleFlatButton(
                    text="4",
                    pos_hint={"center_x": 0.1, "center_y": 0.3},
                ),
                MDRectangleFlatButton(
                    text="5",
                    pos_hint={"center_x": 0.2, "center_y": 0.3},
                ),
                MDRectangleFlatButton(
                    text="6",
                    pos_hint={"center_x": 0.3, "center_y": 0.3},
                ),
                MDRectangleFlatButton(
                    text="+",
                    pos_hint={"center_x": 0.4, "center_y": 0.3},
                ),
                MDRectangleFlatButton(
                    text="7",
                    pos_hint={"center_x": 0.1, "center_y": 0.4},
                ),
                MDRectangleFlatButton(
                    text="8",
                    pos_hint={"center_x": 0.2, "center_y": 0.4},
                ),
                MDRectangleFlatButton(
                    text="9",
                    pos_hint={"center_x": 0.3, "center_y": 0.4},
                ),
                MDRectangleFlatButton(
                    text="-",
                    pos_hint={"center_x": 0.4, "center_y": 0.4},
                ),
                MDRectangleFlatButton(
                    text="C",
                    pos_hint={"center_x": 0.1, "center_y": 0.5},
                ),
                MDRectangleFlatButton(
                    text="CE",
                    pos_hint={"center_x": 0.2, "center_y": 0.5},
                ),
                MDRectangleFlatButton(
                    text="/",
                    pos_hint={"center_x": 0.3, "center_y": 0.5},
                ),
                MDRectangleFlatButton(
                    text="*",
                    pos_hint={"center_x": 0.4, "center_y": 0.5},
                )
            )
        )


Calculadora().run()
