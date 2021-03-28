
def thesaurus (*args):
    dict_names = {}
    for item in args:
        first_let = item[0]
        if not dict_names.get(first_let):
            dict_names[first_let] = [item]
        else: dict_names[first_let].append(item)
    return dict(sorted(dict_names.items()))

names = thesaurus("Андрей", "Иван", "Артур", "Руслан", "Екатерина", "Элла", "Римма")
print(names)