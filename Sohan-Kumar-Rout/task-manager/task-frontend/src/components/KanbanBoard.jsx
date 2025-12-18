import React, { useEffect, useState } from "react";
import {
  DragDropContext,
  Droppable,
  Draggable,
} from "@hello-pangea/dnd";
import { getTasks, updateTask } from "../services/taskService";
import { toast } from "react-toastify";

// 🌈 Header colors
const statusColors = {
  TO_DO: "#A7C7E7",          
  IN_PROGRESS: "#F7E7A1",    // Light Yellow
  REVIEW: "#D7BDE2",         // Light Purple
  COMPLETED: "#7DCEA0",      // Green
};

// 🌈 Column backgrounds
const pastelColumnColors = {
  TO_DO: "bg-[#DCEBFA] dark:bg-[#4A637A]",
  IN_PROGRESS: "bg-[#FFF8CC] dark:bg-[#7A6F2A]",
  REVIEW: "bg-[#F2E6FF] dark:bg-[#5A3A7A]",
  COMPLETED: "bg-[#DFF5E1] dark:bg-[#2F6B3F]",
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
    try {
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
    } catch (err) {
      toast.error("Failed to load tasks!");
    }
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
      toast.error(`You cannot move from ${from} → ${to}`);
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
      toast.success(`Task moved to ${to}!`);
    } catch (err) {
      toast.error("Backend rejected this move. Reloading.");
      loadTasks();
    }
  };

  return (
    <div className="flex gap-6 p-4 w-full">
      <DragDropContext onDragEnd={onDragEnd}>
        {Object.entries(columns).map(([colId, col]) => (
          <div key={colId} className="w-1/4">
            <h2
              className="text-xl font-bold mb-4 p-2 rounded text-white"
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
                          className={`
                            p-4 rounded-lg mb-3 shadow transition border
                            ${pastelCardColors[colId]}
                            dark:bg-gray-700 dark:border-gray-600
                          `}
                        >
                          <span
                            className="text-white px-2 py-1 rounded text-xs font-semibold inline-block mb-2"
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
    </div>
  );
};

export default KanbanBoard;
