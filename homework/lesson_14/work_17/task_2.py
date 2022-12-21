def dict_handler(link_on_dict: dict, key, default_value):
    try:
        try:
            return link_on_dict[key]
        except KeyError:
            return link_on_dict.update({key: default_value})

    except TypeError as err:
        print(err, ": dictionary key cannot be mutable data types!")


if __name__ == '__main__':
    arr = {2: "one"}
    dict_handler(arr, 3, "one")
