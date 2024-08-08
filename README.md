# Book-Recommender
Here is the detailed documentation for both the backend and frontend APIs, including endpoint descriptions, request/response formats, and usage examples. Additionally, I'll explain how to set up interactive API documentation using tools like Swagger and Postman.

Backend API Documentation
Endpoints
POST /api/recommendations/: Submit a new book recommendation.
GET /api/recommendations/: Fetch all book recommendations.
POST /api/recommendations/{id}/like/: Like a book recommendation.
POST /api/recommendations/{id}/comment/: Add a comment to a book recommendation.
Request/Response Formats
1. POST /api/recommendations/
Description: Submits a new book recommendation.

Request:

Method: POST
Headers:
Content-Type: application/json
X-CSRFToken: {csrf_token}
Body: JSON


{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "description": "A novel set in the Jazz Age on Long Island.",
    "cover_image": "http://example.com/great_gatsby.jpg",
    "genre": "Fiction",
    "rating": 4.5,
    "publication_date": "1925-04-10"
}
Response:

Status: 201 Created
Body: JSON

{
    "status": "success"
}
Error Response:

Status: 400 Bad Request
Body: JSON

{
    "error": "Detailed error message"
}
2. GET /api/recommendations/
Description: Fetches all book recommendations.

Request:

Method: GET
Response:

Status: 200 OK
Body: JSON
json
Copy code
[
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "description": "A novel set in the Jazz Age on Long Island.",
        "cover_image": "http://example.com/great_gatsby.jpg",
        "genre": "Fiction",
        "rating": 4.5,
        "publication_date": "1925-04-10"
    },
    
]
3. POST /api/recommendations/{id}/like/
Description: Likes a book recommendation.

Request:

Method: POST
Headers:
X-CSRFToken: {csrf_token}
Body: None
Response:

Status: 200 OK
Body: JSON

{
    "status": "success"
}
Error Response:

Status: 400 Bad Request
Body: JSON

{
    "error": "Detailed error message"
}
4. POST /api/recommendations/{id}/comment/
Description: Adds a comment to a book recommendation.

Request:

Method: POST
Headers:
Content-Type: application/json
X-CSRFToken: {csrf_token}
Body: JSON

{
    "text": "Great book!"
}
Response:

Status: 200 OK
Body: JSON

{
    "status": "success"
}
Error Response:

Status: 400 Bad Request
Body: JSON

{
    "error": "Detailed error message"
}


Frontend API Documentation


Endpoints
searchBooks(query): Searches for books based on a query.
submitRecommendation(): Submits a new book recommendation.
fetchRecommendations(): Fetches all book recommendations.
likeRecommendation(id): Likes a book recommendation.
addComment(id): Adds a comment to a book recommendation.


1. searchBooks(query)
Description: Searches for books based on a query.

2. submitRecommendation()
Description: Submits a new book recommendation.


3. fetchRecommendations()
Description: Fetches all book recommendations.

                
4. likeRecommendation(id)
Description: Likes a book recommendation.

5. addComment(id)
Description: Adds a comment to a book recommendation.










