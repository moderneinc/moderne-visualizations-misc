import os
import yaml

ignore_words = [
    "ESLint",
]

def sentence_case(sentence: str):
    """
    Capitalize the first letter of the first word unless the word is all caps.
    """
    words = sentence.split()

    for index, word in enumerate(words):
        # if word is ALL UPPER then leave it alone
        if word.isupper() or word in ignore_words:
            pass
        # if word ends in lowercase s but rest is uppercase then leave it alone
        elif word[:-1].isupper() and word[-1] == 's':
            pass
        # title the first word
        elif index == 0:
            words[index] = word.title()
        else:
            words[index] = word.lower()

    return " ".join(words)


def check_sentence_casing(spec_filename):
    check_status = True

    with open(f"./moderne_visualizations_misc/specs/{spec_filename}", 'r') as stream:
        try:
            spec = yaml.safe_load(stream)
            # check any value or nested value named "displayName"
            display_names = []

            display_names.append(spec.get('displayName'))

            for option in spec.get('options', []):
                option_dict = option.get(next(iter(option)))
                if option_dict:
                    display_names.append(option_dict.get('displayName'))

            for display_name in display_names:
                if sentence_case(display_name) == display_name:
                    print(f"    ✅ {display_name}")
                else:
                    print(
                        f"    ❌ {display_name} --> {sentence_case(display_name)}")
                    check_status = False

        except yaml.YAMLError as exc:
            print(exc)
            return False
    return check_status


print("\nCheck if display names are sentence case")
print("-----------------------------------------------------------------------------")

# get list of all notebooks in the moderne_visualizations_misc directory
spec_filenames = [
    filename for filename in os.listdir('./moderne_visualizations_misc/specs') if filename.endswith(".yml")]

exit_code = 0

for spec_filename in spec_filenames:
    print(spec_filename)
    if check_sentence_casing(spec_filename):
        pass
    else:
        exit_code = 1

exit(exit_code)
