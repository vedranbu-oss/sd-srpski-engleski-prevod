import gradio as gr
from googletrans import Translator
import modules.scripts as scripts

translator = Translator()

class TranslatePrompt(scripts.Script):
    def title(self):
        return "Srpski → Engleski prevod prompta"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        enable_translation = gr.Checkbox(label="Prevedi prompt sa srpskog na engleski", value=True)
        return [enable_translation]

    def process(self, p, enable_translation):
        if enable_translation and p.prompt:
            try:
                translated = translator.translate(p.prompt, src='sr', dest='en')
                p.prompt = translated.text
            except Exception as e:
                p.extra_generation_params = {"translation_error": str(e)}
