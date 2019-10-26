========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
        | |codeclimate|
    * - package
      - | |commits-since|




.. end-badges

Utilities Package

Installation
============

::

    pip install csci-utils

You can also install the in-development version with::

    pip install https://github.com/GabrielBG010/2019fa-csci-utils-GabrielBG010-3/archive/master.zip


Documentation
=============


https://2019fa-csci-utils-GabrielBG010-3.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
