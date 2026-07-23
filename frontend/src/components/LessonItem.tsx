import LessonLink from "./LessonLink";
import Card from "./Card";
import type { Lesson } from "../types/lesson";

interface LessonItemProps {
    lesson: Lesson;
}

function LessonItem({ lesson }: LessonItemProps) {
    return (
        <LessonLink lessonId={lesson.id}>
            <Card>
                <h3>{lesson.topic}</h3>

                <p>Level: {lesson.level}</p>

                <p>{lesson.dialogue_count} lines</p>
            </Card>
        </LessonLink>
    );
}

export default LessonItem;