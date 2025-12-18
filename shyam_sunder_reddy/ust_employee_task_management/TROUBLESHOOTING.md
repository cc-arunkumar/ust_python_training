# Troubleshooting: Backend Data Not Showing

## Immediate Steps

1. **Open Browser Console (F12)**
   - Check for red error messages
   - Look for API request logs (📤) and response logs (✅/❌)

2. **Check Connection Status**
   - Look for connection test indicator in bottom-right corner
   - Should show "✅ Backend is reachable" or disappear if connected

3. **Verify Backend is Running**
   ```bash
   # In terminal, test backend
   curl http://localhost:8000/health
   # Should return: {"status":"ok"}
   ```

4. **Check Network Tab**
   - Open DevTools → Network tab
   - Look for API calls to `localhost:8000`
   - Check status codes (should be 200, not 401/404/500)

## Common Issues

### "Network Error" or "Failed to fetch"
**Cause:** Backend not running or wrong URL

**Fix:**
1. Start backend: `cd backend && uvicorn main:app --reload --port 8000`
2. Verify URL in `frontend/src/services/api.ts` is `http://localhost:8000`

### CORS Errors in Console
**Cause:** Frontend origin not allowed by backend

**Fix:**
1. Check what port frontend is running on (check terminal output)
2. Add that port to `backend/main.py` origins list
3. Restart backend

### 401 Unauthorized
**Cause:** Token missing, expired, or invalid

**Fix:**
1. Clear localStorage: In browser console, run `localStorage.clear()`
2. Log in again
3. Check token exists: `localStorage.getItem('token')`

### 404 Not Found
**Cause:** Endpoint doesn't exist or wrong path

**Fix:**
1. Check API docs: `http://localhost:8000/docs`
2. Verify endpoint paths match exactly
3. Check backend logs for routing errors

### Empty Data / "No tasks found"
**Cause:** Database empty or user role mismatch

**Fix:**
1. Check database has data
2. Verify user role matches required role
3. Test API directly at `http://localhost:8000/docs`

## Debug Commands

### Test Backend Connection
```bash
curl http://localhost:8000/health
```

### Test Login (in browser console)
```javascript
fetch('http://localhost:8000/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ e_id: YOUR_ID, password: 'YOUR_PASSWORD' })
})
  .then(r => r.json())
  .then(console.log)
  .catch(console.error)
```

### Test API Call (after login)
```javascript
const token = localStorage.getItem('token');
fetch('http://localhost:8000/Task/getall?role=Admin', {
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  }
})
  .then(r => r.json())
  .then(console.log)
  .catch(console.error)
```

## What to Check

1. ✅ Backend running on port 8000
2. ✅ Frontend running (check terminal for port)
3. ✅ No CORS errors in console
4. ✅ Token stored after login
5. ✅ API calls visible in Network tab
6. ✅ API calls return 200 status
7. ✅ Data in response (check Network tab → Response)

## Still Not Working?

1. **Check Backend Logs:** Look at backend console for errors
2. **Check Frontend Logs:** Look at browser console for detailed logs
3. **Test API Directly:** Use `http://localhost:8000/docs` to test endpoints
4. **Verify Data:** Check database has data and user has correct roles


