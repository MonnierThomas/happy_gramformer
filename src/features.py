import csv
import time
import pandas as pd
import numpy as np
from datetime import datetime

def time_function(func):
        '''
        Function used as a decorator that counts the time taken by the function for execution.
        '''
        def wrap(*args, **kwargs):
            start = time.perf_counter()
            func(*args, **kwargs)
            end = time.perf_counter()

            print('time: ', f'{round(end-start, 2)} s')
        return wrap

def create_csv(correction, path):
    '''
    Function used to create a csv file with the inputs, outputs, and other information.
    Inputs:
        texts: original sentences
        results: corrected sentences
        compare: booleans which provide information on whether there has been a correction
        too_long: booleans which provide information on whether the original sentences was too long and was not processed entirely
    '''
    texts, results, compare, too_long = correction.original_sentences, correction.corrected_sentences, correction.is_correction, correction.too_long
    df = pd.DataFrame(np.array([[text, result, detection, size] for text, result, detection, size in zip(texts, results, compare, too_long)]), columns=['Original sentence', 'Corrected sentence', 'Errors detected', 'Text is too long'])
    df = df.set_index('Original sentence')
    if path != None:
        path = path[0].split('/')[-1].split('.')[0]
        df.to_csv(f'results/{path}_results_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.csv')
    else:
        df.to_csv(f'results/results_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.csv')
       