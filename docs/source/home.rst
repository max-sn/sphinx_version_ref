##################
sphinx_version_ref
##################

:Author: M.J.W. Snippe
:Version: |version|

This extension adds a single role to the |RST| parser of |sphinx|_.

.. rst:role:: version-ref

  :rst:role:`version-ref` takes its argument, replaces all occurences of
  ``{version}`` in it by the string set by the ``version`` configuration
  variable and then processes it as if it were a normal :abbr:`URI (uniform
  resource identifier)`.

  .. rubric:: Example

  .. code-block:: restructuredtext

    Some text in which I would like to reference to this specific version's
    repository :version-ref:`See version {version} here!
    <https://github.com/max-sn/sphinx_version_ref/tree/{release}>`


  Some text in which I would like to reference to this specific version's
  repository :version-ref:`See version {version} here!
  <https://github.com/max-sn/sphinx_version_ref/tree/{release}>`


Usage
-----

In your ``conf.py`` file::

  release = '0.0.1a0'
  version = '.'.join(release.split('.')[:2])
  extensions = ['sphinx_version_ref']

Where version can of course be any string. The following uses of ``<ref>``
then will be parsed as:

.. list-table::
  :header-rows: 1

  * - Entered as ``<ref>``
    - Parsed as
    - Resulting in
  * - ``https://docs.com/{version}/index.html`` 
    - ```https://docs.com/0.0/index.html`_``
    - :version-ref:`https://docs.com/{version}/index.html`
  * - ``Repo version {version} <http://github.com/user/project/tree/{release}>``
    - ```Repo version 0.0 <http://github.com/user/project/tree/0.0.1a0>`_``
    - :version-ref:`Repo version {version} <http://github.com/user/project/tree/{release}>`

.. |RST| replace:: reStructuredText
.. |sphinx| replace:: Sphinx
.. _sphinx: http://www.sphinx-doc.org
