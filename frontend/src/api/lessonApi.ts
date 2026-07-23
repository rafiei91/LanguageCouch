import client from "./client";

export async function getLessons() {
    const response = await client.get("/lessons");
    return response.data;
}