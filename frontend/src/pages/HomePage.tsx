import { useState } from "react";
import Loading from "../components/Loading";
import ErrorMessage from "../components/ErrorMessage";
import GenerateLessonForm from "../components/GenerateLessonForm";
import LessonList from "../components/LessonList";
import PageTitle from "../components/PageTitle";
import Section from "../components/Section";
import Spacer from "../components/Spacer";
import { useLessons } from "../hooks/useLessons";
import { useGenerateLesson } from "../hooks/useGenerateLesson";

function HomePage() {
    const { lessons, loading, error, loadLessons } = useLessons();

    const { generating, generate } = useGenerateLesson({
        onSuccess: loadLessons,
    });

    const [topic, setTopic] = useState("Greetings");
    const [level, setLevel] = useState("A1");

    async function handleGenerateLesson() {
        await generate(topic, level);
    }

    return (
        <>
            <Section>
                <PageTitle>LanguageCouch</PageTitle>
            </Section>

            <GenerateLessonForm
                topic={topic}
                level={level}
                generating={generating}
                onTopicChange={setTopic}
                onLevelChange={setLevel}
                onGenerate={handleGenerateLesson}
            />

            <Spacer />

            <Section>
                {(loading || generating) && <Loading />}

                {!loading && !generating && error && (
                    <ErrorMessage message={error} />
                )}

                {!loading && !generating && !error && (
                    <LessonList lessons={lessons} />
                )}
            </Section>
        </>
    );
}

export default HomePage;