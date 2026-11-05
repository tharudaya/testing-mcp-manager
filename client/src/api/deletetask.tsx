const DeleteTask = async (id: number) => {
  const response = await fetch(`http://127.0.0.1:8000/tasks/${id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      id: id
    })
  });
  if (!response.ok) {
    throw new Error("Something went wrong")
  }

  return response.json()
}

export default DeleteTask;