import gradio as gr
from src.tone_of_review import get_prediction


demo = gr.Interface(fn=get_prediction, inputs="text", outputs="text")


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")