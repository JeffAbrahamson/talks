from pandas import DataFrame

def build_data_frame(path, classification):
    data_frame = DataFrame({'text': [], 'class': []})
    for file_name, text in read_files(path):
        data_frame = data_frame.append(
                DataFrame({'text': [text], 'class': [classification]}, index=[file_name]))
    return data_frame
