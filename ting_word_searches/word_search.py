def exists_word(word, instance):
    result = []

    for index in range(len(instance.queue)):
        has_word_in = []
        file_data = instance.search(index)

        for index, line in enumerate(file_data["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                has_word_in.append({
                    "linha": index + 1
                })

        if len(has_word_in) > 0:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": has_word_in
            })

    return result


def search_by_word(word, instance):
    result = []

    for index in range(len(instance.queue)):
        has_word_in = []
        file_data = instance.search(index)

        for index, line in enumerate(file_data["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                has_word_in.append({
                    "linha": index + 1,
                    "conteudo": line
                })

        if len(has_word_in) > 0:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": has_word_in
            })

    return result
