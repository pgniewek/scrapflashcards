import pytest
from mock import patch
from scrapflashcards import scrap

def test_init():
    with patch.object(scrap, "main", return_value=42):
        with patch.object(scrap, "__name__", "__main__"):
            with patch.object(scrap.sys, 'exit') as mock_exit:
                scrap.init()

                assert mock_exit.call_args[0][0] == 42
    
def test_getCategoryMembers():
    sampleResult = [{'title': 'Carmen Mauri', 'pageid': 19087166, 'ns': 0}]
    assert scrap.getCategoryMembers("Category:History_of_Poland_during_the_Piast_dynasty", 1) == sampleResult
