.. image:: https://img.shields.io/github/workflow/status/andersy005/prepapermill/CI?logo=github&style=for-the-badge
    :target: https://github.com/andersy005/prepapermill/actions
    :alt: GitHub Workflow CI Status

.. image:: https://img.shields.io/github/workflow/status/andersy005/prepapermill/code-style?label=Code%20Style&style=for-the-badge
    :target: https://github.com/andersy005/prepapermill/actions
    :alt: GitHub Workflow Code Style Status

.. If you want the following badges to be visible, please remove this line, and unindent the lines below
    .. image:: https://img.shields.io/codecov/c/github/andersy005/prepapermill.svg?style=for-the-badge
        :target: https://codecov.io/gh/andersy005/prepapermill

    .. image:: https://img.shields.io/readthedocs/prepapermill/latest.svg?style=for-the-badge
        :target: https://prepapermill.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

    .. image:: https://img.shields.io/pypi/v/prepapermill.svg?style=for-the-badge
        :target: https://pypi.org/project/prepapermill
        :alt: Python Package Index

    .. image:: https://img.shields.io/conda/vn/conda-forge/prepapermill.svg?style=for-the-badge
        :target: https://anaconda.org/conda-forge/prepapermill
        :alt: Conda Version


prepapermill
============

pre-commit hooks for papermill (https://github.com/nteract/papermill)


Usage
-----

.. code-block:: bash

    $ prepapermill --help
    Usage: prepapermill [OPTIONS] [FILENAMES]...

    Options:
    --kernel-name TEXT     Name of kernel to run
    --parameter-file TEXT  [default: prepapermill.yaml]
    --help                 Show this message and exit.


Example
-------

.. code-block:: bash

    $ prepapermill --parameter-file prepapermill.yaml notebooks/example.ipynb
    Executing: 100%|██████████████████████████████| 4/4 [00:02<00:00,  1.92cell/s]
    Executing: 100%|██████████████████████████████| 4/4 [00:02<00:00,  1.97cell/s]
    $ tree -L 3 notebooks/                                      (sandbox) 11:23:46
    notebooks/
    ├── example.ipynb
    └── output
        ├── example_alpha_1000_ratio_400.ipynb
        └── example_alpha_1_ratio_2.ipynb

    1 directory, 3 files


Development
------------

For a development install, do the following in the repository directory:

.. code-block:: bash

    conda env update -f ci/environment.yml
    conda activate prepapermill-dev
    python -m pip install -e .

Also, please install `pre-commit` hooks from the root directory of the created project by running::

      python -m pip install pre-commit
      pre-commit install

These code style pre-commit hooks (black, isort, flake8, ...) will run every time you are about to commit code.
