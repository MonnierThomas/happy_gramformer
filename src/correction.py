from src.features import time_function

from termcolor import colored

class Correction:
    def __init__(self):
        self.original_sentences = []
        self.corrected_sentences = []
        self.is_correction = []
        self.too_long = []

    @time_function
    def correct_sentence(self, original_sentence, happy_tt, settings):
        '''
        GEC correction with the Gramformer model for a single input.
        '''
        self.original_sentences.append(original_sentence)

        if len(original_sentence) > 250:
            print(colored('Careful, your text is too long and will not be processed entirely!', 'red'))
            self.too_long.append('True')
        else:
            self.too_long.append('False')

        print('Original sentence: ', colored(original_sentence, 'red'))

        text = "gec: " + original_sentence
        self.corrected_sentences.append(happy_tt.generate_text(text, args=settings).text)
        print('Corrected sentence: ', colored(self.corrected_sentences[-1], 'green'))

        self.is_correction.append(str(original_sentence != self.corrected_sentences[-1]))
        print('Correction: ', self.is_correction[-1])