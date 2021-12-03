from src.model import Model
from src.correction import Correction
from src.features import create_csv

import argparse
from icecream import ic

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Choose between sentence or batch correction')
    parser.add_argument('--sentence', nargs='+', help='enter the sentence you want to correct')
    parser.add_argument('--batch', nargs='+', help='enter the path of the batch you want to correct')
    parser.add_argument('--csv', help='enter 1 to save the corrections in a csv file')
    parser.add_argument('--loss', nargs='+', help='enter the path of the file(s) to get the loss of the model on it')
    parser.add_argument('--finetune', help='enter the path of the csv file  for fine-tuning the model')
    args = parser.parse_args()
    
    model = Model("T5",  "prithivida/grammar_error_correcter_v1")
    correction = Correction()
    
    if args.sentence != None:
        for sentence in args.sentence:
            correction.correct_sentence(sentence, model.happy_tt, model.settings)
    
    if args.batch != None:
        for batch in args.batch:
            with open(batch) as f:
                sentences = f.read().splitlines()
                for sentence in sentences:
                    correction.correct_sentence(sentence, model.happy_tt, model.settings)

    if args.csv == '1':
        try:
            create_csv(correction.original_sentences, correction.corrected_sentences, correction.is_correction, correction.too_long)
        except:
            print("No inputs")

    if args.loss != 'None':
        for file in args.loss:
            print(model.loss(file))
    
    if args.finetune != 'None':
        file = args.finetune
        model.fine_tune(file)