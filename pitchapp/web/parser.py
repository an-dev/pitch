"""
Assuming the upladed file is in the right format.

e.g.:
S28805183<A>9K27G60000FPS002000QQQQ  0000495800Y
S28805614<X>AK27GA0000EW000500
S28805614<E>AK27GA0000EWS000500SPY   0001425300Y

Returns a dict with the types found in the
file and count of each entry, highlited by the gt/lt brackets
(or according to the PITCH documentation it's the 10th char)
"""


def parse_pitch_file(tmp_file):
    parsed_dict = {}
    with open(tmp_file, 'r') as read_file:
        for line in read_file:
            msg_type = line[9]
            if line not in parsed_dict.keys():
                parsed_dict[msg_type] = 1
            else:
                parsed_dict[msg_type] += 1
    return parsed_dict