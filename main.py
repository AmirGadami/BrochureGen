from llm import create_brochure
import gradio as gr


app = gr.Interface(
    fn=create_brochure,
    inputs=[
        gr.Textbox(label="Company name:"),
        gr.Textbox(label="Landing page URL including http:// or https://")],
    outputs=[gr.Markdown(label="Brochure:")],
    flagging_mode="never"
)


# Launch the app
if __name__ == "__main__":

    app.launch(inbrowser=True)