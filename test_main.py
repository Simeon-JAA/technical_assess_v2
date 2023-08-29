"""Testing file for main"""

from main import separate_input, get_constituency_name, translate_party_names
from main import get_percentage_of_votes, calculate_percentage


def test_separate_input_base_case_1():
    """Tests base case for separate_input"""

    result = separate_input(
        "Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD")

    assert result == ["Cardiff West", "11014", "C",
                      "17803", "L", "4923", "UKIP", "2069", "LD"]


def test_get_constituency_name_base_case_1():
    """Tests base case for get_constituency_name"""

    result = get_constituency_name(["Cardiff West", "11014", "C",
                                    "17803", "L", "4923", "UKIP", "2069", "LD"])

    assert result == "Cardiff West"


def test_translate_party_names_base_case_1():
    """Tests base case for translate_party_names"""

    result = translate_party_names(["Cardiff West", "11014", "C",
                                    "17803", "L", "4923", "UKIP", "2069", "LD"])

    assert result == ["11014", "Conservative Party",
                      "17803", "Labour Party", "4923", "UKIP", "2069", "Liberal Democrats"]


def test_get_percentage_of_votes_base_case_1():
    """Tests base case for get_percentage_of_votes"""

    result = get_percentage_of_votes(["11014", "Conservative Party",
                                      "17803", "Labour Party", "4923", "UKIP", "2069", "Liberal Democrats"])

    assert result == {
        "Conservative Party": 30.8,
        "Labour Party": 49.7,
        "UKIP": 13.7,
        "Liberal Party": 5.8}


def test_calculate_percentage_base_case_1():
    """Tests base case for calculate_percentages"""

    result = calculate_percentage(100, 20)

    assert result == 20


def test_calculate_percentage_base_case_2():
    """Tests base case for calculate_percentages"""

    result = calculate_percentage(60, 20)

    assert result == 33.3
