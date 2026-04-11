import APP_datasets


def policies_order():
    """This function defines our policies order by asking the user to input the order of the policies one by one
    Output : String if the user has done something wrong, List of Tuples if everything is good.
    """
    global policies_orders
    policies_orders=[]
    for i in range(4):
        L=str(input("Enter the policies order with the actual writing which is ; fuel, medical, technical_issue and diplomatic_level one by one : "))
        if L=="fuel" or L=="diplomatic_level":
            policies_orders.append((L,"int"))
        elif L=="medical" or L=="technical_issue":
            policies_orders.append((L,"bool"))
        else:
            return "Error in the typing of the policy or policy not found."
    return policies_orders

def compare(a, b, sort_key, key_type):
    """The role of this function is to define how two dictionaries are compared depending on the type of the key.
    a & b : dictionnary 
    sort_key : Key to compare, mostly String
    key_type : Type to detect, mostly String
    output : Confirms if a should come before or after b, boolean
    """
    if key_type == "bool":
        return a[sort_key] > b[sort_key]
    return a[sort_key] < b[sort_key]

def insertionSort(dataset, sort_key, key_type):
    """This function sorts the list by building a sorted portion one element at a time from left to right.
    dataset : List of dictionaries
    sort_key : key to compare, mostly String
    key_type : Type to detect, mostly String
    output : Dataset but sorted
    """
    global duplicates, duplicates_index
    duplicates = []
    duplicates_index = []

    for i in range(1, len(dataset)):
        key = dataset[i]
        j = i - 1
        while j >= 0 and compare(key, dataset[j], sort_key, key_type):
            dataset[j + 1] = dataset[j]
            j -= 1
        dataset[j + 1] = key

    for i in range(len(dataset)):
        for j in range(i + 1, len(dataset)):
            if dataset[i] == dataset[j] and dataset[i] not in duplicates:
                duplicates.append(dataset[i])
                duplicates_index.append(j)

    return dataset

def selectionSort(dataset, sort_key, key_type):
    """This function sorts the list by repeatedly finding the element that should come first and placing it at the front.
    dataset : List of dictionaries
    sort_key : key to compare, mostly String
    key_type : Type to detect, mostly String
    output : dataset but sorted
    """
    global duplicates, duplicates_index
    duplicates = []
    duplicates_index = []

    for i in range(len(dataset)):
        min_idx = i
        for j in range(i + 1, len(dataset)):
            if compare(dataset[j], dataset[min_idx], sort_key, key_type):
                min_idx = j
        dataset[i], dataset[min_idx] = dataset[min_idx], dataset[i]

    for i in range(len(dataset)):
        for j in range(i + 1, len(dataset)):
            if dataset[i] == dataset[j] and dataset[i] not in duplicates:
                duplicates.append(dataset[i])
                duplicates_index.append(j)

    return dataset


def sort_with_tiebreaker(dataset, policies):
    """This function is the main function to use for sorting the datasets and how it manages if there are tiebreakers, then the policies switches.
    dataset : List of dictionaries
    policies : List of policies/tuples
    """
    global duplicates, duplicates_index
    if len(policies)==0:
        return "The list of policies is empty"
    else:
        first_key, first_type = policies[0]
        insertionSort(dataset, first_key, first_type)
    
        key_index = 1
        while duplicates and key_index < len(policies):
            current_key, current_type = policies[key_index]
            prev_key, prev_type       = policies[key_index - 1]
            tied_values = [d[prev_key] for d in duplicates]
    
            for val in tied_values:
                group_start = None
                group_end   = None
                for i in range(len(dataset)):
                    if dataset[i][prev_key] == val:
                        if group_start is None:
                            group_start = i
                        group_end = i
    
                tied_group = dataset[group_start:group_end + 1]
    
                if key_index % 2 == 0:
                    insertionSort(tied_group, current_key, current_type)
                else:
                    selectionSort(tied_group, current_key, current_type)
    
                dataset[group_start:group_end + 1] = tied_group
    
            duplicates = []
            duplicates_index = []
            for i in range(len(dataset)):
                for j in range(i + 1, len(dataset)):
                    if dataset[i] == dataset[j] and dataset[i] not in duplicates:
                        duplicates.append(dataset[i])
                        duplicates_index.append(j)
    
            key_index += 1
    
        return dataset
