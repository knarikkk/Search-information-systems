import os


def check_dir_present(base_dir, doc_dir_name="doc"):
    doc_dir = os.path.join(base_dir, doc_dir_name)
    if not os.path.exists(doc_dir):
        os.mkdir(doc_dir)
