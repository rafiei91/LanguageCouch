import client from "./client";

export async function generateLesson(topic: string, level: string) {
    const response = await client.post("/lessons/generate", {
        topic,
        level,
    });

    return response.data;
}