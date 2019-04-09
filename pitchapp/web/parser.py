import time

MESSAGE_TYPE_DESC = {
    'A': 'Add order (short)',
    'd': 'Add order (long)',
    'E': 'Order executed',
    'X': 'Order cancel',
    'P': 'Trade (short)',
    'r': 'Trade (long)',
    'B': 'Trade Break',
    'H': 'Trading Status',
    'I': 'Auction Update',
    'J': 'Auction Summary',
    'R': 'Retail Price Improvement',
    's': 'Symbol Clear',
}


def parse_pitch_file(tmp_file):
    """
    Assuming the upladed file is in the right format.

    e.g.:
    S28805183<A>9K27G60000FPS002000QQQQ  0000495800Y
    S28805614<X>AK27GA0000EW000500
    S28805614<E>AK27GA0000EWS000500SPY   0001425300Y

    Returns a dict with the types found in the
    file and count of each entry
    (according to the PITCH documentation it's the 9th char)
    """
    parsed_dict = {}
    start = time.time()
    msg_type_pos = 9

    with open(tmp_file.file.name, 'r') as read_file:
        for line in read_file:
            msg_type = line[msg_type_pos]
            if msg_type not in parsed_dict.keys():
                parsed_dict[msg_type] = 1
            else:
                parsed_dict[msg_type] += 1

    # if we've reached here, it hasn't thrown
    # an error, do cleanup
    return_dict = {
        'filename': tmp_file.name,
        'time': round(time.time() - start, 3),
        'parsed_data': {MESSAGE_TYPE_DESC.get(k, k): v for k, v in parsed_dict.items()}
    }
    return return_dict
