from typing import Dict


def nested_key_solution(nested_key: Dict = None, keys: str = None):
    extracted_keys = keys.split("/")  # FETCHING INDIVIDUAL KEYS IN THE FORM OF LIST FROM THE PROVIDED STRING KEYS
    try:
        for index, key_to_look in enumerate(extracted_keys):  # ITERATING OVER THE KEYS LIST
            value = nested_key.get(key_to_look)
            if value:
                nested_key = value
            else:
                raise ValueError
        return value
    except ValueError as error:
        print(f"Found None value in the given Object please check the object provided")


if __name__ == '__main__':
    # Given sample inputs
    object_s = {"x": {"y": {"z": "a"}}}
    key = "x/y/z"
    extracted_value = nested_key_solution(object_s, key)
    print(f'Extracted value is {extracted_value}')
