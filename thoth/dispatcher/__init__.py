"""Selinon dispatcher files manipulation."""

import os
import typing


def get_dispatcher_config() -> typing.Tuple[str, typing.List[str]]:
    """Return all dispatcher configuration files."""
    dir_path = os.path.dirname(os.path.realpath(__file__))

    flows = []
    flows_path = os.path.join(dir_path, 'flows')
    for file_name in os.listdir(flows_path):
        if file_name.endswith(('.yaml', '.yml')):
            flows.append(os.path.join(flows_path, file_name))

    return os.path.join(dir_path, 'nodes.yaml'), flows
