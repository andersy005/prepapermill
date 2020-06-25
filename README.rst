.. image:: https://img.shields.io/github/workflow/status/andersy005/prepapermill/CI?logo=github&style=for-the-badge
    :target: https://github.com/andersy005/prepapermill/actions
    :alt: GitHub Workflow CI Status

.. image:: https://img.shields.io/github/workflow/status/andersy005/prepapermill/code-style?label=Code%20Style&style=for-the-badge
    :target: https://github.com/andersy005/prepapermill/actions
    :alt: GitHub Workflow Code Style Status

.. image:: https://img.shields.io/codecov/c/github/andersy005/prepapermill.svg?style=for-the-badge
    :target: https://codecov.io/gh/andersy005/prepapermill

.. If you want the following badges to be visible, please remove this line, and unindent the lines below
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
