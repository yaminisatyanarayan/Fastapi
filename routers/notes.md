What is FastAPI?

FastAPI is a modern Python web framework used to build high-performance APIs. It supports asynchronous programming, automatic data validation using Pydantic, and provides built-in interactive API documentation.

FastAPI vs Flask?

FastAPI supports asynchronous programming and is faster compared to Flask, which is mostly synchronous. FastAPI also provides automatic validation and documentation, while Flask requires additional libraries for these features.

What is Pydantic?

Pydantic is used in FastAPI for data validation and parsing. It ensures that the data received in the request body follows the correct data types and structure.

Combine everything:  FastAPI is a modern Python framework used to build high-performance APIs. It supports asynchronous programming, uses Pydantic for data validation, and provides automatic API documentation, making development faster and efficient.

What is Dependency Injection?

Dependency Injection in FastAPI is a way to reuse common logic like database connections or authentication using the Depends() function. It helps avoid code duplication and makes the application more modular and maintainable.

What is Middleware?

Middleware is a function that runs before and after every request. It is used for tasks like logging, authentication, and modifying requests or responses.

What is CORS? 

CORS (Cross-Origin Resource Sharing) allows the frontend and backend running on different domains or ports to communicate with each other.


Practice this:

I used dependency injection in FastAPI to manage reusable components like database connections. Middleware helped me log request and response flow, and I used CORS to enable communication between my React frontend and FastAPI backend running on different ports.


How did you connect FastAPI with database?

I connected FastAPI with the database using SQLAlchemy. I created a database engine and session using sessionmaker, and used dependency injection to manage database sessions in API routes.

What is ORM?

ORM (Object Relational Mapping) is a technique that allows us to interact with the database using Python objects instead of writing raw SQL queries.

Difference between add() and commit()

add() is used to add data to the session, while commit() is used to save the changes permanently to the database.

Practice this:

I used SQLAlchemy ORM to connect FastAPI with the database. I created an engine and session, and managed database connections using dependency injection. ORM helps me work with Python objects instead of SQL queries, and I use add() to stage data and commit() to persist it in the database.

What is JWT and how does it work?

JWT (JSON Web Token) is a secure token used for authentication. When a user logs in, the server verifies the credentials and generates a token. This token is then sent by the client in every request, and the server validates it to allow access to protected APIs.

🔁 FLOW (VERY IMPORTANT)

👉 Explain like this:

User logs in
Server verifies credentials
Server creates JWT token
Client stores token
Client sends token in header (Authorization: Bearer token)
Server verifies token → allows access

How did you implement authentication?

👉 Say:

I implemented JWT-based authentication in FastAPI. I created a login API where users provide credentials, and if valid, a JWT token is generated. I used password hashing for security and protected routes using dependency injection to verify the token.

What is password hashing and why is it important?

👉 Say:

Password hashing is the process of converting a plain password into a secure encrypted format. It is important because passwords should never be stored in plain text, which improves security and protects user data.

Practice this:

I implemented JWT-based authentication where users log in to receive a token. The token is sent in the Authorization header for protected routes. I used password hashing with bcrypt to securely store passwords and dependency injection to validate tokens in FastAPI.

When should you use async in FastAPI?

Async is used when handling I/O-bound operations like database calls, API requests, or file operations. It allows multiple requests to be processed efficiently without blocking the server.

How do you structure a FastAPI project?

I follow a modular structure where database connection is handled in a separate file, models define database tables, schemas handle validation, CRUD contains business logic, and routers define API endpoints. This improves scalability and maintainability.
app/
 ├── main.py
 ├── database.py
 ├── models.py
 ├── schemas.py
 ├── crud.py
 ├── routers/
 ├── auth.py


 How do you handle errors in FastAPI?

 I handle errors using HTTPException in FastAPI. It allows me to return proper status codes and error messages when something goes wrong, such as invalid input or authentication failure.

 raise HTTPException(status_code=404, detail="User not found")


 Explain your project (THIS DECIDES SELECTION)

I built a User Management API using FastAPI where I implemented CRUD operations with SQLAlchemy ORM. I structured the project into modules like models, schemas, CRUD, and routers for better maintainability.

I also implemented JWT-based authentication where users can register and log in to receive a token. I used password hashing with bcrypt for security and protected routes using dependency injection.

Additionally, I used middleware for logging requests and enabled CORS to connect the FastAPI backend with a React frontend.