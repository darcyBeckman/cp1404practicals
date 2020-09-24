from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMileToKm(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value, difference):
        result = value + difference
        self.root.ids.input_value.text = str(result)

    def convert_miles(self, value):
        result = value * 1.609
        self.root.ids.output_value.text = str(result)


ConvertMileToKm().run()
