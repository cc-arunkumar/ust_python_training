# Frontend-Backend Integration Guide

This guide will help you set up and run the complete UST Employee Task Management system with both frontend and backend working together.

## Prerequisites

- Python 3.8+ (for backend)
- Node.js 18+ and npm/yarn/pnpm (for frontend)
- PostgreSQL database (for backend)
- MongoDB (for remarks storage)

## Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
# Or if using pyproject.toml:
pip install -e .
```

4. Set up environment variables:
Create a `.env` file in the backend directory with:
```
DATABASE_URL=postgresql://user:password@localhost:5432/ust_task_db
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=ust_task_db
SECRET_KEY=UST-TaskTracker-Secret
```

5. Initialize the database:
```bash
# Make sure PostgreSQL is running and database is created
# The application will create tables automatically on first run
```

6. Start the backend server:
```bash
uvicorn main:app --reload --port 8000
```

The backend API will be available at `http://localhost:8000`
API documentation: `http://localhost:8000/docs`

## Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
# or
pnpm install
```

3. Start the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

The frontend will be available at `http://localhost:5173`

## Integration Points

### API Base URL
The frontend is configured to connect to `http://localhost:8000` (backend default port).

To change this, update `frontend/src/services/api.ts`:
```typescript
const API_BASE_URL = 'http://localhost:8000'; // Change this if needed
```

### CORS Configuration
The backend is configured to accept requests from:
- `http://localhost:5173` (Vite default)
- `http://localhost:3000` (React alternative)
- `http://localhost:8080` (Alternative port)

To add more origins, update `backend/main.py`:
```python
origins = [
    "http://localhost:5173",
    # Add your frontend URL here
]
```

### Authentication Flow

1. User logs in with Employee ID and password
2. Backend validates credentials and returns JWT token
3. Frontend stores token in localStorage
4. All subsequent API calls include token in Authorization header
5. Backend validates token on each request
6. On 401 errors, frontend automatically redirects to login

### API Endpoints Mapping

| Frontend Function | Backend Endpoint | Method |
|-----------------|-----------------|--------|
| `authAPI.login()` | `/auth/login` | POST |
| `authAPI.getMe()` | `/auth/me` | GET |
| `taskAPI.getAll()` | `/Task/getall?role={role}` | GET |
| `taskAPI.create()` | `/Task/create?role={role}` | POST |
| `taskAPI.update()` | `/Task/update?t_id={id}&role={role}&...` | PUT |
| `employeeAPI.getAll()` | `/Employee/getall?role={role}` | GET |
| `employeeAPI.create()` | `/Employee/create?role={role}` | POST |
| `userAPI.getAll()` | `/Users/getall?role={role}` | GET |
| `remarkAPI.getByTask()` | `/Remark/getbytask?task_id={id}&role={role}` | GET |
| `remarkAPI.create()` | `/Remark/create` | POST (multipart/form-data) |

## Testing the Integration

1. **Start Backend:**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

2. **Start Frontend:**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Test Login:**
   - Open `http://localhost:5173`
   - Use valid Employee ID and password
   - Should redirect to dashboard on success

4. **Test API Connection:**
   - Check browser console for any errors
   - Verify API calls in Network tab
   - Check backend logs for incoming requests

## Common Issues and Solutions

### CORS Errors
**Problem:** Browser shows CORS errors
**Solution:** 
- Verify backend CORS origins include your frontend URL
- Check backend is running on correct port
- Ensure `allow_credentials=True` in CORS middleware

### 401 Unauthorized Errors
**Problem:** API calls return 401
**Solution:**
- Check token is stored in localStorage
- Verify token hasn't expired (30 minutes default)
- Re-login to get new token
- Check backend token validation logic

### 404 Not Found Errors
**Problem:** API endpoints return 404
**Solution:**
- Verify backend server is running
- Check API base URL in frontend matches backend
- Verify endpoint paths match exactly
- Check backend router includes are correct

### Empty Arrays/No Data
**Problem:** Pages show "No data found"
**Solution:**
- Check database has data
- Verify user has correct role permissions
- Check API responses in Network tab
- Verify role parameter is correct

### Task Update Not Working
**Problem:** Task updates fail
**Solution:**
- Backend expects query parameters, not JSON body
- Verify all required fields are provided
- Check user has correct role (Manager/Developer)
- Verify task ID is correct

## Role-Based Access

The system uses role-based access control:

- **Admin:** Full access to all features
- **Manager:** Can create tasks, manage employees (if permitted)
- **Developer:** Can view and update assigned tasks

Each API call requires a `role` parameter matching one of the user's roles.

## Development Tips

1. **Backend Logging:** Check backend console for request/response logs
2. **Frontend Console:** Check browser console for errors and API responses
3. **Network Tab:** Use browser DevTools Network tab to inspect API calls
4. **API Docs:** Use `/docs` endpoint for interactive API documentation
5. **Token Debugging:** Check localStorage for stored token

## Production Deployment

For production:

1. **Backend:**
   - Set proper CORS origins
   - Use environment variables for secrets
   - Enable HTTPS
   - Set up proper database connection pooling

2. **Frontend:**
   - Build for production: `npm run build`
   - Update API_BASE_URL to production backend
   - Serve static files with proper server configuration
   - Enable HTTPS

## Support

If you encounter issues:
1. Check backend logs
2. Check frontend console
3. Verify database connections
4. Test API endpoints directly via `/docs`
5. Verify environment variables are set correctly


