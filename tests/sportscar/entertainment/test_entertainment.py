#test_entertainemt.py

from pytest import mark


@mark.ui
@mark.entertainment
def test_can_navigate_to_webpage(chrome_browser):
    chrome_browser.get('https://www.siriusxm.com/')
    assert True

