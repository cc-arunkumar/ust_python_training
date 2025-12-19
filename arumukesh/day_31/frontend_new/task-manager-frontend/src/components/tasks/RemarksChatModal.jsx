import React, { useEffect, useState, useRef } from "react";
import Modal from "../common/Modal";
import { remarksApi } from "../../services/remarksApi";
import { useAuth } from "../../context/AuthContext";
import Button from "../common/Button";
import Input from "../common/Input";
import { toast } from "react-toastify";

const RemarksChatModal = ({ taskId, isOpen, onClose }) => {
  const { user } = useAuth();
  const [messages, setMessages] = useState([]);
  const [text, setText] = useState("");
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [sending, setSending] = useState(false);
  const bottomRef = useRef(null);
  const fileInputRef = useRef(null);

  const fetchMessages = async () => {
    try {
      const data = await remarksApi.getRemarks(taskId);
      setMessages(Array.isArray(data) ? data : []);
      return Array.isArray(data) ? data : [];
    } catch (err) {
      console.error("Failed to load remarks", err);
      return null;
    }
  };

  useEffect(() => {
    if (isOpen) fetchMessages();
  }, [isOpen]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const tryFindServerSaved = (serverMessages, msgText) => {
    if (!Array.isArray(serverMessages)) return null;
    return serverMessages.find((sm) => {
      try {
        return (
          String(sm.from_emp_id) === String(user.emp_id) &&
          String(sm.message) === String(msgText) &&
          Math.abs(new Date(sm.timestamp).getTime() - Date.now()) < 60000
        );
      } catch (e) {
        return false;
      }
    });
  };

  const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB per file

  const handleSend = async () => {
    const msg = text.trim();
    // allow messages with files only
    if (!msg && selectedFiles.length === 0) return;

    // validate file sizes
    for (const f of selectedFiles) {
      if (f.size > MAX_FILE_SIZE) {
        toast.error(`${f.name} exceeds 5MB limit`);
        return;
      }
    }

    const tmpId = `tmp-${Date.now()}`;
    const optimistic = {
      id: tmpId,
      task_id: taskId,
      message: msg,
      from_emp_id: user.emp_id,
      timestamp: new Date().toISOString(),
      pending: true,
      // keep file objects for retry and previews
      files: selectedFiles.map((f) => ({
        name: f.name,
        size: f.size,
        type: f.type,
        preview: URL.createObjectURL(f),
        fileObj: f,
      })),
    };

    setMessages((prev) => [...prev, optimistic]);
    setText("");
    setSelectedFiles([]);

    try {
      setSending(true);
      await remarksApi.postRemark(
        taskId,
        msg,
        optimistic.files.map((x) => x.fileObj)
      );
      const serverMessages = await fetchMessages();
      if (Array.isArray(serverMessages)) setMessages(serverMessages);
    } catch (err) {
      console.error("Failed to send remark", err);
      // Double-check server in case request actually succeeded on the server side
      const serverMessages = await fetchMessages();
      const found = tryFindServerSaved(serverMessages, msg);
      if (found) {
        setMessages(serverMessages);
        return;
      }

      // mark optimistic message as failed
      setMessages((prev) =>
        prev.map((m) =>
          m.id === tmpId ? { ...m, failed: true, pending: false } : m
        )
      );
    } finally {
      setSending(false);
    }
  };

  const handleRetry = async (optimisticMsg) => {
    const tmpId = optimisticMsg.id;
    // set back to pending
    setMessages((prev) =>
      prev.map((m) =>
        m.id === tmpId ? { ...m, pending: true, failed: false } : m
      )
    );
    try {
      // if optimisticMsg has fileObjs, send them
      const filesToSend = (optimisticMsg.files || [])
        .map((x) => x.fileObj)
        .filter(Boolean);
      await remarksApi.postRemark(
        taskId,
        optimisticMsg.message,
        filesToSend.length ? filesToSend : undefined
      );
      const serverMessages = await fetchMessages();
      if (Array.isArray(serverMessages)) {
        setMessages(serverMessages);
        return;
      }
    } catch (err) {
      console.error("Retry failed", err);
      const serverMessages = await fetchMessages();
      const found = tryFindServerSaved(serverMessages, optimisticMsg.message);
      if (found) {
        setMessages(serverMessages);
        return;
      }
    }

    // still failed
    setMessages((prev) =>
      prev.map((m) =>
        m.id === tmpId ? { ...m, pending: false, failed: true } : m
      )
    );
  };

  if (!isOpen) return null;

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Task Remarks" size="medium">
      <div className="flex flex-col h-96">
        <div className="flex-1 overflow-auto p-3 space-y-3 bg-gray-50 border border-gray-200 flex flex-col hide-scrollbar">
          {messages.length === 0 && (
            <div className="text-sm text-gray-500">
              No remarks yet. Start the conversation.
            </div>
          )}

          {messages.map((m) => {
            const mine = String(m.from_emp_id) === String(user.emp_id);
            return (
              <div
                key={m.id}
                className={`${mine ? "self-end" : "self-start"} w-full`}
              >
                <div
                  className={`p-2 rounded ${
                    mine ? "bg-primary-100" : "bg-white"
                  } max-w-[80%]`}
                >
                  <div className="text-xs text-gray-600">
                    {m.from_emp_id} • {new Date(m.timestamp).toLocaleString()}
                  </div>
                  <div className="mt-1 text-sm text-gray-800">{m.message}</div>

                  {/* attachments: server persisted (m.attachments) or optimistic (m.files) */}
                  {m.attachments && m.attachments.length > 0 && (
                    <div className="mt-2 space-y-1">
                      {m.attachments.map((a, idx) => (
                        <div key={idx}>
                          {a.content_type &&
                          a.content_type.startsWith("image/") ? (
                            <img
                              src={a.url}
                              alt={a.filename}
                              className="max-h-48 rounded"
                            />
                          ) : (
                            <a
                              href={a.url}
                              target="_blank"
                              rel="noreferrer"
                              className="text-sm text-blue-600 underline"
                            >
                              {a.filename}
                            </a>
                          )}
                        </div>
                      ))}
                    </div>
                  )}

                  {m.files && m.files.length > 0 && (
                    <div className="mt-2 space-y-1">
                      {m.files.map((a, idx) => (
                        <div key={idx}>
                          {a.type && a.type.startsWith("image/") ? (
                            <img
                              src={a.preview}
                              alt={a.name}
                              className="max-h-48 rounded"
                            />
                          ) : (
                            <div className="text-sm">{a.name}</div>
                          )}
                        </div>
                      ))}
                    </div>
                  )}

                  <div className="mt-1">
                    {m.pending && (
                      <span className="text-xs text-gray-500 italic">
                        Sending...
                      </span>
                    )}

                    {m.failed && (
                      <span className="text-xs text-red-600">
                        Failed to send.{" "}
                        <button
                          className="underline"
                          onClick={() => handleRetry(m)}
                        >
                          Retry
                        </button>
                      </span>
                    )}
                  </div>
                </div>
              </div>
            );
          })}

          <div ref={bottomRef} />
        </div>

        <div className="mt-3 flex gap-2 items-center">
          <div className="flex-1 relative">
            <Input
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Write a remark..."
              className="h-10 pr-12"
            />

            <input
              type="file"
              multiple
              ref={fileInputRef}
              className="hidden"
              onChange={(e) => setSelectedFiles(Array.from(e.target.files))}
            />

            <button
              type="button"
              aria-label="Attach files"
              className="absolute right-2 top-1/2 -translate-y-1/2 text-gray-500 hover:text-gray-700 relative"
              onClick={() => fileInputRef.current && fileInputRef.current.click()}
            >
              {/* paperclip SVG */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M21.44 11.05l-9.19 9.19a5 5 0 01-7.07-7.07l9.19-9.19a3.5 3.5 0 014.95 4.95L10.5 18.37a2 2 0 01-2.83-2.83l7.07-7.07" />
              </svg>

              {selectedFiles.length > 0 && (
                <span className="absolute -top-1 -right-1 bg-red-600 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">{selectedFiles.length}</span>
              )}
            </button>

            {selectedFiles.length > 0 && (
              <div className="text-xs text-gray-600 mt-1">
                {selectedFiles.map((f) => f.name).join(", ")}
              </div>
            )}
          </div>
          <Button onClick={handleSend} loading={sending} className="h-10" >
            Send
          </Button>
        </div>
      </div>
    </Modal>
  );
};

export default RemarksChatModal;
