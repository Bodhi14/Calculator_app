from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self): # self is the constructor
        self.icon = "download.png"
        self.operators = ["/", "*", "+", "-","M"] # where operator is an object of the class build
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")

        self.solution = TextInput(background_color="black", foreground_color="white")

        main_layout.add_widget(self.solution) # add_widget is an internal property of BoxLayout

        buttons = [

            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
            ["", "", "", "M"],

        ]

        for row in buttons:
            h_layout = BoxLayout() # a row layout in the whole BoxLayout
            for label in row:
                button = Button(
                    text=label, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},

                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        equal = Button(
            text="=", font_size=20, background_color="green",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        equal.bind(on_press=self.on_solution)

        main_layout.add_widget(equal)

        return main_layout

    def on_button_press(self, instance): # instance the value getting passed by clicking on the button
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "M":
            current = self.solution.text
            self.solution.text = "M"
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
            self.last_button = button_text
            self.last_was_operator = self.last_button in self.operators


    def on_solution(self, instance):
        text = self.solution.text
        if text: # text is not null
            solution = str(eval(self.solution.text))
            self.solution.text = solution # updating the screen text





if __name__ == "__main__":
    app = MainApp()
    app.run()
