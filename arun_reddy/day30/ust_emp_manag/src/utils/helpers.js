export const getAuthHeader = () => {
  const token = sessionStorage.getItem("access_token");
  return token ? { Authorization: `Bearer ${token}` } : {};
};

export const parseJWT = (token) => {
  try {
    const tokenParts = token.split(".");
    if (tokenParts.length >= 2) {
      return JSON.parse(atob(tokenParts[1]));
    }
  } catch (e) {
    console.error("Error parsing JWT:", e);
  }
  return null;
};

export const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString();
};

export const getNextStatus = (currentStatus) => {
  const statusFlow = ["to-do", "in-progress", "review", "completed"];
  const currentIndex = statusFlow.indexOf(currentStatus);
  return statusFlow[currentIndex + 1] || null;
};
