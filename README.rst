sphinx_version_ref
==================

.. image:: https://img.shields.io/pypi/v/sphinx-version-ref
  :target: https://pypi.org/project/sphinx-version-ref/
  :alt: PyPi version

.. image:: https://img.shields.io/pypi/dm/sphinx-version-ref
  :target: https://pypi.org/project/sphinx-version-ref/
  :alt: PyPi downloads per month

.. image:: https://img.shields.io/readthedocs/sphinx-version-ref/latest
  :target: https://sphinx-version-ref.readthedocs.io/en/latest/
  :alt: Documentation Status

This extension adds a single role to `Sphinx <http://www.sphinx-doc.org/>`_.
With ``:version-ref:`<ref>``` one can substitute the version given in
``conf.py`` into ``<ref>``.

Usage
-----

In your ``conf.py`` file::

  release = '1.4.1a5'
  version = '.'.join(release.split('.')[:2])
  extensions = ['sphinx_version_ref']

Where version can of course be any string. The following uses of ``<ref>``
then will be parsed as:

.. list-table::
  :header-rows: 1

  * - Entered as ``<ref>``
    - Parsed as
  * - ``https://docs.com/{version}/index.html`` 
    - ```https://docs.com/1.4/index.html`_``
  * - ``{version} <http://github.com/user/project/tree/{version}>``
    - ```1.4 <http://github.com/user/project/tree/1.4>`_``
  * - ``See version {version} <http://github.com/user/project/tree/{release}>``
    - ```See version 1.4 <http://github.com/user/project/tree/1.4.1a5>`_``

See `the docs <http://sphinx-version-ref.readthedocs.io>`_ for more
information.
