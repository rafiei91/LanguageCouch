import { useState } from "react";
import Loading from "../components/Loading";
import ErrorMessage from "../components/ErrorMessage";
import LessonHeader from "../components/LessonHeader";
import LessonAudioPanel from "../components/LessonAudioPanel";
import DialogueList from "../components/DialogueList";
import { useLesson } from "../hooks/useLesson";

function LessonPage() {
    const id = window.location.pathname.split("/")[2];

    const { lesson, loading, error } = useLesson(id);

    const [showTranslation, setShowTranslation] = useState(true);

    if (loading) return <Loading />;

    if (error) return <ErrorMessage message={error} />;

    if (!lesson) return null;

    return (
        <>
            <LessonHeader
                topic={lesson.topic}
                level={lesson.level}
            />

            <LessonAudioPanel
                conversationAudio={lesson.conversation_audio}
                learningAudio={lesson.learning_audio}
                shadowingAudio={lesson.shadowing_audio}
            />

            <button
                type="button"
                onClick={() =>
                    setShowTranslation(!showTranslation)
                }
            >
                {showTranslation
                    ? "Hide translations"
                    : "Show translations"}
            </button>

            <DialogueList
                dialogue={lesson.dialogue}
                showTranslation={showTranslation}
            />
        </>
    );
}

export default LessonPage;