# Deploying AI CashOrbit to Vercel

This guide provides step-by-step instructions for deploying the AI CashOrbit Django application to Vercel.

## Prerequisites

- A Vercel account (sign up at [vercel.com](https://vercel.com))
- Git repository with your AI CashOrbit project
- PostgreSQL database (Vercel doesn't provide PostgreSQL, so you'll need an external provider)

## Setup Steps

### 1. Database Setup

Set up a PostgreSQL database using one of these services:
- [Supabase](https://supabase.com) (Recommended)
- [Neon](https://neon.tech)
- [Railway](https://railway.app)
- [ElephantSQL](https://www.elephantsql.com)

After creating your database, note the connection details (URL or individual credentials).

### 2. Deploy to Vercel

1. Push your code to a Git repository (GitHub, GitLab, or Bitbucket)
2. Log in to your Vercel account
3. Click "Add New" → "Project"
4. Import your Git repository
5. Configure the project:
   - Framework Preset: Other
   - Build Command: `sh build_files.sh`
   - Output Directory: `staticfiles`
   - Install Command: `pip install -r requirements.txt`

### 3. Environment Variables

Add these environment variables in the Vercel project settings:

- `DATABASE_URL`: Your PostgreSQL connection URL
- `SECRET_KEY`: A secure random string for Django
- `DEBUG`: Set to `False` for production

### 4. Deploy

Click "Deploy" and wait for the build to complete.

## Troubleshooting

### Static Files

If static files aren't loading properly:
1. Ensure `STATIC_ROOT` is set to `staticfiles` in settings.py
2. Verify that WhiteNoise is properly configured
3. Check that the build script is collecting static files

### Database Migrations

If you need to run migrations manually:
1. Install Vercel CLI: `npm i -g vercel`
2. Login: `vercel login`
3. Run command: `vercel run python manage.py migrate`

### Function Size Limits

If you encounter function size limits, try:
1. Reducing dependencies in requirements.txt
2. Increasing the maxLambdaSize in vercel.json (up to 50MB)

## Important Notes

- Vercel has a 50MB limit for serverless functions
- The free tier has limitations on build minutes and function execution
- For production use, consider upgrading to a paid plan

## Maintenance

After deployment, any push to your main branch will trigger automatic redeployment on Vercel.