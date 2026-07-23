import DialogueLineCard from "./DialogueLineCard";
import type { DialogueLine } from "../types/lessonDetails";

interface DialogueListProps {
    dialogue: DialogueLine[];
    showTranslation: boolean;
}

function DialogueList({
    dialogue,
    showTranslation,
}: DialogueListProps) {
    return (
        <>
            {dialogue.map((line, index) => (
                <DialogueLineCard
                    key={index}
                    line={line}
                    showTranslation={showTranslation}
                />
            ))}
        </>
    );
}

export default DialogueList;