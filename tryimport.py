# -*- coding: utf-8 -*-

# standard imports
from __future__ import print_function, division


# third party imports
imports = ["Quandl", "pyhoofinance", "googlefinance"]
for i in imports:
    try:
        exec("import {}".format(i))
        print("[INFO] '{}' successfully imported".format(i))

    except:
        print("[WARN] '{}' not available".format(i))


##############################################################################
# Do some really important stuff below...
##############################################################################

