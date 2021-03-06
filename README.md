# UCSF BMI203 HW #3 Optimal Alignment

[![Build
Status](https://travis-ci.org/tcavazos2/hw3-OptimalAlign.svg?branch=master)](https://travis-ci.org/tcavazos2/hw3-OptimalAlign)

Example python project with testing.

## usage

To use the package, first make a new conda environment and activate it

```
conda create -n exampleenv python=3
source activate exampleenv
```

then run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `opt_align/__main__.py`) can be run as follows

```
# Run initial alignment 
python -m opt_align --align score_matrices/ Pospairs.txt Negpairs.txt

# Optimize scoring matrix given alignments where initaial alignments are computed using --align
python -m opt_align --optimize score_matrices/BLOSUM50 Pospairs.txt Negpairs.txt alignments_pos.txt alignments_neg.txt 
```

## testing

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.
