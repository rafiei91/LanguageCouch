interface LevelSelectProps {
    value: string;
    onChange: (value: string) => void;
}

function LevelSelect({ value, onChange }: LevelSelectProps) {
    return (
        <select
            value={value}
            onChange={(e) => onChange(e.target.value)}
            style={{
                padding: "0.5rem",
            }}
        >
            <option value="A1">A1</option>
            <option value="A2">A2</option>
            <option value="B1">B1</option>
            <option value="B2">B2</option>
            <option value="C1">C1</option>
            <option value="C2">C2</option>
        </select>
    );
}

export default LevelSelect;