import { useEffect, useState } from "react"
import CreateTask from "./api/createtask";
import TaskList from "./components/tasklist"

function App() {

  const [task, setTask] = useState<string>("");
  const [isCreated, setIscreated] = useState(false);
  const [isOnline, setIsOnline] = useState(true);

  useEffect(() => {

    setIsOnline(navigator.onLine);

    const handleOnline = () => {
      setIsOnline(true)
    }
    const handleOffline = () => {
      setIsOnline(false);
    }

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return (() => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    });

  }, [navigator.onLine])

  const handleButtonClick = () => {
    CreateTask(task)
      .then(() => setIscreated(true))
      .catch((error) => console.error(error))
    setTask("");
    setTimeout(() => {
      setIscreated(false)
    }, 500)
  }

  return (
    <>
      <h1 className="text-5xl text-center m-10">Task Manager</h1>
      <div className="p-10 w-3/4 md:w-1/2 mx-auto border rounded-2xl">
        <div className="flex mb-5">
          <input value={task} onChange={(e) => setTask(e.target.value)} className="border flex-4 p-2" type="text" name="input" placeholder="Enter the task" />
          <button onClick={handleButtonClick} className="p-2 flex-1 bg-blue-900 text-white hover:cursor-pointer hover:bg-blue-950">ADD</button>
        </div>
        <TaskList isCreated={isCreated} />
      </div>
      {
        !isOnline && (
          <h2 className="text-red-700 text-5xl">Hey, you are offline</h2>
        )
      }
      <div>
      </div>
    </>
  )
}

export default App