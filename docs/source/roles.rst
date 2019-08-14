#####
Roles
#####

.. rst:role:: version-ref

  :rst:role:`version-ref` takes its argument, replaces all occurrences of
  ``{version}`` in it by the string set by the ``version`` configuration
  variable and similarly for all occurrences of ``{release}``. Then it will
  proces its argument as if it were a normal :abbr:`URI (uniform resource
  identifier)`.

  .. rubric:: Example

  .. code-block:: restructuredtext

    Some text in which I would like to reference to this specific version's
    repository :version-ref:`See version {version} here!
    <https://github.com/max-sn/sphinx_version_ref/tree/{release}>`


  Some text in which I would like to reference to this specific version's
  repository :version-ref:`See version {version} here!
  <https://github.com/max-sn/sphinx_version_ref/tree/{release}>`

