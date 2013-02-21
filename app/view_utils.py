"""Module for storing utility functions and classes."""

import jinja2
import os


ROOT_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(ROOT_DIR, 'templates')

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


def render(template_file, content):
    """Renders content to a template.

    Args:
        template_file: string template file name.
        content: dictionary containing context attributes

    Returns:
        string rendered template
    """
    template = jinja_environment.get_template(template_file)
    return template.render(content)
