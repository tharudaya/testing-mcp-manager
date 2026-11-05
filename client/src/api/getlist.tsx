
export type Task = {
  text: string,
  id: number
};

const getList = async (): Promise<Task[]> => {
  const response = await fetch("http://127.0.0.1:8000/tasks");
  if (!response.ok) {
    throw new Error("Something went wrong")
  }

  return response.json()
}

export default getList;