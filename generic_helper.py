import re
def extract_session_id(session_str : str):

    match = re.search(r"/sessions/(.*?)/contexts", session_str)
    if match :
        extract_string = match.group(1)
        return extract_string
    return ""

def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])


if __name__=="__main__":
    print(get_str_from_food_dict({"samosa":2, ":chhole": 5}))