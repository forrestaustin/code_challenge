#Example qusers 

```
forrest_challenge>python -m scripts.qusers "72.165.6.125" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; BTRS127482; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)"
---- output ----
beach
bikini
julianne-hough-miami-beach-bikini-babe-507555
celebrity-gossip
gossip
hough
julianne-hough
babe
miami
celebrity
julianne
beach
bikini
julianne-hough-miami-beach-bikini-babe-507555
celebrity-gossip
gossip
hough
julianne-hough
babe
miami
celebrity
julianne
````

# Example qwords
````
C:forrest_challenge>python -m scripts.qwords cat

--- output --
('98.97.43.85', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')
----
('138.37.51.219', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.25) Gecko/20111212 Firefox/3.6.25')
----
('96.116.131.62', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1')
----
('80.83.48.164', 'Mozilla/4.0 (compatible')
----
('114.55.90.68', 'Mozilla/4.0 (compatible')
----
('50.0.65.97', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7')
----
````

# Example running unit tessts
```
C:\Users\forre\Git_Repos\forrest_challenge>python -m pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.6.4, pytest-4.3.0, py-1.8.0, pluggy-0.9.0 -- C:\Users\forre\AppData\Local\Programs\Python\Python36-32\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\forre\Git_Repos\forrest_challenge, inifile:
collected 14 items

tests/test_dictools.py::test_adduser_entry[user_tuple0-wordlist0-input_dict0-output_dict0] PASSED                [  7%]
tests/test_dictools.py::test_adduser_entry[user_tuple1-wordlist1-input_dict1-output_dict1] PASSED                [ 14%]
tests/test_dictools.py::test_adduser_entry[user_tuple2-wordlist2-input_dict2-output_dict2] PASSED                [ 21%]
tests/test_dictools.py::test_addword_entry[user_tuple0-wordlist0-input_dict0-output_dict0] PASSED                [ 28%]
tests/test_dictools.py::test_addword_entry[user_tuple1-wordlist1-input_dict1-output_dict1] PASSED                [ 35%]
tests/test_dictools.py::test_addword_entry[user_tuple2-wordlist2-input_dict2-output_dict2] PASSED                [ 42%]
tests/test_parsetools.py::test_entryparse[IP: ipstring\nUA: uastring\nU: ustring\nR: rstring\n-result0] PASSED   [ 50%]
tests/test_parsetools.py::test_entryparse[IP: ipstring\nUA: uastring\nU: \nR: \n-result1] PASSED                 [ 57%]
tests/test_parsetools.py::test_entryparse[-result2] PASSED                                                       [ 64%]
tests/test_parsetools.py::test_entryparse[Some random string-result3] PASSED                                     [ 71%]
tests/test_parsetools.py::test_urltowords[http://www.stackoverflow.com/exit-vim-ulist0] PASSED                   [ 78%]
tests/test_parsetools.py::test_urltowords[https://www.docs.python.org/3-ulist1] PASSED                           [ 85%]
tests/test_parsetools.py::test_urltowords[001.microsoftadvertisingexchange.com-ulist2] PASSED                    [ 92%]
tests/test_parsetools.py::test_urltowords[adserv.brandaffinity.net/eas?cu=2267;cre=mu;target=_blank-ulist3] PASSED [100%]

============================================== 14 passed in 0.14 seconds ==============================================
```