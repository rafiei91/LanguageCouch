import type { ReactNode } from "react";

interface StackProps {
    children: ReactNode;
}

function Stack({ children }: StackProps) {
    return (
        <div
            style={{
                display: "flex",
                flexDirection: "column",
                gap: "1rem",
            }}
        >
            {children}
        </div>
    );
}

export default Stack;