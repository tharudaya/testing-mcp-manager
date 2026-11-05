const CreateTask = async (task: string) => {
  const response = await fetch("http://127.0.0.1:8000/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      text: task
    })
  })
  if (!response.ok) {
    throw new Error("Could not create the task")
  }

  return response;

}

export default CreateTask;