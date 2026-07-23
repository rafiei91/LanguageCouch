import { useState } from "react";
import { generateLesson } from "../api/generateLessonApi";

interface UseGenerateLessonOptions {
    onSuccess?: () => Promise<void> | void;
}

export function useGenerateLesson(options?: UseGenerateLessonOptions) {
    const [generating, setGenerating] = useState(false);

    async function generate(topic: string, level: string) {
        setGenerating(true);

        try {
            await generateLesson(topic, level);

            await options?.onSuccess?.();
        } finally {
            setGenerating(false);
        }
    }

    return {
        generating,
        generate,
    };
}