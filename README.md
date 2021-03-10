*David B. Blumenthal*

# Introduction to Python for Bioinformatics

In this course, targeted at PhD students in the biomedical sciences, participants will receive an introduction to the programming language Python. We will start with the basics (I/O, basic data structures, loops and conditions, functions, classes), introduce widely used packages for data manipulation and visualization ([NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [seaborn](https://seaborn.pydata.org/)), and will provide a first glimpse at the [Biopython](https://biopython.org/) package. 

# Getting Started

All course materials are provided as [Jupyter Notebooks](https://jupyter.org/index.html). To run Jupyter Notebooks on your machine, install an [Anaconda distribution](https://docs.anaconda.com/anaconda/install/) before the start of the course.

Now download the course material:

```bash
git clone https://github.com/dbblumenthal/python-intro
cd python-intro
```

And install all dependencies via [conda](https://docs.conda.io/en/latest/):

```bash
conda env create -f environment.yml
conda activate python-intro
```

You can now open the Notebooks as follows:

```bash
jupyter-notebook python-basics.ipynb
```



# Acknowledgements

This course uses material from Mark Bakker's [Exploratory computing with Python](http://mbakker7.github.io/exploratory_computing_with_python/) course.

# License

This course is licensed under the
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
