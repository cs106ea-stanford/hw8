import json
import random

import ipywidgets as widgets
from ipywidgets import HBox, VBox, HTML, Button, Output, Text, Label, FloatSlider, IntText
from IPython.display import clear_output

with open("alpaca_data.json", "r") as f:
    alpaca_data = json.load(f)  # Now we have a list of dictionaries

sample_size = 5

def show_samples(_):
    with text_output:
        text_output.clear_output()  # Properly clear previous output
        random_samples = random.sample(alpaca_data, sample_size)

        html_content = "<h3>Random Samples</h3>"
        for i, entry in enumerate(random_samples, start=1):
            html_content += f"""
            <div style="border: 1px solid #ddd; padding: 10px; margin: 5px; border-radius: 5px;">
                <strong>Example {i}:</strong><br>
                <b>🔹Instruction:</b> {entry['instruction']}<br>
                <b>🔹Input:</b> {entry['input'] if entry['input'] else 'N/A'}<br>
                <b>🔹Output:</b> {entry['output']}
            </div>
            """

        # Display HTML content inside the Output widget
        display(HTML(html_content))

text_output = Output()
more_response_btn = Button(description="Show Samples", button_style="info")

more_response_btn.on_click(show_samples)

def display_ui():
    display(VBox([more_response_btn, text_output]))
    show_samples(None)
