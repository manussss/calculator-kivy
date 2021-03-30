from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatButton

Window.size = (290, 400)

KV = '''
<MDButton>:
    text_color: 0, 0, 0, 1
    md_bg_color: app.theme_cls.primary_dark
    size_hint:None, None
    size: .5, 30

<CalcGridLayout>:
    id: calculator
    display: entry
    rows: 7
    padding: 5
    spacing: 5
    row_default_height: '50dp'
    row_force_default: True

    BoxLayout:
        TextInput:
            id: entry
            font_size: 32
            multiline: False

    BoxLayout:
        spacing: 5
        MDButton:
            text: "7"
            on_press: entry.text += self.text
        MDButton:
            text: "8"
            on_press: entry.text += self.text
        MDButton:
            text: "9"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 5
        MDButton:
            text: "4"
            on_press: entry.text += self.text
        MDButton:
            text: "5"
            on_press: entry.text += self.text
        MDButton:
            text: "6"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 5
        MDButton:
            text: "1"
            on_press: entry.text += self.text
        MDButton:
            text: "2"
            on_press: entry.text += self.text
        MDButton:
            text: "3"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 5
        MDButton:
            text: "AC"
            on_press: entry.text = ""
        MDButton:
            text: "0"
            on_press: entry.text += self.text
        MDButton:
            text: "/"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 5
        MDButton:
            text: "+"
            on_press: entry.text += self.text
        MDButton:
            text: "-"
            on_press: entry.text += self.text
        MDButton:
            text: "*"
            on_press: entry.text += self.text

    BoxLayout:
        MDRaisedButton:
            text: "="
            on_press: calculator.calculate(entry.text)
            size_hint: None, None
            size: 60, 30
'''
root = Builder.load_string(KV)

class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class MDButton(MDRectangleFlatButton):
    pass

class CalculatorApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        return CalcGridLayout()


calcApp = CalculatorApp()
calcApp.run()
