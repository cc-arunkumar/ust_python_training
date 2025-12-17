import React, { useEffect, useState } from "react";
import {
  DragDropContext,
  Droppable,
  Draggable,
} from "@hello-pangea/dnd";
import { getTasks, updateTask } from "../services/taskService";

const initialColumns = {
  Pending: {
    name: "Pending",
    items: [],
  },
  "In Progress": {
    name: "In Progress",
    items: [],
  },
  Completed: {
    name: "Completed",
    items: [],
  },
};

const KanbanBoard = () => {
  const [columns, setColumns] = useState(initialColumns);

  const loadTasks = async () => {
    const res = await getTasks();
    const tasks = res.data;

    const newColumns = {
      Pending: { ...initialColumns.Pending, items: [] },
      "In Progress": { ...initialColumns["In Progress"], items: [] },
      Completed: { ...initialColumns.Completed, items: [] },
    };

    tasks.forEach((task) => {
      if (newColumns[task.status]) {
        newColumns[task.status].items.push(task);
      }
    });

    setColumns(newColumns);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const onDragEnd = async (result) => {
    const { source, destination } = result;
    if (!destination) return;

    const sourceColId = source.droppableId;
    const destColId = destination.droppableId;

    // Same column: reorder only
    if (sourceColId === destColId) {
      const column = columns[sourceColId];
      const copiedItems = [...column.items];
      const [removed] = copiedItems.splice(source.index, 1);
      copiedItems.splice(destination.index, 0, removed);

      setColumns({
        ...columns,
        [sourceColId]: {
          ...column,
          items: copiedItems,
        },
      });
      return;
    }

    // Different columns: move + update status
    const sourceColumn = columns[sourceColId];
    const destColumn = columns[destColId];

    const sourceItems = [...sourceColumn.items];
    const destItems = [...destColumn.items];

    const [removed] = sourceItems.splice(source.index, 1);
    removed.status = destColId;

    destItems.splice(destination.index, 0, removed);

    setColumns({
      ...columns,
      [sourceColId]: {
        ...sourceColumn,
        items: sourceItems,
      },
      [destColId]: {
        ...destColumn,
        items: destItems,
      },
    });

    // Persist change to backend
    try {
      await updateTask(removed.task_id, { status: removed.status });
    } catch (err) {
      console.error("Failed to update status", err);
      // Optionally: reload to sync again
      loadTasks();
    }
  };

  return (
    <div className="flex gap-6 p-4 w-full">
      <DragDropContext onDragEnd={onDragEnd}>
        {Object.entries(columns).map(([columnId, column]) => (
          <div key={columnId} className="w-1/3">
            <h2 className="text-xl font-bold text-blue-400 mb-4">
              {column.name}
            </h2>

            <Droppable droppableId={columnId}>
              {(provided) => (
                <div
                  ref={provided.innerRef}
                  {...provided.droppableProps}
                  className="bg-gray-800 p-4 rounded-lg min-h-[500px]"
                >
                  {column.items.map((task, index) => (
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
                          className="bg-gray-700 p-4 rounded-lg mb-3 shadow hover:bg-gray-600 transition"
                        >
                          <h3 className="font-bold text-white">
                            {task.title}
                          </h3>
                          {task.description && (
                            <p className="text-gray-300 text-sm mt-1">
                              {task.description}
                            </p>
                          )}
                          <p className="text-sm mt-2">
                            <span className="text-blue-400">Priority:</span>{" "}
                            {task.priority}
                          </p>
                          <p className="text-sm">
                            <span className="text-green-400">
                              Assigned To:
                            </span>{" "}
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
