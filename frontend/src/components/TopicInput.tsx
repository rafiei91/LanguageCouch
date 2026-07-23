interface TopicInputProps {
    value: string;
    onChange: (value: string) => void;
}

function TopicInput({ value, onChange }: TopicInputProps) {
    return (
        <input
            type="text"
            placeholder="Topic"
            value={value}
            onChange={(e) => onChange(e.target.value)}
            style={{
                flex: 1,
                padding: "0.5rem",
            }}
        />
    );
}

export default TopicInput;