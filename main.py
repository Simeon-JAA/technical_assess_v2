"""Solution to technical assessment pt 2"""


def separate_input(string: str) -> list[str]:
    """Will return a list separating the name and votes"""

    string = string.strip()

    string = string.split(', ')

    return string


def get_constituency_name(input: list[str]) -> str:
    """Returns constituency name from list input"""

    return input[0]


def translate_party_names(input: list[str]) -> list[str]:
    """Returns list of strings with translated party names"""

    party_codes = {
        "C": "Conservative Party",
        "L": "Labour Party",
        "UKIP": "UKIP",
        "LD": "Liberal Democrats",
        "G": "Green Party",
        "Ind": "Independent",
        "SNP": "SNP"}

    input = input[1:]

    for i, value in enumerate(input):
        if not value.isnumeric() and value in party_codes:
            input[i] = party_codes[value]

    return input


def calculate_percentage(total_votes: int, current_votes: int) -> float:
    """Returns the % of votes for given party"""

    percentage_vote = (current_votes/total_votes) * 100

    return round(percentage_vote, 1)


def get_percentage_of_votes(input: list[str]) -> dict:
    """Returns dictionary with key as party name and value as vote percentage"""

    total_votes = 0

    vote_perentage = {}

    for entry in input:
        if entry.isnumeric():
            total_votes += int(entry)

    for index, entry in enumerate(input):
        if not entry.isnumeric():
            number_of_votes = int(input[index - 1])
            party_name = entry
            vote_perentage[party_name] = calculate_percentage(
                total_votes, number_of_votes)

    print(vote_perentage)
    return vote_perentage


if __name__ == "__main__":
    separate_input()
