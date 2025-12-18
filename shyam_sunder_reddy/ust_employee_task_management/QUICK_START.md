# Quick Start Guide

Get the UST Employee Task Management system up and running in minutes!

## Prerequisites Check

- ✅ Python 3.8+ installed
- ✅ Node.js 18+ installed
- ✅ PostgreSQL running
- ✅ MongoDB running (for remarks)

## Step 1: Backend Setup (5 minutes)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy pymongo python-dotenv python-jose passlib bcrypt

# Create .env file with your database credentials
# DATABASE_URL=postgresql://user:password@localhost:5432/ust_task_db
# MONGODB_URL=mongodb://localhost:27017
# MONGODB_DB_NAME=ust_task_db

# Start backend server
uvicorn main:app --reload --port 8000
```

✅ Backend should be running at `http://localhost:8000`
✅ API docs available at `http://localhost:8000/docs`

## Step 2: Frontend Setup (3 minutes)

```bash
# Open a new terminal
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

✅ Frontend should be running at `http://localhost:5173`

## Step 3: Test the Integration

1. Open browser to `http://localhost:5173`
2. You should see the login page
3. Use valid Employee ID and password from your database
4. After login, you should see the dashboard

## Verification Checklist

- [ ] Backend server starts without errors
- [ ] Frontend server starts without errors
- [ ] Login page loads
- [ ] Can login with valid credentials
- [ ] Dashboard loads after login
- [ ] No CORS errors in browser console
- [ ] API calls visible in Network tab

## Common First-Time Issues

### Backend won't start
- Check Python version: `python --version`
- Verify virtual environment is activated
- Check database connection in .env file

### Frontend won't start
- Check Node version: `node --version`
- Delete `node_modules` and run `npm install` again
- Check if port 5173 is already in use

### Can't login
- Verify user exists in database
- Check backend logs for errors
- Verify password matches in database

### CORS errors
- Ensure backend CORS includes `http://localhost:5173`
- Restart backend after changing CORS settings

## Next Steps

1. Create test users via backend API or database
2. Create test employees
3. Create test tasks
4. Explore all features

## Need Help?

- Check `INTEGRATION_GUIDE.md` for detailed documentation
- Review backend logs for errors
- Check browser console for frontend errors
- Use `/docs` endpoint for API testing


