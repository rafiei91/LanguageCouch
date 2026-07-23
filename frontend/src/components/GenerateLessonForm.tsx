import Row from "./Row";
import Section from "./Section";
import TopicInput from "./TopicInput";
import LevelSelect from "./LevelSelect";
import GenerateLessonButton from "./GenerateLessonButton";

interface GenerateLessonFormProps {
    topic: string;
    level: string;
    generating: boolean;
    onTopicChange: (value: string) => void;
    onLevelChange: (value: string) => void;
    onGenerate: () => void;
}

function GenerateLessonForm({
    topic,
    level,
    generating,
    onTopicChange,
    onLevelChange,
    onGenerate,
}: GenerateLessonFormProps) {
    return (
        <Section>
            <Row>
                <TopicInput
                    value={topic}
                    onChange={onTopicChange}
                />

                <LevelSelect
                    value={level}
                    onChange={onLevelChange}
                />

                <GenerateLessonButton
                    onClick={onGenerate}
                    disabled={generating}
                    generating={generating}
                />
            </Row>
        </Section>
    );
}

export default GenerateLessonForm;