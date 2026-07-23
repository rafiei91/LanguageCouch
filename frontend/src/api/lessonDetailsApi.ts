import client from "./client";

export async function getLesson(id: string) {
    const response = await client.get(`/lessons/${id}`);
    return response.data;
}