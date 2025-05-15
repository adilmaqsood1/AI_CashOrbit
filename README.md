# AI CashOrbit

A Django-based accounting and financial management application.

## Docker Setup

This project is containerized with Docker for easy deployment.

### Local Development

1. Clone the repository
2. Run with Docker Compose:
   ```
   docker-compose up
   ```
3. Access the application at http://localhost:8000

### Production Deployment on Railway

1. Create a Railway account and install the Railway CLI
2. Login to Railway:
   ```
   railway login
   ```
3. Initialize your project:
   ```
   railway init
   ```
4. Add a PostgreSQL database:
   ```
   railway add
   ```
   Select PostgreSQL from the options.

5. Set environment variables in Railway dashboard:
   - `DEBUG`: False
   - `SECRET_KEY`: [your-secret-key]
   - `ALLOWED_HOSTS`: your-app-domain.railway.app,localhost,127.0.0.1
   - `DJANGO_SETTINGS_MODULE`: AI_CashOrbit.settings_production

6. Deploy your application:
   ```
   railway up
   ```

7. Generate a domain:
   ```
   railway domain
   ```

## Environment Variables

The following environment variables can be configured:

- `DEBUG`: Set to 'True' for development, 'False' for production
- `SECRET_KEY`: Django secret key
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DJANGO_SETTINGS_MODULE`: Path to settings module (use AI_CashOrbit.settings_production for production)
- Database settings (automatically provided by Railway):
  - `PGDATABASE`: Database name
  - `PGUSER`: Database user
  - `PGPASSWORD`: Database password
  - `PGHOST`: Database host
  - `PGPORT`: Database port