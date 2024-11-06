def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1") #get request to /books/1
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "To Kill a Mockingbird",
        "description": "A novel by Harper Lee published in 1960."
    }

def test_create_one_cat_in_empty_database(client):
    response = client.post("/books", json={
        "title": "The Art of Computer Programming",
        "description": "A comprehensive book series on algorithms and data structures by Donald Knuth."
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "The Art of Computer Programming",
        "description": "A comprehensive book series on algorithms and data structures by Donald Knuth."
    }
    
def test_create_one_book_already_in_database(client, two_saved_books):  
    response = client.post("/books", json={
        "title": "The Art of Computer Programming",
        "description": "A comprehensive book series on algorithms and data structures by Donald Knuth."
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "The Art of Computer Programming",
        "description": "A comprehensive book series on algorithms and data structures by Donald Knuth."
    }

 