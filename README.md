# Flask Blog

This is a simple blog application built using Flask. The application allows users to create, read, update, and delete blog posts.

## Features

- Create, read, update, and delete blog posts
- Home page displaying all blog posts
- Individual post pages
- Simple and clean design

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/TaylorBeck/flask_blog.git
    cd flask_blog
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```python
    from app import db, create_app

    app = create_app()
    with app.app_context():
        db.create_all()
    ```

5. **Run the application:**

    ```bash
    python run.py
    ```

6. **Open a browser and navigate to `http://localhost:5000` to see the application in action.**

## Usage

- Navigate to the home page to see all blog posts.
- Click on "New Post" to create a new blog post.
- Click on a post title to view the full post.
- Each post can be edited or deleted.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.