import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('file, content', [
  ("/home/test_yes/.bashrc", "force_color_prompt=yes")
  ("/home/test_no/.bashrc", "#force_color_prompt=yes")
])

def test_files(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
