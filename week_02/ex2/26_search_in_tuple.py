def search_in_tuple(yes, num_search):
    if num_search in yes:
        print(f'Element found at Index: {yes.index(num_search)}')
    else:
        print('Element not found in the tuple')
search_in_tuple([20,15,10,30], 15)
