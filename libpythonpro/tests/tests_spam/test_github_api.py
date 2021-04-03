from libpythonpro import github_api


def test_buscar_avatar():
    url = github_api.buscar_avatar('GabrielBarcell0s')
    assert '' == url