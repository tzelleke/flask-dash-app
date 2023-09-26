def test_main(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Flask Dash App" in response.data
