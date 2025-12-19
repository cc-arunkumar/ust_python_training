import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";

const TaskModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData,
  defaultAssigned,
}) => {
  const { register, handleSubmit, reset, setValue } = useForm();
  const [selectedFile, setSelectedFile] = useState(null);

  useEffect(() => {
    if (initialData) {
      // Populate form if editing
      setValue("title", initialData.title);
      setValue("remarks", initialData.remarks);
      setValue("priority", initialData.priority);
      setValue("assigned_to", initialData.assigned_to);
      setValue("reviewer", initialData.reviewer || 1); // Default reviewer ID if needed
    } else {
      reset();
      // If a default assigned ID is provided (e.g., manager viewing as employee), prefill it
      if (defaultAssigned) {
        setValue("assigned_to", defaultAssigned);
      }
    }
  }, [initialData, isOpen, reset, setValue]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div className="bg-white p-6 rounded-lg w-full max-w-md">
        <h2 className="text-xl font-bold mb-4">
          {initialData ? "Edit Task" : "Create Task"}
        </h2>

        <form
          onSubmit={handleSubmit((data) =>
            onSubmit({ ...data, file: selectedFile })
          )}
          className="space-y-4"
        >
          <div>
            <label className="block text-sm font-medium">Title</label>
            <input
              {...register("title", { required: true })}
              className="w-full border p-2 rounded"
            />
          </div>

          <div>
            <label className="block text-sm font-medium">
              Assigned To (Emp ID)
            </label>
            <input
              {...register("assigned_to", { required: true })}
              className="w-full border p-2 rounded"
              placeholder="e.g. 101"
            />
          </div>

          <div className="flex gap-4">
            <div className="w-1/2">
              <label className="block text-sm font-medium">Priority</label>
              <select
                {...register("priority")}
                className="w-full border p-2 rounded"
              >
                <option value="medium">Medium</option>
                <option value="high">High</option>
                <option value="low">Low</option>
              </select>
            </div>
            <div className="w-1/2">
              <label className="block text-sm font-medium">Reviewer ID</label>
              <input
                {...register("reviewer")}
                className="w-full border p-2 rounded"
                defaultValue="0"
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium">Remarks</label>
            <textarea
              {...register("remarks")}
              className="w-full border p-2 rounded"
            ></textarea>
          </div>

          <div>
            <label className="block text-sm font-medium">Attach file</label>
            <input
              type="file"
              onChange={(e) => setSelectedFile(e.target.files?.[0] || null)}
              className="w-full mt-1"
            />
          </div>

          <div className="flex justify-end gap-2 mt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-gray-600 bg-gray-200 rounded"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-4 py-2 text-white bg-blue-600 rounded"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default TaskModal;
