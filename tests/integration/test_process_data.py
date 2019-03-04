import os
import sys
from scripts import processdata
from scripts import qusers
from scripts import qwords

#datapath = os.join("forrest_challenge","data","pickled_data")

# def setup_function(test_process_data): #not sure if param is right
#     datapath = os.join("forrest_challenge", "data", "pickled_data")
#     files = os.listdir(datapath)
#     if "utw_fixture.pickle" in files:
#         os.remove("utw_fixture.pickle")
#     if "utw_fixture.pickle" in files:
#         os.remove("wtu_fixture.pickle")


# def teardown_function(test_process_data):
#     datapath = os.join("forrest_challenge", "data", "pickled_data")
#     files = os.listdir(datapath)
#     if "utw_fixture.pickle" in files:
#         os.remove("utw_fixture.pickle")
#     if "wtu_fixture.pickle" in files:
#         os.remove("wtu_fixture.pickle")


#def test_process_data_check_files():
#should maybe test for type errors/ invalid inputs
#SHOULD maybe convert all worlds to lower case!!!