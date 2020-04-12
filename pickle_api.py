
import pickle

def store_pickle(pickled_item,pickled_path):
    pickle_file = open(pickled_path,'ab')
    pickle.dump(pickled_item,pickle_file)
    pickle_file.close()
    
def get_pickle(pickled_path):
    pickled_file = open(pickled_path,'rb')
    pickled_item = pickle.load(pickled_file)
    pickled_file.close
    return pickled_item
