import BackButton from "./BackButton";
import PageTitle from "./PageTitle";

interface LessonHeaderProps {
    topic: string;
    level: string;
}

function LessonHeader({ topic, level }: LessonHeaderProps) {
    return (
        <>
            <BackButton />

            <PageTitle>{topic}</PageTitle>

            <p>Level: {level}</p>
        </>
    );
}

export default LessonHeader;