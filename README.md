*David B. Blumenthal*

# Introduction to Python for Bioinformatics

In this course, targeted at PhD students in the biomedical sciences, participants will receive an introduction to the programming language [Python 3](https://www.python.org/). We will start with the basics (I/O, basic data structures, loops and conditions, functions, classes) and then introduce widely used packages for data manipulation, scientific computing, and visualization ([NumPy](https://numpy.org/), [SciPy](https://www.scipy.org/), [pandas](https://pandas.pydata.org/), [seaborn](https://seaborn.pydata.org/)). Finally, the course will provide a first glimpse at two widely used packages for the analysis of biological data ([Biopython](https://biopython.org/), [GSEAPY](https://gseapy.readthedocs.io/en/latest/index.html)).

# Getting Started

All course materials are provided as [Jupyter Notebooks](https://jupyter.org/index.html). To run Jupyter Notebooks on your machine, install an [Anaconda distribution](https://docs.anaconda.com/anaconda/install/) before the start of the course.

Now download the course material into a directory called `python-intro`. For this, either click on **Code → Download ZIP**, or download the course material via [git](https://git-scm.com/): 

```bash
git clone https://github.com/dbblumenthal/python-intro
```

After downloading the course material, navigate to the `python-intro` directory and create a [conda](https://docs.conda.io/en/latest/) environment called **python-intro** with all dependencies:

```bash
cd python-intro
conda env create -f environment.yml
```

You can now activate the environment and connect it to your Jupyter Notebook:

```bash
conda activate python-intro
(python-intro) python -m ipykernel install --user --name=python-intro
```

Now you can open your first notebook as follows:

```sh
(python-intro) jupyter notebook first_steps.ipynb
```

If the Notebook opens without any errors, you are ready for the course.

# Acknowledgements

This course uses material from Mark Bakker's [Exploratory computing with Python](http://mbakker7.github.io/exploratory_computing_with_python/) course.

# License

This course is licensed under the
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
