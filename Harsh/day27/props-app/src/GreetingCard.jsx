import React, { useRef, useState } from "react";
import "./GreetingCard.css";

const GreetingCard = ({ name, views, musicUrl }) => {
  const audioRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);

  const togglePlay = () => {
    if (!audioRef.current) return;

    if (isPlaying) {
      audioRef.current.pause();
    } else {
      audioRef.current.play();
    }
    setIsPlaying(!isPlaying);
  };

  return (
    <div className="main_div">
      <div className="greet-card">
        {/* Image wrapper */}
        <div className="image-wrapper">
          <img
            src="data:image/webp;base64,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"
            className="card-image"
          />
          <div className="overlay"></div>
        </div>

        {/* Header */}
        <div className="card-header">
          <span className="badge">Karan Aujla</span>
          <h2 className="title">{name || "Modern Design Solutions"}</h2>
        </div>

        {/* Description */}
        <p className="description">Album : P-POP CULTURE</p>

        {/* Footer */}
        <div className="card-footer">
          <button className="btn" onClick={togglePlay}>
            {isPlaying ? "⏸ Pause" : "▶ Play"}
          </button>
          <div className="views">
            <svg className="icon" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
              <path
                fillRule="evenodd"
                d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
                clipRule="evenodd"
              />
            </svg>
            <span>{views} views</span>
          </div>
        </div>

        {/* Hidden audio element */}
        {musicUrl && (
          <audio
            ref={audioRef}
            src={musicUrl}
            preload="auto"
            onEnded={() => setIsPlaying(false)} // reset when song ends
            onPause={() => setIsPlaying(false)} // sync state if paused externally
            onPlay={() => setIsPlaying(true)}   // sync state if played externally
          />
        )}
      </div>
    </div>
  );
};

export default GreetingCard;
