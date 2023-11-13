from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_FACTOR = 1.60934  # Constant for conversion factor


class ConvertMilesApp(App):
    km_result = StringProperty('0.0')  # Property to update the Label text

    def build(self):
        return Builder.load_file('convert_miles_km.kv')

    def handle_increment(self, value):
        try:
            miles = float(self.root.ids.miles_input.text) + value
            self.root.ids.miles_input.text = str(miles)
            self.calculate_conversion()
        except ValueError:
            self.root.ids.miles_input.text = '0'
            self.calculate_conversion()

    def handle_input_change(self):
        self.calculate_conversion()

    def calculate_conversion(self):
        try:
            miles = float(self.root.ids.miles_input.text)
            km = miles * MILES_TO_KM_FACTOR
            self.km_result = '{:.2f}'.format(km)
        except ValueError:
            self.km_result = '0.0'


if __name__ == '__main__':
    ConvertMilesApp().run()
