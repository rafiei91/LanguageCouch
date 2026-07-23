interface GenerateLessonButtonProps {
    onClick: () => void;
    disabled?: boolean;
    generating?: boolean;
}

function GenerateLessonButton({
    onClick,
    disabled = false,
    generating = false,
}: GenerateLessonButtonProps) {
    return (
        <button
            type="button"
            onClick={onClick}
            disabled={disabled}
        >
            {generating ? "Generating..." : "Generate Lesson"}
        </button>
    );
}

export default GenerateLessonButton;