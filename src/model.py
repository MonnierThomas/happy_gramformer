# Download the T5-Gramformer model and define the settings
from happytransformer import HappyTextToText
from happytransformer import TTSettings

class Model:
    def __init__(self, transformer, model):
        try:
            self.happy_tt = HappyTextToText(load_path='model/')
            self.happy_tt.save("model/")
        except:
            print('The model needs to be downloaded')
            self.happy_tt = HappyTextToText(transformer,  model)
        self.settings = TTSettings(num_beams=5,  min_length=1, max_length=100)

    def loss(self, file):
        '''
        The input file must be tagged
        '''
        loss = self.happy_tt.eval(file)
        return loss