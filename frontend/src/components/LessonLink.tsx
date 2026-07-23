import { Link } from "react-router-dom";

interface LessonLinkProps {
    lessonId: string;
    children: React.ReactNode;
}

function LessonLink({ lessonId, children }: LessonLinkProps) {
    return (
        <Link to={`/lessons/${lessonId}`}>
            {children}
        </Link>
    );
}

export default LessonLink;