interface SpacerProps {
    size?: number;
}

function Spacer({ size = 16 }: SpacerProps) {
    return <div style={{ height: size }} />;
}

export default Spacer;