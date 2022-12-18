import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
        
    vals = np.reshape(list, (3,3))
    
    calculations = {
        'mean': [np.mean(vals, axis=0).tolist(), np.mean(vals, axis=1).tolist(), np.mean(vals).tolist()],
        'variance': [np.var(vals, axis=0).tolist(), np.var(vals, axis=1).tolist(), np.var(vals).tolist()],
        'standard deviation': [np.std(vals, axis=0).tolist(), np.std(vals, axis=1).tolist(), np.std(vals).tolist()],
        'max': [np.amax(vals, axis=0).tolist(), np.amax(vals, axis=1).tolist(), np.amax(vals).tolist()],
        'min': [np.amin(vals, axis=0).tolist(), np.amin(vals, axis=1).tolist(), np.amin(vals).tolist()],
        'sum': [np.sum(vals, axis=0).tolist(), np.sum(vals, axis=1).tolist(), np.sum(vals).tolist()]
    }

    return calculations