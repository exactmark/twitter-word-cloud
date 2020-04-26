# A simple example of how to get a data set into memory from the page/data structure
from load_archive import get_data_from_archive

root_dir = "page"
target_time = "20200424170843"

trend_result,trend_map, status_dict = get_data_from_archive(root_dir, target_time)

print("Loaded trend: ",trend_result)
print("Trend_map: ",trend_map)
print(status_dict)
# print("Loaded %d statuses" % len(status_list))
