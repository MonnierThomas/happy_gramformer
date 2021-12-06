# Download the T5-Gramformer model and define the settings
from happytransformer import HappyTextToText
from happytransformer import TTSettings
from happytransformer import TTTrainArgs
from datetime import datetime

class Model:
    def __init__(self, transformer, model):
        try:
            self.happy_tt = HappyTextToText(load_path='model/')
        except:
            print('The model needs to be downloaded')
            self.happy_tt = HappyTextToText(transformer,  model)
            self.happy_tt.save("model/")
        self.settings = TTSettings(num_beams=5,  min_length=1, max_length=100)

    def loss(self, file):
        '''
        The input file must be tagged
        '''
        loss = self.happy_tt.eval(file)
        return loss
    
    def fine_tune(self, file, batch_size=8):
        '''
        The input file must contain two columns: input and target
        The input column must contain for every row 'grammar: {text}'
        The target column can contain one or more suggestions of correction
        '''
        args = TTTrainArgs(batch_size=batch_size)
        self.happy_tt.train(file, args=args)
        self.happy_tt.save(f'model_finetuning_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}/')