"""Sample fixture data used for integration testing

"""

utw_fix_dict = {
    ("12.34.56.78", "Mozilla/5.0 (Windows NT 6.1)"): ["petsmart", "cats-dog", "tim", "cats", "dog"],
    ("00.00.00.00", ""): ["salon", "category", "news"],
    ("11.11.11.11", ""): ["wikipedia","wiki", "Austin_Texas"]
}

wtu_fix_dict = {
    "petsmart": ("12.34.56.78", "Mozilla/5.0 (Windows NT 6.1)"),
    "cats-dog": ("12.34.56.78", "Mozilla/5.0 (Windows NT 6.1)"),
    "cats": ("12.34.56.78", "Mozilla/5.0 (Windows NT 6.1)"),
    "dogs": ("12.34.56.78", "Mozilla/5.0 (Windows NT 6.1)"),
    "tim": ("12.34.56.78", "Mozilla/5.0 (Windows NT 6.1)"),
    "salon": ("00.00.00.00", ""),
    "category": ("00.00.00.00", ""),
    "news": ("00.00.00.00", ""),
    "wikipedia": ("11.11.11.11", ""),
    "wiki": ("11.11.11.11", ""),
    "Austin_Texas": ("11.11.11.11", "")
}

