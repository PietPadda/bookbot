def get_book(path):
    """Gets a book's txt from a path.

    Args:
        string: The string path.

    Returns:
        Text of the file path (string).
    """
    with open(path) as f:  # with closes files after run
        return f.read()  # get file as string


def count_words(string):
    """Counts the number of words in a string.

    Args:
        string: The string to analyze.

    Returns:
        The number of words in the string (int).
    """
    words = string.split()  # make individual words
    return len(words)  # count words


def count_char(string):
    """Makes string lowercase. Then builds unique and sorted char list. Finally counts to dictionary.

    Args:
        string: The string to analyze.

    Returns:
        A dictionary with char:count pairs (dict).
    """

    # make a sorted list of chars to use in dictionary
    lower_text = string.lower()  # make string lowercase
    unique_characters = set()  # init empty set
    for char in lower_text:  # loop each character in the string
        unique_characters.add(char)  # filter out uniq chars
    sorted_unique = sorted(list(unique_characters))  # create sorted list

    # count the chars
    char_counts = {}  # init dict
    for uniq_char in sorted_unique:
        char_counts[uniq_char] = 0  # start empty
        for text_char in lower_text:  # loop each char in the string
            if text_char == uniq_char:  # if it's = to unique char list
                char_counts[uniq_char] += 1  # update counter

    # print (f"DEBUG : Pre list of chars:\n\n {char_counts}\n\n")
    return char_counts  # return dict with counted unique chars


def alphabet_only(dict):
    """Takes the output of count_char and filters out only alphabet.

    Args:
        dict: The dict of char:count pair.

    Returns:
        A dictionary with only alphabet filtered out  (dict).
    """
    alpha_dict = {}  # init dict
    for key in dict:  # each char in dictionary
        if key.isalpha():  # if is alphabetical
            alpha_dict[key] = dict[key]  # add to new dictionary
    # print(f"DEBUG : alphabetical:\n\n {alpha_dict}\n\n")
    return alpha_dict  # dict with only alphabetical letters


def report_dict(dict):
    """Takes the output of alphabet_only and generates list of dicts. Use this to sort by sum ie count

    Args:
        dict: The dict of char:count pair.

    Returns:
        A list with keys sorted by descending sum  (list).
    """
    sum_dict = []  # init list

    for name, count in dict.items():  # get key and value from dict
        char_dict = {}  # dict per character to be added to list
        char_dict["name"] = name  # set chardict name = key
        char_dict["sum"] = count  # set chardict sum = value
        sum_dict.append(char_dict)  # add each chardict to the new list

    sum_dict.sort(reverse=True, key=lambda key: key["sum"])  # sort list by "sum" key in each dict inside list
    # print(f"DEBUG : sorted dicts by sum:\n\n {sum_dict}\n\n")

    return sum_dict


def text_report(dict, word_count):
    """Takes the output of report_dict and generates a report printout

    Args:
        list: a list of dictionaries, each corresponding to the name and count of a character

    Returns:
        A series of text for the  report  (string).
    """
    print("--- Begin report of books/frankenstein.txt ---")  # report header
    print(f"{word_count} words found in the document\n")  # summary of word wount

    for char_dict in dict:  # loop each dictionary inside list
        char = char_dict["name"]  # set char = name of each char dictionary ie character
        count = char_dict["sum"]  # set count = sum of each char dictionary ie sun
        print(f"The '{char}' character was found {count} times.")  # print each char count

    print("\n--- End report ---")  # report footer


def main():
    """Main function to read a file, count words, and print the count."""
    path = "books/frankenstein.txt"  # path to text
    text = get_book(path)  # get book from path
    word_count = count_words(text)  # generate word count
    counting = count_char(text)  # create sorted dict of chars counted
    alpha = alphabet_only(counting)  # filter out only alphabetical keys
    rep_dict = report_dict(alpha)  # generate dict of list of dict with sorted sum
    report = text_report(rep_dict, word_count)  # generate report to output


if __name__ == "__main__":
    main()
