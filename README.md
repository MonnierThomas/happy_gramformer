# Happy Gramformer

> Happy Transformer + Gramformer = Happy Gramformer

This repository provides an easy way to use the T5 Gramformer model for Grammatical Error Correction while using the extremely simple and useful Python package Happy Transformer. Thanks to HuggingFace, Gramformers' developers and Eric Fillion's HappyTransformer, it is now amazingly simple to correct sentences and batches with low effort and tremendous results.

# Table of contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [References](#references)
- [Tuning](#tuning)
- [Fine-tuning](#fine-tuning)
- [Docker](#docker)
- [References](#references)

# Installation

After cloning the project,

```
pip3 install requirements.txt
```

Export the project to your PYTHONPATH.

Create three folders at the root of the project: 
- `inputs` containing the batches of sentences you want to correct
- `results` to collect the results in csv files
- `model` to store the model and use the dockerfile

# Quick start

With Happy Gramformer, you can use either correct sentences or batches.

```
usage: main.py [-h] [--sentence SENTENCE [SENTENCE ...]] [--batch BATCH [BATCH ...]] [--csv CSV] [--loss LOSS [LOSS ...]] [--finetune FINETUNE]

Choose between sentence or batch correction

optional arguments:
  -h, --help            show this help message and exit
  --sentence SENTENCE [SENTENCE ...]
                        enter the sentence you want to correct
  --batch BATCH [BATCH ...]
                        enter the path of the batch you want to correct
  --csv CSV             enter 1 to save the corrections in a csv file
  --loss LOSS [LOSS ...]
                        enter the path of the file(s) to get the loss of the model on it
  --finetune FINETUNE   enter the path of the csv file for fine-tuning the model
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

-------

```
python3 src/main.py --batch inputs/test_1.txt inputs/test_2.txt
```

with `test_1.txt` and `test_2.txt` two `.txt` files containing only sentences to be corrected, separated by a line break.

-------

Results can be returned in a csv file, containing four columns:
- Original sentence <the inputs>
- Corrected sentence <the results>
- Errors detected <a boolean / True if there is at least one correction>
- Text is too long <a boolean / True if the number of tokens surpasses the maximum of tokens authorized>

# Tuning

<table> <thead> <tr> <th>Parameter</th> <th>Default</th> <th>Definition</th> </tr> </thead> <tbody> <tr> <td>min_length</td> <td>10</td> <td>Minimum number of generated tokens</td> </tr> <tr> <td>max_length</td> <td>50</td> <td>Maximum number of generated tokens</td> </tr> <tr> <td>do_sample</td> <td>False</td> <td>When True, picks words based on their conditional probability</td> </tr> <tr> <td>early_stopping</td> <td>False</td> <td>When True, generation finishes if the EOS token is reached</td> </tr> <tr> <td>num_beams</td> <td>1</td> <td>Number of steps for each search path</td> </tr> <tr> <td>temperature</td> <td>1.0</td> <td>How sensitive the algorithm is to selecting low probability options</td> </tr> <tr> <td>top_k</td> <td>50</td> <td>How many potential answers are considered when performing sampling</td> </tr> <tr> <td>top_p</td> <td>1.0</td> <td>Min number of tokens are selected where their probabilities add up to top_p</td> </tr> <tr> <td>no_repeat_ngram_size</td> <td>0</td> <td>The size of an n-gram that cannot occur more than once. (0=infinity)</td> </tr> </tbody> </table>

We are currently using these parameters in `src/model.py`: 
```
self.settings = TTSettings(num_beams=5,  min_length=1, max_length=100)
```

Feel free to change and test the different values to achieve the best results for your domain.
  
# Fine-tuning

Thanks to Eric Fillion's Happy Transformer package, it is very easy to fine-tune Gramformer for Grammatical Error Correction.
  
In order to fine-tune Gramformer, you need to build a dataset in a csv file with:
  - `input` column containing source sentences with the prefix 'grammar: ' / example: 'grammar: I have bought an new book'
  - `target` column containing one or more reference sentences
  
Then, run:
```
python3 src/main.py --finetune path_of_file.csv
```
  
or:
```
docker run happy_transformer:latest --finetune path_of_file.csv'
```

The model will be saved in a folder `model_finetune_[datetime]`
  
# Docker

It's now a possibility to use Docker to run Happy Gramformer. Since Docker is not able to download the model from the internet via HuggingFace, we need the model to be saved in the model folder that you created before. 
  
The model has not been upload on this repository because it is too heavy. But you need it locally for Docker to work.
  
Follow these steps in order to build:

- `python3 src/main.py                                # it will save the model in the model directory` 
- `docker build . -t happy_gramformer --network=host  # it will build the docker image`
  
Then you can do whatever you want (from correcting sentences to batches and saving the results in csv files):
Example:
- `docker run happy_gramformer:latest --sentence 'I have bought an book .'`

# References

- [Gramformer - GitHub](https://github.com/PrithivirajDamodaran/Gramformer)
- [HappyTransformer - GitHub](https://github.com/EricFillion/happy-transformer)
- [Gramformer - HuggingFace Model](https://huggingface.co/prithivida/grammar_error_correcter_v1)
- [Happy Transformer - Website](http://happytransformer.com/)
- [Gramformer: Correct Grammar With a Transformer Model](https://www.vennify.ai/gramformer-correct-grammar-transformer-nlp/)
- [Fine-Tune a Transformer Model for Grammar Correction](https://www.vennify.ai/fine-tune-grammar-correction/)
