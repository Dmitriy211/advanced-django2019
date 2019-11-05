import re


def spec_char_validate(value):
    spec = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if spec.search(value) is not None:
        return False
    else:
        return True
