import Container from "../components/Container";

interface MainLayoutProps {
    children: React.ReactNode;
}

function MainLayout({ children }: MainLayoutProps) {
    return (
        <main>
            <Container>{children}</Container>
        </main>
    );
}

export default MainLayout;