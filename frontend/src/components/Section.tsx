import type { ReactNode } from "react";

interface SectionProps {
    children: ReactNode;
}

function Section({ children }: SectionProps) {
    return (
        <section
            style={{
                marginBottom: "2rem",
            }}
        >
            {children}
        </section>
    );
}

export default Section;