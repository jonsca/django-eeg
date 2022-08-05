#captured from the ipynb I used to work all this up

import pyedflib.highlevel as phl
import numpy as np

#file_name = 'chb01_14.edf'
#file_name = 'test_generator.edf'

def return_epochs(file_name, epoch_length=30):
    signals,signal_headers,header = phl.read_edf(file_name)

    sigs = {}
    for n in range(len(signals)):
        end_time = len(signals[n])/signal_headers[n]['sample_frequency']
        num_points = len(signals[n])
        sigs[signal_headers[n]['label']] = (np.linspace(0, end_time, num_points), signals[n])

    epochs = {}
    labels = list(sigs.keys())

    for l in labels:
        sample_freq = [d['sample_frequency'] for d in signal_headers if d['label'] == l][0]
        time_divisor = int(len(sigs[l][0])/(epoch_length*sample_freq))
        signal_divisor = int(len(sigs[l][1])/(epoch_length*sample_freq))
        epochs[l] = (np.array_split(sigs[l][0], time_divisor), np.array_split(sigs[l][1], signal_divisor ))

    return epochs