from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import time
import qrcode as qr

class QRGenApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=(20, 120, 20, 20), spacing=20, size_hint=(1, 1))

        # Set background color of the layout to black
        self.layout.canvas.before.clear()
        with self.layout.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.image_layout = FloatLayout(size_hint=(1, 0.8))  # Adjust the size_hint to move the image down

        self.image = Image(source="bruh2.png", size_hint=(None, None), size=("300dp", "300dp"), allow_stretch=True, keep_ratio=True, pos_hint={"center_x": 0.5, "center_y": 0.5 - 0.1})  # Adjust 'center_y' to move the image down
        self.image_layout.add_widget(self.image)

        self.label = Label(text="Custom QR Code Generator", font_size=24, color=(1, 1, 1, 1), padding_y=0)  # White text color and increased padding at the bottom

        self.data_input = TextInput(text="Enter Text here", size_hint=(1, None), height="48dp", font_size=18)
        self.data_input.background_color = (1, 1, 1, 1)  # White text input background

        self.btn_generate = Button(text="Generate", size_hint=(0.5, None), height="48dp", font_size=18)
        self.btn_generate.background_color = (0.2, 0.2, 0.2, 1)  # Dark gray button background
        self.btn_generate.bind(on_press=self.generate_qr)

        self.layout.add_widget(self.image_layout)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.data_input)
        self.layout.add_widget(self.btn_generate)
        return self.layout

    def generate_qr(self, instance):
        qr_data = self.data_input.text
        qr_img = qr.make(qr_data)

        # Generate a unique filename using the current timestamp
        filename = f"myqr_{int(time.time())}.png"
        qr_img.save(filename)

        # Update the displayed image
        self.image.source = filename

if __name__ == "__main__":
    QRGenApp().run()
