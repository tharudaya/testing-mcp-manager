import { useEffect, useState } from "react";
import DeleteTask from "../api/deletetask";
import getList, { type Task } from "../api/getlist";

type Props = {
  isCreated: boolean
}

function TaskList(props: Props) {
  const { isCreated } = props;
  const [tasks, setTasks] = useState<Task[]>([]);
  const [isDeleted, setIsDeleted] = useState(false)

  useEffect(() => {
    getList()
      .then((data) => setTasks(data))
      .catch((error) => console.error(error))
  }, [isCreated, isDeleted])

  const handleDelete = (id: number) => {
    DeleteTask(id)
      .then(() => setIsDeleted(true))
      .catch((error) => console.error(error))
    setTimeout(() => {
      setIsDeleted(false)
    }, 500)
  }

  return (
    <div>
      <h2 className="text-2xl mb-2">Task list:</h2>
      <ul className="list-disc pl-5">
        {
          tasks.map((task) => (
            <div key={task.id} className="flex gap-2 items-center mb-2">
              <li className="flex-auto">{task.text}</li>
              {/* <button className="px-2 py-1 bg-green-900 rounded-sm text-white hover:cursor-pointer hover:bg-green-950">Edit</button> */}
              <button onClick={() => handleDelete(task.id)} className="px-2 py-1 bg-red-900 rounded-sm text-white hover:cursor-pointer hover:bg-red-950">Delete</button>
            </div>
          ))
        }
      </ul>
    </div>
  )
}

export default TaskList