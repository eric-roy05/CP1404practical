from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    def build(self):
        # Sample list of names
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']

        main_layout = BoxLayout(orientation='vertical')

        for name in names:
            label = Label(text=name, font_size=20)
            main_layout.add_widget(label)

        return main_layout


if __name__ == '__main__':
    DynamicLabelsApp().run()
