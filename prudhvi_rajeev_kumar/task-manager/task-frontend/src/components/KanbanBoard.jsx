import React, { useEffect, useState } from "react";
import {
  DragDropContext,
  Droppable,
  Draggable,
} from "@hello-pangea/dnd";
import { getTasks, updateTask } from "../services/taskService";
import { toast, ToastContainer } from "react-toastify"; // Import toast and ToastContainer
import "react-toastify/dist/ReactToastify.css"; // Import Toastify styles

// 🌈 Header colors
const statusColors = {
  TO_DO: "#A7C7E7",          // Light Blue
  IN_PROGRESS: "#F7E7A1",    // Light Yellow
  REVIEW: "#D7BDE2",         // Light Purple
  COMPLETED: "#7DCEA0",      // Green
};

// 🌈 Column backgrounds
const pastelColumnColors = {
  TO_DO: "bg-[#E6F1FA] dark:bg-[#3E5B74]",
  IN_PROGRESS: "bg-[#F8F4C9] dark:bg-[#A7A442]",
  REVIEW: "bg-[#F2E6FF] dark:bg-[#7D4D85]",
  COMPLETED: "bg-[#D4F2D7] dark:bg-[#5D7F47]",
};

// 🌈 Card backgrounds
const pastelCardColors = {
  TO_DO: "bg-[#CFE2F3] border-[#A7C7E7]",
  IN_PROGRESS: "bg-[#FFF2A8] border-[#F7E7A1]",
  REVIEW: "bg-[#E8D9FF] border-[#D7BDE2]",
  COMPLETED: "bg-[#C8EFD4] border-[#7DCEA0]",
};

const initialColumns = {
  TO_DO: { name: "TO DO", items: [] },
  IN_PROGRESS: { name: "IN PROGRESS", items: [] },
  REVIEW: { name: "REVIEW", items: [] },
  COMPLETED: { name: "COMPLETED", items: [] },
};

const isMoveAllowedFrontend = (role, from, to) => {
  const employeeRules = {
    TO_DO: ["IN_PROGRESS"],
    IN_PROGRESS: ["REVIEW"],
  };

  const managerRules = {
    ...employeeRules,
    REVIEW: ["COMPLETED", "IN_PROGRESS"],
  };

  if (role === "Employee") return employeeRules[from]?.includes(to) || false;
  if (role === "Manager" || role === "Admin")
    return managerRules[from]?.includes(to) || false;

  return false;
};

const KanbanBoard = () => {
  const [columns, setColumns] = useState(initialColumns);
  const role = localStorage.getItem("role");

  const loadTasks = async () => {
    const res = await getTasks();
    const tasks = res.data;

    const newCols = {
      TO_DO: { ...initialColumns.TO_DO, items: [] },
      IN_PROGRESS: { ...initialColumns.IN_PROGRESS, items: [] },
      REVIEW: { ...initialColumns.REVIEW, items: [] },
      COMPLETED: { ...initialColumns.COMPLETED, items: [] },
    };

    tasks.forEach((task) => {
      if (newCols[task.status]) newCols[task.status].items.push(task);
    });

    setColumns(newCols);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const onDragEnd = async (result) => {
    const { source, destination } = result;
    if (!destination) return;

    const from = source.droppableId;
    const to = destination.droppableId;

    if (from === to) {
      const col = columns[from];
      const items = [...col.items];
      const [moved] = items.splice(source.index, 1);
      items.splice(destination.index, 0, moved);

      setColumns({ ...columns, [from]: { ...col, items } });
      return;
    }

    if (!isMoveAllowedFrontend(role, from, to)) {
      toast.error(`You cannot move from ${from} → ${to}`); // Error notification
      return;
    }

    const sourceCol = columns[from];
    const destCol = columns[to];

    const sourceItems = [...sourceCol.items];
    const destItems = [...destCol.items];

    const [moved] = sourceItems.splice(source.index, 1);
    moved.status = to;

    destItems.splice(destination.index, 0, moved);

    setColumns({
      ...columns,
      [from]: { ...sourceCol, items: sourceItems },
      [to]: { ...destCol, items: destItems },
    });

    try {
      await updateTask(moved.task_id, { status: moved.status });
      toast.success(`Task moved to ${to}!`); // Success notification
    } catch (err) {
      toast.error("Backend rejected this move. Reloading."); // Error notification
      loadTasks();
    }
  };

  return (
    <div className="flex gap-6 p-6 w-full">
      <DragDropContext onDragEnd={onDragEnd}>
        {Object.entries(columns).map(([colId, col]) => (
          <div key={colId} className="w-1/4">
            <h2
              className="text-xl font-semibold mb-4 p-4 rounded-lg text-white"
              style={{ backgroundColor: statusColors[colId] }}
            >
              {col.name}
            </h2>

            <Droppable droppableId={colId}>
              {(provided) => (
                <div
                  ref={provided.innerRef}
                  {...provided.droppableProps}
                  className={`${pastelColumnColors[colId]} p-4 rounded-lg min-h-[500px] transition-all duration-300`}
                >
                  {col.items.map((task, index) => (
                    <Draggable
                      key={task.task_id}
                      draggableId={task.task_id.toString()}
                      index={index}
                    >
                      {(provided) => (
                        <div
                          ref={provided.innerRef}
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                          className={`p-4 rounded-lg mb-3 shadow-lg transition-all border ${pastelCardColors[colId]}`}
                        >
                          <span
                            className="text-xs font-semibold inline-block mb-2"
                            style={{ backgroundColor: statusColors[task.status] }}
                          >
                            {task.status}
                          </span>

                          <h3 className="font-bold text-black dark:text-white">
                            {task.title}
                          </h3>

                          {task.description && (
                            <p className="text-gray-700 dark:text-gray-300 text-sm mt-1">
                              {task.description}
                            </p>
                          )}

                          <p className="text-sm mt-2">
                            <span className="text-blue-600 dark:text-blue-400">Priority:</span>{" "}
                            {task.priority}
                          </p>

                          <p className="text-sm">
                            <span className="text-green-600 dark:text-green-400">Assigned To:</span>{" "}
                            {task.assigned_to}
                          </p>
                        </div>
                      )}
                    </Draggable>
                  ))}

                  {provided.placeholder}
                </div>
              )}
            </Droppable>
          </div>
        ))}
      </DragDropContext>

      {/* Toast Container for showing notifications */}
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
    </div>
  );
};

export default KanbanBoard;
