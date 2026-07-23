import type { ReactNode } from "react";

interface CardProps {
    children: ReactNode;
}

function Card({ children }: CardProps) {
    return (
        <div
            style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "1rem",
                marginBottom: "1rem",
            }}
        >
            {children}
        </div>
    );
}

export default Card;