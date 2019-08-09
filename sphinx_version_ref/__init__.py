from pkg_resources import get_distribution, DistributionNotFound

from docutils import nodes

from sphinx.util.nodes import split_explicit_title, set_role_source_info

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # Package is not installed
    __version__ = 'unknown'


def version_ref_role(name, rawtext, text, lineno, inliner, options={},
                     content=[]):
    """
    Parses its contents to replace every occurrence of ``{version}`` and
    replaces it by the string set by ``version`` in ``conf.py``.
    """
    version = inliner.document.settings.env.config.version
    release = inliner.document.settings.env.config.release
    text = text.format(version=version, release=release)
    has_explicit_title, title, target = split_explicit_title(text)
    if target.startswith('#'):
        target = target.replace(version, version.replace('.', '-'))
    if has_explicit_title:
        ref_node = nodes.reference('', '')
        ref_node['refuri'] = target
        ref_node.append(nodes.paragraph(title, title))
    else:
        ref_node = nodes.reference(target, target)
        ref_node['refuri'] = target
    set_role_source_info(inliner, lineno, ref_node)
    return [ref_node], []

version_ref_role.options = {'class': None}
version_ref_role.content = False


def setup(app):

    app.add_role('version-ref', version_ref_role)

    return {'version': '0.0',
            'parallel_read_safe': True,
            'parallel_write_safe': True}
