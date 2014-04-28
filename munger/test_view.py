def test_munging(client):
    response = client.post('/', {'content': '1234'})
    assert response.context['munged'] == '1324'
