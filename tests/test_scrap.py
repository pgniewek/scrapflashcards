import pytest
from mock import patch

def test_init():
    from scrapflashcards import scrap
    with patch.object(scrap, "main", return_value=42):
        with patch.object(scrap, "__name__", "__main__"):
            with patch.object(scrap.sys, 'exit') as mock_exit:
                scrap.init()

                assert mock_exit.call_args[0][0] == 42
    
