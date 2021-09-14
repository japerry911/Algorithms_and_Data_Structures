from typing import Dict, List

import pytest


def tournament_winner(
        competitions: List[List[str]],
        results: List[int]
) -> str:
    """calculates which competitor wins the most matches, where results says
        who wins
    :param List[List[str]] competitions: the matches that take place, in this
        format -> [[home-team, away-team], ...]
    :param List[int] results: the results array of each match, a 1 says home
        team wins, a 0 says away team wins
    :returns: winning team's name
    :rtype: str
    """
    score_dict = dict()
    zipped_results_list = list(zip(competitions, results))

    for teams, result in zipped_results_list:
        if result == 0:
            score_dict = add_score_to_dict(score_dict, teams[1])
        else:
            score_dict = add_score_to_dict(score_dict, teams[0])

    return max(score_dict, key=score_dict.get)


def add_score_to_dict(score_dict: Dict[str, int], team: str) -> Dict[str, int]:
    if team not in score_dict:
        score_dict[team] = 0
    score_dict[team] += 1
    return score_dict


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
    assert tournament_winner(input_3a, input_3b) == expected_output_3


pytest.main(["TournamentWinner"])
