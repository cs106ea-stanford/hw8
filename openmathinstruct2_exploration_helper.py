import random
from datasets import load_dataset

import ipywidgets as widgets
from ipywidgets import HTML, VBox, Button, Output
from IPython.display import display, Markdown


from datasets import load_dataset
# Load only the 1M subset (instead of full 14M dataset)
dataset = load_dataset("nvidia/OpenMathInstruct-2", split="train_1M")

# Convert to Pandas DataFrame
df = dataset.to_pandas()

# Create widgets
text_output = Output()
more_response_btn = Button(description="Show Samples", button_style="info")
sample_size = 5  # Default sample size

# Function to safely format LaTeX in Markdown
def format_latex(text):
    """Ensure LaTeX expressions are properly formatted for Markdown rendering."""
    if text is None:
        return ""

    return (
        text.replace("[", r"\[")
            .replace("]", r"\]")
            .replace(r"\(", r"$")  # Convert inline LaTeX to Markdown style
            .replace(r"\)", r"$")
    )

# Function to format and display LaTeX using Markdown
def show_samples(_):
    with text_output:
        text_output.clear_output()  # Clear previous output

        # Select random samples
        random_samples = df.sample(n=sample_size).to_dict(orient="records")

        # Create Markdown content for proper LaTeX rendering
        formatted_output = "### 📌 Random Samples\n\n"

        for i, entry in enumerate(random_samples, start=1):
            problem_text = format_latex(entry['problem'])
            generated_solution_text = format_latex(entry['generated_solution'])
            expected_answer_text = format_latex(entry['expected_answer'])

            formatted_output += (
                f"---\n"
                f"### Example {i}:\n"
                f"#### 🔹 Problem:\n"
                f"{problem_text}\n\n"
                f"#### ✍️ Generated Solution:\n"
                f"{generated_solution_text}\n\n"
                f"#### ✅ Expected Answer:\n"
                f"$$ {expected_answer_text} $$\n"
            )

        # Display using Markdown (ensures proper LaTeX rendering in Jupyter)
        display(Markdown(formatted_output))

        # ✅ **Force MathJax to render in Google Colab**
        display(HTML("<script>MathJax.Hub.Queue(['Typeset', MathJax.Hub]);</script>"))

# Function to display UI
def display_ui():
    display(VBox([more_response_btn, text_output]))
    show_samples(None)

# Bind button click event
more_response_btn.on_click(show_samples)
