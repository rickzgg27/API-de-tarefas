import express from "express";
import sqlite3 from "sqlite3";
import { open } from "sqlite";

const app = express();
app.use(express.json());

const db = await open({
  filename: "./tasks.db",
  driver: sqlite3.Database,
});

await db.exec("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT)");

interface Task {
    id: number;
    title: string;
}

app.get("/tasks", async (_: express.Request, res: express.Response): Promise<void> => {
    const tasks: Task[] = await db.all("SELECT * FROM tasks");
    res.json(tasks);
});

app.post("/tasks", async (req: express.Request, res: express.Response): Promise<void> => {
    const { title } = req.body as { title: string };
    await db.run("INSERT INTO tasks (title) VALUES (?)", [title]);
    res.json({ message: "Tarefa criada!" });
});

app.listen(3000, () => console.log("API rodando na porta 3000"));
