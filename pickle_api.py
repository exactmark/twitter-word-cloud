
import pickle
import bz2

def store_pickle(pickled_item,pickled_path):
    bz_file = bz2.BZ2File(pickled_path,'w')
    pickle.dump(pickled_item,bz_file)
    bz_file.close()

def get_pickle(pickled_path):
    pickled_file = bz2.BZ2File(pickled_path,'rb')
    pickled_item = pickle.load(pickled_file)
    pickled_file.close()
    return pickled_item
