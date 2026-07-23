import { useEffect, useState } from "react";
import { getLesson } from "../api/lessonDetailsApi";
import type { LessonDetails } from "../types/lessonDetails";

export function useLesson(id: string | undefined) {
    const [lesson, setLesson] = useState<LessonDetails | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        if (!id) return;

        getLesson(id)
            .then(setLesson)
            .catch(() => setError("Failed to load lesson."))
            .finally(() => setLoading(false));
    }, [id]);

    return {
        lesson,
        loading,
        error,
    };
}