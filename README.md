# XGBFIR
XGBoost Feature Interactions Reshaped

### What is Xgbfi?
Xgbfir is a [XGBoost](https://github.com/dmlc/xgboost) model dump parser, which ranks features as well as feature interactions by different metrics.

This project started as a python port of [Xgbfi - XGBoost Feature Interactions &amp; Importance project](https://github.com/Far0n/xgbfi). Thanks Far0n for great tool and idea!

Some basic description from Xgbfi project page is presented here.

### The Metrics
 * **Gain**: Total gain of each feature or feature interaction
 * **FScore**: Amount of possible splits taken on a feature or feature interaction
 * **wFScore**: Amount of possible splits taken on a feature or feature interaction weighted by the probability of the splits to take place
 * **Average wFScore**: *wFScore* divided by *FScore*
 * **Average Gain**: *Gain* divided by *FScore*
 * **Expected Gain**: Total gain of each feature or feature interaction weighted by the probability to gather the gain
 * **Average Tree Index**
 * **Average Tree Depth**

### Additional Features
 * **Leaf Statistics**
 * **Split Value Histograms**

## Installation

You have several options to install Xgbfir. 

### Using pip
You can install using the pip package manager by running

    pip install xgbfir

### ~~Using conda~~
Sorry, conda build is not ready yet. Please build from source.

~~You can install using the conda package manager by running~~

~~conda install~~

### From source
Clone the repo and install:

    git clone https://github.com/limexp/xgbfir.git
    cd xgbfir
    sudo python setup.py install
	
Or download the source code by pressing 'Download ZIP' on this page. Install by navigating to the proper directory and running

    sudo python setup.py install

## Usage
Xgbfir is a CLI (Command Line Interface) tool, so you can run it with command:

    xgbfir [options]

Use the following command for help:

    xgbfir --help

**XGBoost model dump must be created before running xgbfir**. More information on [Xgbfi page](https://github.com/Far0n/xgbfi).
	

## Dependencies
* python (2.7+ or 3.5+)
* xlsxwriter (>=0.9.3)

## TODO
Xgbfir is in beta now, so there are several ways for improvement:
* Add more information and error messages, handle wrong input
* Make code style cool
* Cover with tests
* Add non-CLI
* Parse model from XGBoost without dumping
* Optimize code
* Add new functions
	
## Questions
Feel free to contact me, open issues or pull requests.
