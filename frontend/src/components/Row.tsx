import type { ReactNode } from "react";

interface RowProps {
    children: ReactNode;
}

function Row({ children }: RowProps) {
    return (
        <div
            style={{
                display: "flex",
                gap: "1rem",
                alignItems: "center",
                flexWrap: "wrap",
            }}
        >
            {children}
        </div>
    );
}

export default Row;