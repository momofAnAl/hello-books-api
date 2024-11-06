def test_get_all_authors_with_no_records(client):
    # Act
    response = client.get("/authors")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_author(client, two_saved_authors):
    # Act
    response = client.get("/authors/1")  # GET request to /authors/1
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "J.K. Rowling"
    }


def test_get_one_author_with_no_record(client):
    # Act
    response = client.get("/authors/1")  # GET request to a non-existent author
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Author not found"}


def test_create_one_author_in_empty_database(client):
    # Act
    response = client.post("/authors", json={
        "name": "George Orwell"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "George Orwell"
    }


def test_create_one_author_already_in_database(client, two_saved_authors):
    # Act
    response = client.post("/authors", json={
        "name": "Agatha Christie"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "name": "Agatha Christie"
    }