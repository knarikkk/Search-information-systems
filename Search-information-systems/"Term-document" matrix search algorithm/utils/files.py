import os
from rich import print


def get_files_list(base_dir, doc_dir_name="doc", allowed_files=["txt"]):
    doc_dir = os.path.join(base_dir, doc_dir_name)
    files = [
        os.path.join(doc_dir, file)
        for file in os.listdir(doc_dir)
        if file.split(".")[-1] in allowed_files
    ]
    if not files:
        print("[red]No [italic bold]files[/italic bold] found[/]")
        exit(1)
    return files


def generate_dictionary_by_files(files):
    data = {}
    for file in files:
        with open(file, "r") as doc:
            for word in doc.read().split():
                word = word.lower()
                data[word] = {
                    *data.get(word, {}),
                    os.path.splitext(os.path.basename(file))[0],
                }
    return data
