export interface DialogueLine {
    speaker: string;
    danish: string;
    english: string;
}

export interface LessonDetails {
    id: string;
    topic: string;
    level: string;

    speaker1: {
        name: string;
        gender: string;
        voice: string;
    };

    speaker2: {
        name: string;
        gender: string;
        voice: string;
    };

    dialogue: DialogueLine[];

    vocabulary: unknown[];

    conversation_audio: string | null;
    learning_audio: string | null;
    shadowing_audio: string | null;
}