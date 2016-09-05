
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934

class MileToKilometre(App):
    def build(self):
        Window.size = (600, 200)
        self.title = "Covert Miles to Kilometres"
        self.root = Builder.load_file('mile_to_kilometres.kv')
        return self.root
    def convert_mile(self):
        value = self.get_validated_miles()
        output = value * MILES_TO_KM
        self.root.ids.output_label.text = str(output)
    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_number.text = str(value)
        self.convert_mile()
    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MileToKilometre().run()