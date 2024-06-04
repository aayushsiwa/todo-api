# ToDo API

This is a simple RESTful API for managing ToDo items.

## Features

- Create a new ToDo item
- Read a ToDo item by its ID
- Update a ToDo item
- Delete a ToDo item
- Read all ToDo items

## Technologies Used

- FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- SQLAlchemy: SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- SQLite: SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

## Installation

1. Clone the repository:

```
git clone https://github.com/aayushsiwa/todo-api.git
```

2. Navigate into the project directory:

```
cd todo-api
```

3. Install dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

1. Run the FastAPI server:

```
uvicorn main:app --reload
```

2. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

3. You can now use the API endpoints to perform CRUD operations on ToDo items.

## API Endpoints

- `POST /todo`: Create a new ToDo item.
- `GET /todo/{id}`: Read a ToDo item by its ID.
- `PUT /todo/{id}`: Update a ToDo item by its ID.
- `DELETE /todo/{id}`: Delete a ToDo item by its ID.
- `GET /todo`: Read all ToDo items.

## Schema

The API uses the following data schema for ToDo items:

```json
{
  "id": 1,
  "task": "Do something"
}
```

## Future Enhancements

- **User Authentication and Authorization**: Implement user authentication and authorization to allow users to manage their own ToDo lists securely. This could include features like user registration, login, and access control based on user roles or permissions.

- **Sorting and Filtering**: Add endpoints to sort and filter ToDo items based on different criteria such as creation date, completion status, priority, etc. This would provide users with more flexibility in managing their ToDo lists.

- **Pagination**: Implement pagination for endpoints that return multiple ToDo items to improve performance and user experience, especially when dealing with large datasets.

- **Due Dates and Reminders**: Introduce due dates and reminders for ToDo items to help users track deadlines and stay organized. This could include features like setting due dates, receiving notifications for approaching deadlines, and marking items as completed.

- **Tags and Categories**: Allow users to categorize ToDo items using tags or categories for better organization and easier retrieval. This could facilitate grouping related tasks together and quickly finding specific items.

- **Webhooks and Integrations**: Enable webhook support and integrations with other services to automate workflows and enhance productivity. For example, users could receive notifications or perform actions in external applications based on changes to their ToDo lists.

- **Data Export and Backup**: Provide functionality for users to export their ToDo data in various formats (e.g., CSV, JSON) and perform regular backups to prevent data loss. This would give users peace of mind knowing that their tasks are safely backed up and can be easily transferred to other systems if needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.