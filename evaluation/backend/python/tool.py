from time import time
import numpy as np

def predict_topk(scores, max_k):
    # top_k item index (not sorted)
    s = time()
    # order from the smallest to biggest
    relevant_items_partition = (-scores).argpartition(max_k, 1)[:, 0:max_k]
    # top_k item score (not sorted)
    # relevant_items_partition_original_value = prediction[relevant_items_partition]
    relevant_items_partition_original_value = np.take_along_axis(scores, relevant_items_partition, 1)
    # top_k item sorted index for partition

    # get indexes of sorting
    relevant_items_partition_sorting = np.argsort(-relevant_items_partition_original_value, 1)
    # sort top_k index
    # prediction = relevant_items_partition[relevant_items_partition_sorting]

    # get back values from indexes
    topk = np.take_along_axis(relevant_items_partition, relevant_items_partition_sorting, 1)
    # print('topk:', time() - s)

    return topk