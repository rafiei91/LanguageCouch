import LessonItem from "./LessonItem";
import type { Lesson } from "../types/lesson";

interface LessonListProps {
    lessons: Lesson[];
}

function LessonList({ lessons }: LessonListProps) {
    if (lessons.length === 0) {
        return <p>No lessons yet.</p>;
    }

    return (
        <>
            {lessons.map((lesson) => (
                <LessonItem key={lesson.id} lesson={lesson} />
            ))}
        </>
    );
}

export default LessonList;