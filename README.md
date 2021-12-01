# Happy Gramformer

> Happy Transformer + Gramformer = Happy Gramformer

This repository provides an easy way to use the T5 Gramformer model for Grammatical Error Correction while using the extremely simple and useful Python package Happy Transformer. Thanks to HuggingFace, Gramformers' developers and Eric Fillion's HappyTransformer, it is now amazingly simple to correct sentences and batches with low effort and tremendous results.

# Table of contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [References](#references)
- [Fine-tuning](#fine-tuning)

# Installation

After cloning the project,

```
pip3 install requirements.txt
```

Export the project to your PYTHONPATH.

Create two folders at the root of the project: 
- 'inputs' containing the batches of sentences you want to correct
- 'results' to collect the results in csv files.

# Quick start

With Happy Gramformer, you can use either correct sentences or batches.

```
usage: main.py [-h] [--sentence SENTENCE [SENTENCE ...]] [--batch BATCH [BATCH ...]] [--csv CSV]

Choose between sentence or batch correction

optional arguments:
  -h, --help            show this help message and exit
  --sentence SENTENCE [SENTENCE ...]
                        enter the sentence(s) you want to correct
  --batch BATCH [BATCH ...]
                        enter the path of the batch(es) you want to correct
  --csv CSV             enter 1 to save the corrections in a csv file
```
  
Examples: 
  
```
python3 src/main.py --sentence 'It issnot true' 'I bought an new book .'
```
```
12/01/2021 11:03:57 - INFO - happytransformer.happy_transformer -   Using model: cpu
Original sentence:  It issnot true
Corrected sentence:  It is not true.
Correction:  True

time:  0.56 s
Original sentence:  I bought an new book .
Corrected sentence:  I bought a new book.
Correction:  True
time:  0.57 s
```

# Fine-tuning

<table> <thead> <tr> <th>Parameter</th> <th>Default</th> <th>Definition</th> </tr> </thead> <tbody> <tr> <td>min_length</td> <td>10</td> <td>Minimum number of generated tokens</td> </tr> <tr> <td>max_length</td> <td>50</td> <td>Maximum number of generated tokens</td> </tr> <tr> <td>do_sample</td> <td>False</td> <td>When True, picks words based on their conditional probability</td> </tr> <tr> <td>early_stopping</td> <td>False</td> <td>When True, generation finishes if the EOS token is reached</td> </tr> <tr> <td>num_beams</td> <td>1</td> <td>Number of steps for each search path</td> </tr> <tr> <td>temperature</td> <td>1.0</td> <td>How sensitive the algorithm is to selecting low probability options</td> </tr> <tr> <td>top_k</td> <td>50</td> <td>How many potential answers are considered when performing sampling</td> </tr> <tr> <td>top_p</td> <td>1.0</td> <td>Min number of tokens are selected where their probabilities add up to top_p</td> </tr> <tr> <td>no_repeat_ngram_size</td> <td>0</td> <td>The size of an n-gram that cannot occur more than once. (0=infinity)</td> </tr> </tbody> </table>

We are currently using these parameters in `src/model.py`: 
```
self.settings = TTSettings(num_beams=5,  min_length=1, max_length=100)
```

Feel free to change and test the different values to achieve the best results for your domain.

# References

- [Gramformer - GitHub](https://github.com/PrithivirajDamodaran/Gramformer)
- [HappyTransformer - GitHub](https://github.com/EricFillion/happy-transformer)

- [Gramformer - HuggingFace Model](https://huggingface.co/prithivida/grammar_error_correcter_v1)
- [Happy Transformer - Website](http://happytransformer.com/)

- [Gramformer: Correct Grammar With a Transformer Model](https://www.vennify.ai/gramformer-correct-grammar-transformer-nlp/)
