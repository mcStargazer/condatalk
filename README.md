# condatalk
Code to support the OKC Python User's Group 2015-11-11 talk entitled, **_Anaconda/Conda: A platform for replicable science with Python and “The Others”._** Assumes Git and Anaconda or Miniconda are already installed. Within the commandline instructions below, the first time you try to interpret the tryimport.py script, you'll get warnings that the imports are not available. The second time you try it, there should simply be informational messages of success.

Commandline Instructions for Windows:<br>
0. git clone https://github.com/mcStargazer/condatalk.git<br>
1. cd condatalk<br>
2. python tryimport.py
3. conda env create -n condatalk -f condatalk_windows.yml<br>
4. activate condatalk<br>
5. python tryimport.py

Commandline Instructions for Linux:<br>
0. git clone https://github.com/mcStargazer/condatalk.git<br>
1. cd condatalk<br>
2. python tryimport.py
3. conda env create -n condatalk -f condatalk_linux.yml<br>
4. source activate condatalk<br>
5. python tryimport.py

Useful links for exploring Anaconda/Miniconda/Conda are as follows, and I quote:
* [Go here to get Git](http://git-scm.com/download/)
* [Go here to get Anaconda or Miniconda](http://bit.ly/condaquickinstall)
* [30 minute test drive of conda](http://bit.ly/tryconda)
* [A data science with conda tutorial](http://continuum.io/content/conda-data-science)
* [General conda advocacy](http://continuum.io/why-anaconda)
