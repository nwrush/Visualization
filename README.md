# Visualization

This project is still in active development, but is mostly stable. Various features are subject to appear or disappear with little/no notice.

## Current Release

v1.0 - [Link](https://github.com/nwrush/Visualization/releases)

## About

This project builds on the work done by Chenhao Tan and Dallas Card in [this paper](https://chenhaot.com/pages/idea-relations.html). This tool provides a way to visualize text interactively using the relations outlined in the paper.

# Installation
Installing has been tested on Windows (7 and higher) (64-bit), Linux (Centos7), and some version of OSX. For convenience install scripts are provided for Windows and Linux.
Binaries are also provided for Windows and Linux.

After running any of the installation methods, if you've never used NLTK you will need to download the NLTK stopword corpus. Activate the virtualenv for the application and run `python -m nltk.downloader stopwords`

### Requirements
- Python3 (only tested on 3.5 and higher)
- A display
    - Running over a x-server is possibly but does not look good

## Installing from the repo

### Linux Installation
1. Download or clone the repo
2. Change the value of the variables $PYTHONPATH and $VenvPath to point to your system python installation and virtualenv
3. Run `./FullSetup.sh`
    - This will create the application in a new folder called Application
4. Activate the virtualenv (Application/venv)
5. Run the visualizer with: `python Visualizer.py`

### Windows Installation
1. Download or clone the repo
2. Change the value of the variable PythonPath to point to your system python installation
3. Run `FullSetup.bat`
    - This will create the application in a new folder called Application
4. Activate the virtualenv
    - If you called FullSetup.bat from the command line, the virtualenv may already be active
5. Run the visualizer with: `python Visualizer.py`

### Manual Installation
1. Download or clone the repo
2. Run: `git submodule init` and then `git submodule update`
3. Create a new folder where you want to install the application
4. From the folder Visualizer, copy all .py files and all folders to your application folder
6. Copy the top level idea_relations folder into the application folder
7. Create a virtual environment containing the packages listed in the FullRequirements.txt file
8. Activate the virtual environment and run the visualizer with `python Visualizer.py`

### Anaconda Installation
1. Follow the Manual Installation instructions up to step 6
2. Instead of creating a python virtualenv, you can create an anaconda environment containing the packages in Conda_package_list.txt
    - Linux and Windows users can try to use the appropriate spec file
3. Run the program the same as the manual installation instructions

## Packaged Installation

The application is distributed in three forms. A standalone Windows binary, standalone Linux binary, and the plain python files.
Both the Windows and Linux binary should run without any issue, just double click on the executable (Visualizer.exe) to run.
The Linux binary should function on any Linux system (including OSX), but has only been tested on Centos 7.

For the python files, you must have python version >3.5 available on your system. Installation is similar to the manual installation. Unpack the zip file and follow the manual installation instructions above from step 7.

Because of the much larger size of the Windows and Linux binaries, it is probably better to use the python version, especially if you already have Python 3 on your system.

As of right now, the prepacked installations cannot run the preprocessor due to bugs with scipy. A fix will potentially be available late December. Using a virtualenv with the raw python files works fine though.

## Note for Windows installation

On Windows, it may be difficult/impossible to install scipy using pip. To get around that we recommend downloading a prebuilt wheel for numpy and scipy from [this](https://www.lfd.uci.edu/~gohlke/pythonlibs/) website. You will need wheels for both numpy and scipy. Download the appropriate wheel for your system (matching python version and architecture).
If you're installing the program from the repo using the installation scripts, place them in the root directory for the repo, and edit lines 52 and 53 of FullSetup.py to have the correct file names. If you're installing from the zipped python files, copy them wherever you unpacked the code and install them using pip into your virtualenv. You must install them
before you install packages from FullRequirements.txt otherwise pip will install numpy from the web and then be unable to install scipy.
If you're installing from the standalone Windows binary, you don't need to do anything.

# Usage

The preprocessor can be run in two modes, Keywords and Topics. In keywords, the system will take two files a "input" file and a "background" file. The system calculates the prevelance of each word in both files, and creates the topic list from the top n words/phrases in the input file that aren't in the background file. While not necessary, the background file should be in the same domain as the input file for more accurate results.
In Topic mode the system will run LDA on the input file using Mallet to "learn" the top 50 topics on its own. This doesn't require a background file, but does take significantly longer (~30 minutes on the demo dataset).
Further details for how the topics are selected is available in [this paper](https://chenhaot.com/pages/idea-relations.html).

After running the preprocessor to get the relationships a new tab will open with the plot of the relationships between topics. Each dot on the graph represents a single topic/topic pair, if there are more than 1000 pairs then 1000 items will be selected randomly to populate the graph. Selecting an item will display the frequency time series for each relation as well as populating the 'Top Relation' filters.

On the left side of the window is the filter tab area, here you can filter down the visible topics. Selecting items in the ideas tab causes all relationship involving the selected ideas to populate the graph. In the types tab, relations are sorted by their type and strength, selecting a relationship here causes all relations involving either topic to appear on the graph. The other two tabs here 'Top Relation 1' and 'Top Relation 2' simply display a sorted list of the strength of all relations each selected topic has.

You can save visualizations for later use from the File menu, this saves you from having to wait for the preprocessor to run again. Additionally, you can load multiple visualizations into multiple tabs. In the visualization menu you can save images of the current PMI/correlation plot and the time series plot, the images saved are exactly what appears on the screen when you hit save.

## Input file format

Input files should be given as jsonlists, one document per line. The only two fields needed are date and text. 
The date will be parsed using the [python dateutil library](http://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.parse) with a default date of datetime(1,1,1) and all other arguemnts at their defaults. It will be converted to a string first as well. The text should be just the full text of the document properly quoted. For examples see acl.jsonlist in the included [example data folder](./examples).
The datafile can be compressed with gz before being passed in.

Two example visualizations are provided for you, acl.p and nips_t.p. The first one is the acl dataset in acl.jsonlist.gz processed using keywords with the nips dataset as the background file, the second one is the nips dataset processed using topics.

## Preprocessor options

You must pass the preprocessor 3 options, exploration name which determines what the visualization will be called (mainly setting the tab title), the number of ideas (which tells the preprocessor how many ideas to look for), and time grouping (year, month, day) to set the time scale the preprocessor uses when grouping articles. There are also 3 optional options, Tokenize, Lemmatize, and No Stop Words. These will perform the relevant preprocessing to the data before searching for topics. Additionally, you can use the advanced options to force the preprocessor to save it's intermediate output data somewhere else if you wanted. The intermediate data isn't terrible useful/readable though.

![Visualizer Screenshot](./Vis_OrigColors.png)
