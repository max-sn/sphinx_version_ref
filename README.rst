sphinx_version_ref
==================

This extension adds a single role to `Sphinx <www.sphinx-doc.org>`_. With 
``:version-ref:`<ref>``` one can substitute the version given in ``conf.py``
into ``<ref>``.

Usage
-----

In your ``conf.py`` file::

  version = 'v0.1'
  extensions = ['sphinx_version_ref']

Where version can of course be any string. The following uses of ``<ref>``
then will be parsed as:

.. list-table::
  :header-rows: 1

  * - Entered as ``<ref>``
    - Parsed as
  * - ``https://docs.com/{version}/index.html`` 
    - ```https://docs.com/v0.1/index.html`_``
  * - ``{version} <http://github.com/user/project/tree/{version}>``
    - ```v0.1 <http://github.com/user/project/tree/v0.1>`_``

See `the docs <http://sphinx-version-ref.readthedocs.io>`_ for more
information.