import os


def get_current_body(page_root):
    index_path = os.path.join(page_root, "index.html")
    print(os.path.normpath(index_path))
    if os.path.exists(index_path):
        print("totally exists")
    else:
        print("does not exist")


def convert_list_to_table(working_list):
    return_table = ["<table style = 'width:100%'>"]
    return_table.append("<tr>")
    for header_row_item in working_list[0]:
        return_table.append("<th>" +header_row_item + "</th>")
    return_table.append("</tr>")
    for body_row in working_list[1:]:
        return_table.append("<tr>")
        for body_row_item in body_row:
            return_table.append("<td>" +body_row_item + "</td>")
        return_table.append("</tr>")
    return_table.append("</table>")
    return return_table



# <td><img src='page\imgs\20200412163349\0.png' alt='0'></td>
def create_table_from_trend_dicts(date_time_num, date_time_str, trend_list, trend_urls_dict, page_root):
    working_list = [[date_time_str]]
    working_list.append(
        # <td><img src='.//imgs//20200412163349//trend_cloud.png' alt='cloud'></td>
        ["<img src='" + "/".join(["imgs", str(date_time_num), "trend_cloud.png'"]) + " alt='cloud'>"])
    linksrow = []
    images_row = []
    for single_link_index,single_link in enumerate( trend_list):
        linksrow.append(
            "<a href='" + trend_urls_dict[single_link[1]] + "'>" + single_link[1] + ": " + str(single_link[0]) + "</a>")
        images_row.append("<a href='"+("http://google.com"+str(trend_urls_dict[single_link[1]])[18:])+"'><img src='" + "/".join(["imgs", str(date_time_num), str(single_link_index)+".png'"]) + " alt='"+str(single_link_index)+"'></a>")
    working_list.append(linksrow)
    working_list.append(images_row)
    table = convert_list_to_table(working_list)
    print(table)
    print("\n".join(table))
    return table

def get_blank_index_list():
    return ["<!DOCTYPE html>","<html lang='en'>","<head>","    <meta charset='UTF-8'>","    <title>Title</title>","</head>","<body>","</body>","</html>"]

def append_table_to_index(page_root,new_table):
    index_path = os.path.join(page_root, "index.html")
    if not os.path.exists(index_path):
        print("does not exist")
        working_index = get_blank_index_list()
    else:
        print("totally exists")
        working_index = []
        with open(index_path,'r') as current_index_file:
            for line in current_index_file:
                working_index.append(line.rstrip())
    body_close_index = working_index.index("</body>")
    working_index = working_index[:body_close_index]+new_table+working_index[body_close_index:]
    with open(index_path,'w') as current_index_file:
        current_index_file.write('\n'.join(working_index))
