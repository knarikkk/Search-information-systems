import os
from utils.validators import check_dir_present
from utils.files import get_files_list, generate_dictionary_by_files
from utils.data import sort_dict, search
from utils.data_visualization import primary_data_table

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run():
    check_dir_present(BASE_DIR)
    files = get_files_list(BASE_DIR)
    data = sort_dict(generate_dictionary_by_files(files))
    primary_data_table(data)

    search(data)


if __name__ == "__main__":
    run()
