"""
Set of parameterized unit tests for testing parsetools.

Some common cases that were testsed:
normal txt entry in valid format with all fields there
normal txt entry in valid format with missing fields
Not including parts such as http www. and ? query parameters in the urltowords
"""

import pytest
from scripts.parsetools import entryparse
from scripts.parsetools import urltowords


@pytest.mark.parametrize(
    'entry, result', [
        ("IP: ipstring\nUA: uastring\nU: ustring\nR: rstring\n", ("ipstring","uastring","ustring","rstring")),
        ("IP: ipstring\nUA: uastring\nU: \nR: \n", ("ipstring", "uastring", "", "")),
        ("", ("", "", "", "")),
        ("Some random string", ("", "", "", ""))
    ]
)
def test_entryparse(entry, result):
    assert entryparse(entry) == result
    assert type(entryparse(entry)) == tuple
    assert len(entryparse(entry)) == 4


@pytest.mark.parametrize(
    'url, ulist', [                              # to, a, in filtered out
        ("http://www.stackoverflow.com/exit-vim/to/a/in", ["stackoverflow", "exit-vim", "exit", "vim"]),
        ("https://www.docs.python.org/3", ["python", "docs"]),
        ("001.microsoftadvertisingexchange.com", ["microsoftadvertisingexchange"]),
        ("adserv.brandaffinity.net/eas?cu=2267;cre=mu;target=_blank", ["adserv", "brandaffinity", "eas"]),
    ]
)
def test_urltowords(url, ulist):
    assert set(urltowords(url)) == set(ulist)
    for word in ulist:
        assert len(word) >= 3



