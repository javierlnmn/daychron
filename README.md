# Django App Template

This Django template includes:

- JET admin interface
- Python slugify package
- Django Tailwind (_node.js and npm required_)
- Python dotenv package
- Basic templating structure
- Basic account functionality (login and logout)

## Installation

1. Install dependencies:
   ```
   poetry install
   ```
2. Install tailwind dependencies:
   ```
   poetry run python manage.py tailwind install
   ```
3. Migrate:
   ```
   poetry run python manage.py migrate
   ```

## Dotenv

In order to use the `dotenv` package, you will need to create a _.env_ file in the root of your project. You can change the location of the file by modifying this line in the `settings.py` file:

```python
# Load environment variables from .env
load_dotenv(os.path.join(BASE_DIR, '.env'))
```

By default, the project settings gets `DEBUG` and `SECRET_KEY` values from _.env_ file.

## Development Server

To run the development server, just run these two commands in separate terminals:

```
poetry run python manage.py tailwind start
```

and

```
poetry run python manage.py runserver
```

Alternatively, you can use Docker to run the development server:

```
docker-compose -f docker/dev/docker-compose.dev.yaml up
```

### Running in Production

To run the production server we recommend using Docker.
You will need to set up the following environment variables:

- `DEBUG`: Set to `False`
- `SECRET_KEY`: A random secret key
- `ALLOWED_HOSTS`: A comma-separated list of allowed hosts
- `CSRF_TRUSTED_ORIGINS`: A comma-separated list of trusted origins

You can set these variables in the _.env_ file.

Then run the following command to start the production server:

```
docker-compose -f docker-compose.prod.yaml up
```
