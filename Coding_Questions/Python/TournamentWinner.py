from typing import List

import pytest


def tournament_winner(
        competitions: List[List[str]],
        results: List[int]
) -> str:
    pass


def test_tournament_winner():
    input_1a = [
      ["HTML", "C#"],
      ["C#", "Python"],
      ["Python", "HTML"]
    ]
    input_1b = [0, 0, 1]
    expected_output_1 = "Python"
    assert tournament_winner(input_1a, input_1b) == expected_output_1

    input_2a = [
      ["HTML", "Java"],
      ["Java", "Python"],
      ["Python", "HTML"]
    ]
    input_2b = [0, 1, 1]
    expected_output_2 = "Java"
    assert tournament_winner(input_2a, input_2b) == expected_output_2

    input_3a = [
      ["AlgoMasters", "FrontPage Freebirds"],
      ["Runtime Terror", "Static Startup"],
      ["WeC#", "Hypertext Assassins"],
      ["AlgoMasters", "WeC#"],
      ["Static Startup", "Hypertext Assassins"],
      ["Runtime Terror", "FrontPage Freebirds"],
      ["AlgoMasters", "Runtime Terror"],
      ["Hypertext Assassins", "FrontPage Freebirds"],
      ["Static Startup", "WeC#"],
      ["AlgoMasters", "Static Startup"],
      ["FrontPage Freebirds", "WeC#"],
      ["Hypertext Assassins", "Runtime Terror"],
      ["AlgoMasters", "Hypertext Assassins"],
      ["WeC#", "Runtime Terror"],
      ["FrontPage Freebirds", "Static Startup"]
    ]
    input_3b = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
    expected_output_3 = "AlgoMasters"
    assert tournament_winner(input_3a, input_3b)


pytest.main(["TournamentWinner"])
