# Download the T5-Gramformer model and define the settings
from happytransformer import HappyTextToText
from happytransformer import TTSettings

class Model:
    def __init__(self, transformer, model, do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100):
        self.happy_tt = HappyTextToText(transformer,  model)
        self.settings = TTSettings(num_beams=5,  min_length=1, max_length=100)