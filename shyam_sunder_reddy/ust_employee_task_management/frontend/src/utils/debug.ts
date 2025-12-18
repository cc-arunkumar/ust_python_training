// Debug utility to test API connectivity
export const testAPIConnection = async () => {
  try {
    const response = await fetch('http://localhost:8000/health');
    const data = await response.json();
    console.log('✅ Backend health check:', data);
    return true;
  } catch (error) {
    console.error('❌ Backend connection failed:', error);
    return false;
  }
};

// Test authentication
export const testAuth = async (token: string) => {
  try {
    const response = await fetch('http://localhost:8000/auth/me', {
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });
    const data = await response.json();
    console.log('✅ Auth test:', data);
    return data;
  } catch (error) {
    console.error('❌ Auth test failed:', error);
    return null;
  }
};


