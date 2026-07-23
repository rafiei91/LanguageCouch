import Card from "./Card";
import type { DialogueLine } from "../types/lessonDetails";

interface DialogueLineCardProps {
    line: DialogueLine;
    showTranslation: boolean;
}

function DialogueLineCard({
    line,
    showTranslation,
}: DialogueLineCardProps) {
    return (
        <Card>
            <strong>{line.speaker}</strong>

            <p>{line.danish}</p>

            {showTranslation && <p>{line.english}</p>}
        </Card>
    );
}

export default DialogueLineCard;