import re


def normalize_phone(phone_number: str) -> str:
    """Function get unformatted phone and return formatted phone"""
    formatted_phone = phone_number.strip()

    start = ""
    if formatted_phone.startswith("+"):
        start = "+"

    pattern = r"\D"
    formatted_phone = re.sub(pattern, "", formatted_phone)

    if start == "+":
        return "+" + formatted_phone
    if formatted_phone.startswith("38"):
        return "+" + formatted_phone
    return "+38" + formatted_phone


# list_of_numbers = [
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
#     "+37(050)8889900",
# ]

# for phone in list_of_numbers:
#     print(normalize_phone(phone))
