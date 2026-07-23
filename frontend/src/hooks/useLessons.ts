import { useEffect, useState } from "react";
import { getLessons } from "../api/lessonApi";
import type { Lesson } from "../types/lesson";

export function useLessons() {
    const [lessons, setLessons] = useState<Lesson[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    async function loadLessons() {
        setLoading(true);
        setError("");

        try {
            const data = await getLessons();
            setLessons(data);
        } catch {
            setError("Failed to load lessons.");
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        loadLessons();
    }, []);

    return {
        lessons,
        loading,
        error,
        loadLessons,
    };
}