from TTS.api import TTS
import gradio as gr
import os

# Load model
# This will download the model to the local directory or cache
print("Downloading/Loading Model...")
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False) # Helper for CPU

def speak(text):
    output_path = "output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

# UI
with gr.Blocks(title="TTS by Qahir") as demo:
    gr.Markdown("# 🗣️ Text-to-Speech Converter")
    with gr.Row():
        inp = gr.Textbox(label="Enter text", placeholder="Hello, how are you?")
        out = gr.Audio(label="Speech Output")
    btn = gr.Button("Generate Speech")
    btn.click(speak, inp, out)

if __name__ == "__main__":
    demo.launch()
