def test_index(application, default_settings):
    with application.test_client() as client:
        response = client.get("/{{ cookiecutter.plugin_module }}/")
        assert response.status_code == 200
