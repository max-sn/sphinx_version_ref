#####
Usage
#####

In your ``conf.py`` file::

  release = '0.2.0-a'
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
    - ```Repo version 0.0 <http://github.com/user/project/tree/0.1.0a0>`_``
    - :version-ref:`Repo version {version} <http://github.com/user/project/tree/{release}>`
