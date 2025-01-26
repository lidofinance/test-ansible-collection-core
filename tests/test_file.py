testinfra_hosts = ['ansible://lc_file']


def test_file(host):
    inventory = host.ansible.get_variables()
    lc_filename = inventory['lc_filename']
    assert host.file('/tmp/' + lc_filename).content_string == "test file"
