import React, { createContext, useContext, useState, useCallback } from "react";

const ToastContext = createContext(null);

export const ToastProvider = ({ children }) => {
  const [toasts, setToasts] = useState([]);

  const show = useCallback((message, type = "info", timeout = 4000) => {
    const id = Date.now() + Math.random();
    setToasts((t) => [...t, { id, message, type }]);
    if (timeout > 0)
      setTimeout(() => setToasts((t) => t.filter((x) => x.id !== id)), timeout);
    return id;
  }, []);

  const remove = useCallback(
    (id) => setToasts((t) => t.filter((x) => x.id !== id)),
    []
  );

  return (
    <ToastContext.Provider value={{ show, remove }}>
      {children}
      <div
        aria-live="polite"
        className="fixed right-4 bottom-4 z-50 flex flex-col gap-3"
      >
        {toasts.map((t) => (
          <div
            key={t.id}
            className={`px-4 py-2 rounded shadow-md text-white ${
              t.type === "error"
                ? "bg-red-600"
                : t.type === "success"
                ? "bg-green-600"
                : "bg-gray-800"
            }`}
          >
            {t.message}
          </div>
        ))}
      </div>
    </ToastContext.Provider>
  );
};

export const useToast = () => {
  const ctx = useContext(ToastContext);
  if (!ctx) throw new Error("useToast must be used within ToastProvider");
  return ctx;
};

export default ToastContext;
