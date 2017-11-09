# XGBFIR [![Build Status](https://ci.appveyor.com/api/projects/status/github/limexp/xgbfir?branch=master&svg=true)](https://ci.appveyor.com/project/limexp/xgbfir) [![PyPI version](https://badge.fury.io/py/xgbfir.svg)](https://pypi.python.org/pypi/xgbfir/)

XGBoost Feature Interactions Reshaped


### What is Xgbfir?
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

### From source
Clone the repo and install:

    git clone https://github.com/limexp/xgbfir.git
    cd xgbfir
    sudo python setup.py install
	
Or download the source code by pressing 'Download ZIP' on this page. Install by navigating to the proper directory and running

    sudo python setup.py install

## Usage
You can use Xgbfir as a python function or as a CLI (Command Line Interface) tool.

### Python function

You can produce feature interactions file without saving any model dump file beforehand:
```python
import xgbfir

xgbfir.saveXgbFI(booster) # booster is a XGBoost booster
```

List of saveXgbFI function parameters:
 * **booster** - XGBoost booster or XGBClassifier
 * **feature_names** (default = None) - feature names that *will be set in booster*
 * **OutputXlsxFile** (default = 'XgbFeatureInteractions.xlsx') - output file name
 * **MaxTrees** (default = 100) - Upper bound for trees to be parsed
 * **MaxInteractionDepth** (default = 2) - Upper bound for extracted feature interactions depth
 * **MaxDeepening** (default = -1) - Upper bound for interaction start deepening (zero deepening => interactions starting at root only)
 * **TopK** (default = 100) - Upper bound for exported feature interactions per depth level
 * **MaxHistograms** (default = 10) - Maximum number of histograms
 * **SortBy** (default = 'Gain') - Score metric to sort by (Gain, FScore, wFScore, AvgwFScore, AvgGain, ExpGain)

### Python example

Take a look at this example of usage (available in [examples](https://github.com/limexp/xgbfir/tree/master/examples)):

```python
from sklearn.datasets import load_iris, load_boston
import xgboost as xgb
import xgbfir

# loading database
boston = load_boston()

# doing all the XGBoost magic
xgb_rmodel = xgb.XGBRegressor().fit(boston['data'], boston['target'])

# saving to file with proper feature names
xgbfir.saveXgbFI(xgb_rmodel, feature_names=boston.feature_names, OutputXlsxFile='bostonFI.xlsx')


# loading database
iris = load_iris()

# doing all the XGBoost magic
xgb_cmodel = xgb.XGBClassifier().fit(iris['data'], iris['target'])

# saving to file with proper feature names
xgbfir.saveXgbFI(xgb_cmodel, feature_names=iris.feature_names, OutputXlsxFile='irisFI.xlsx')
```


### CLI 

Xgbfir can be run as a console tool with the following command:

    xgbfir [options]

Use the following command for help:

    xgbfir --help

**XGBoost model dump must be created before running xgbfir**. 

To dump a model with proper feature names use the following code:
```python
booster.feature_names = list(feature_names) # set names for XGBoost booster
booster.dump_model('xgb.dump', with_stats=True)
```

## Dependencies
* python (2.7+ or 3.5+)
* xlsxwriter (>=0.9.3)


## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md).

Feel free to [open issues](https://github.com/limexp/xgbfir/issues) or pull requests.

