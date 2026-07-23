import { useMemo, useState } from "react";

interface LessonAudioPanelProps {
    conversationAudio: string | null;
    learningAudio: string | null;
    shadowingAudio: string | null;
}

type AudioMode = "conversation" | "learning" | "shadowing";

function LessonAudioPanel({
    conversationAudio,
    learningAudio,
    shadowingAudio,
}: LessonAudioPanelProps) {
    const [mode, setMode] = useState<AudioMode>("conversation");

    const audio = useMemo(() => {
        switch (mode) {
            case "conversation":
                return conversationAudio;
            case "learning":
                return learningAudio;
            case "shadowing":
                return shadowingAudio;
        }
    }, [mode, conversationAudio, learningAudio, shadowingAudio]);

    return (
        <>
            <h3>Audio</h3>

            <button onClick={() => setMode("conversation")}>
                Conversation
            </button>

            <button onClick={() => setMode("learning")}>
                Learning
            </button>

            <button onClick={() => setMode("shadowing")}>
                Shadowing
            </button>

            <p>
                Current mode: <strong>{mode}</strong>
            </p>

            {audio ? (
                <audio
                    key={audio}
                    controls
                    autoPlay
                    src={`http://localhost:8000${audio}`}
                />
            ) : (
                <p>No audio available.</p>
            )}
        </>
    );
}

export default LessonAudioPanel;