import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";
import Avatar from "./Avatar";

export default function TaskBoard({ tasks, onDragEnd }) {
  // Flow order: To Do -> In Progress -> Review -> Done
  const columns = {
    todo: "To Do",
    inprogress: "In Progress",
    review: "Review",
    done: "Done"
  };

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <div className="board">
        {Object.entries(columns).map(([key, label]) => (
          <Droppable droppableId={key} key={key}>
            {(provided, snapshot) => (
              <div
                className={`column ${key} ${snapshot.isDraggingOver ? "drag-over" : ""}`}
                ref={provided.innerRef}
                {...provided.droppableProps}
              >
                <h3>{label}</h3>
                {tasks
                  .filter((t) => t.status === key)
                  .map((t, index) => (
                    <Draggable
                      key={t.taskid}
                      draggableId={String(t.taskid)}
                      index={index}
                    >
                      {(provided) => (
                        <div
                          className="task-card"   // neutral style only
                          ref={provided.innerRef}
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                        >
                          <h4>{t.title}</h4>
                          <p>{t.description}</p>
                          {t.assigned_to_name && (
                            <Avatar name={t.assigned_to_name} />
                          )}
                        </div>
                      )}
                    </Draggable>
                  ))}
                {provided.placeholder}
              </div>
            )}
          </Droppable>
        ))}
      </div>
    </DragDropContext>
  );
}
