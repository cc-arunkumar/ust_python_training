# Debugging Guide - Backend Data Not Showing in Frontend

This guide will help you troubleshoot why backend data is not appearing in the frontend.

## Quick Checks

### 1. Verify Backend is Running
```bash
# Check if backend is running
curl http://localhost:8000/health
# Should return: {"status":"ok"}
```

### 2. Verify Frontend is Running
- Open browser to `http://localhost:5173`
- Check browser console (F12) for errors

### 3. Check Browser Console
Open browser DevTools (F12) and check:
- **Console tab**: Look for error messages
- **Network tab**: Check if API calls are being made and their status

## Common Issues and Solutions

### Issue 1: CORS Errors
**Symptoms:** Browser console shows CORS errors

**Solution:**
1. Check backend CORS configuration in `backend/main.py`
2. Verify your frontend URL is in the origins list
3. Restart backend after changing CORS settings

**Test:**
```bash
# Test CORS from browser console
fetch('http://localhost:8000/health')
  .then(r => r.json())
  .then(console.log)
  .catch(console.error)
```

### Issue 2: 401 Unauthorized Errors
**Symptoms:** API calls return 401 status

**Solution:**
1. Check if token is stored: `localStorage.getItem('token')` in browser console
2. Verify token hasn't expired (30 minutes)
3. Try logging in again
4. Check backend logs for authentication errors

**Test:**
```javascript
// In browser console
const token = localStorage.getItem('token');
fetch('http://localhost:8000/auth/me', {
  headers: { 'Authorization': `Bearer ${token}` }
})
  .then(r => r.json())
  .then(console.log)
  .catch(console.error)
```

### Issue 3: 404 Not Found
**Symptoms:** API calls return 404

**Possible Causes:**
- Backend endpoint doesn't exist
- Wrong URL path
- Backend router not included

**Solution:**
1. Check backend API docs: `http://localhost:8000/docs`
2. Verify endpoint paths match exactly
3. Check backend logs for routing errors

### Issue 4: Empty Data / No Results
**Symptoms:** Page loads but shows "No data found"

**Possible Causes:**
- Database is empty
- User doesn't have correct role
- Backend returns 404 for empty results

**Solution:**
1. Check database has data
2. Verify user role in database matches what's needed
3. Check backend logs for query results
4. Test API directly: `http://localhost:8000/docs`

### Issue 5: Network Errors
**Symptoms:** "Network Error" or "Failed to fetch"

**Possible Causes:**
- Backend not running
- Wrong backend URL
- Firewall blocking connection

**Solution:**
1. Verify backend is running: `curl http://localhost:8000/health`
2. Check backend URL in `frontend/src/services/api.ts`
3. Check firewall/antivirus settings

## Step-by-Step Debugging

### Step 1: Test Backend Health
```bash
curl http://localhost:8000/health
```

### Step 2: Test Login
1. Open browser console
2. Try logging in
3. Check console for:
   - Request being sent
   - Response received
   - Token stored

### Step 3: Test API Call
In browser console after login:
```javascript
// Get token
const token = localStorage.getItem('token');

// Test API call
fetch('http://localhost:8000/Task/getall?role=Admin', {
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  }
})
  .then(r => {
    console.log('Status:', r.status);
    return r.json();
  })
  .then(data => {
    console.log('Data:', data);
  })
  .catch(err => {
    console.error('Error:', err);
  });
```

### Step 4: Check Backend Logs
Look at backend console for:
- Incoming requests
- Errors or exceptions
- Database query results

### Step 5: Check Frontend Logs
Look at browser console for:
- API request logs (with 📤 emoji)
- API response logs (with ✅ or ❌ emoji)
- Error messages

## Debugging Tools Added

### 1. Connection Test Component
- Shows connection status in bottom-right corner
- Auto-checks every 5 seconds
- Only visible if backend is unreachable

### 2. Enhanced Logging
- All API requests logged with 📤
- All API responses logged with ✅ or ❌
- Detailed error information in console

### Step 6: Enable Verbose Logging

The frontend now logs:
- All API requests (method, URL, params, data)
- All API responses (status, data)
- All errors (status, message, response data)

Check browser console for these logs.

## Testing Checklist

- [ ] Backend server starts without errors
- [ ] Backend health endpoint responds: `curl http://localhost:8000/health`
- [ ] Frontend loads without console errors
- [ ] Connection test shows "connected" (or disappears)
- [ ] Can login successfully
- [ ] Token is stored in localStorage
- [ ] API calls appear in Network tab
- [ ] API calls return 200 status (not 401, 404, 500)
- [ ] Data appears in browser console logs
- [ ] Data appears in UI

## Still Not Working?

1. **Check Backend Logs:**
   - Look for errors in backend console
   - Check database connection
   - Verify routes are registered

2. **Check Frontend Logs:**
   - Open browser DevTools
   - Check Console tab for errors
   - Check Network tab for failed requests

3. **Test API Directly:**
   - Use `http://localhost:8000/docs` (Swagger UI)
   - Test endpoints manually
   - Verify responses match expected format

4. **Verify Data:**
   - Check database has data
   - Verify user has correct roles
   - Test with different user roles

## Quick Fixes

### Restart Everything
```bash
# Stop backend (Ctrl+C)
# Stop frontend (Ctrl+C)

# Restart backend
cd backend
uvicorn main:app --reload --port 8000

# Restart frontend (new terminal)
cd frontend
npm run dev
```

### Clear Browser Cache
- Clear localStorage: `localStorage.clear()` in console
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Clear browser cache

### Check Ports
- Backend should be on port 8000
- Frontend should be on port 5173 (or check console output)
- Verify no other services using these ports


