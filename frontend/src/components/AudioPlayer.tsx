interface AudioPlayerProps {
    audioPath: string | null;
}

function AudioPlayer({ audioPath }: AudioPlayerProps) {
    if (!audioPath) {
        return <span>No audio</span>;
    }

    return <audio controls src={audioPath} />;
}

export default AudioPlayer;