import sys
from ting_file_management.file_management import txt_importer


def check_file_exists(path_file, instance):
    for item in range(len(instance.queue)):
        return instance.search(item)["nome_do_arquivo"] == path_file


def process(path_file, instance):
    if not check_file_exists(path_file, instance):
        file_lines = txt_importer(path_file)
        qt_lines = len(file_lines)

        file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": qt_lines,
            "linhas_do_arquivo": file_lines
        }

        instance.enqueue(file_data)
        sys.stdout.write(str(file_data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
