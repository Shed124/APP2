import APP_datasets

###To use the variables inside APP_datasets : make sure to add "APP_datasets." before the variable. 

#Test : print(APP_datasets.avions_chaos_100)

Policies_order=[
    ("fuel","int"),
    ("technical_issue","bool"),
    ("medical","bool"),
    ("diplomatic_level","int")
]

def insertionSort(dataset, sort_key):
    global duplicates, duplicates_index
    duplicates = []
    duplicates_index = []

    for i in range(1, len(dataset)):
        key = dataset[i]
        j = i - 1
        while j >= 0 and key[sort_key] < dataset[j][sort_key]:
            dataset[j + 1] = dataset[j]
            j -= 1
        dataset[j + 1] = key

    for i in range(len(dataset)):
        for j in range(i + 1, len(dataset)):
            if dataset[i] == dataset[j] and dataset[i] not in duplicates:
                duplicates.append(dataset[i])
                duplicates_index.append(j)

    return dataset


def selectionSort(dataset, sort_key):
    global duplicates, duplicates_index
    duplicates = []
    duplicates_index = []

    for i in range(len(dataset)):
        min_idx = i
        for j in range(i + 1, len(dataset)):
            if dataset[j][sort_key] < dataset[min_idx][sort_key]:
                min_idx = j
        dataset[i], dataset[min_idx] = dataset[min_idx], dataset[i]

    for i in range(len(dataset)):
        for j in range(i + 1, len(dataset)):
            if dataset[i] == dataset[j] and dataset[i] not in duplicates:
                duplicates.append(dataset[i])
                duplicates_index.append(j)

    return dataset


def sort_with_tiebreaker(dataset, sort_keys):
    global duplicates, duplicates_index

    #First insertion sort by sort_keys[0]
    insertionSort(dataset, sort_keys[0])

    #Loop through remaining keys if there are still tie-breakers
    key_index = 1
    while duplicates and key_index < len(sort_keys):
        current_key = sort_keys[key_index]
        tied_values = [d[sort_keys[key_index - 1]] for d in duplicates]

        for val in tied_values:
            group_start = None
            group_end = None
            for i in range(len(dataset)):
                if dataset[i][sort_keys[key_index - 1]] == val:
                    if group_start is None:
                        group_start = i
                    group_end = i

            tied_group = dataset[group_start:group_end + 1]

            #Alternate between insertion (even) and selection (odd)
            if key_index % 2 == 0:
                insertionSort(tied_group, current_key)
            else:
                selectionSort(tied_group, current_key)

            dataset[group_start:group_end + 1] = tied_group

        #Recheck for duplicates on the whole list
        duplicates = []
        duplicates_index = []
        for i in range(len(dataset)):
            for j in range(i + 1, len(dataset)):
                if dataset[i] == dataset[j] and dataset[i] not in duplicates:
                    duplicates.append(dataset[i])
                    duplicates_index.append(j)

        key_index += 1

    if not duplicates:
        pass

    return dataset
