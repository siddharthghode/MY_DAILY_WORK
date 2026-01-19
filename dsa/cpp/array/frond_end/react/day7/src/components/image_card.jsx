export default function ImageCard({ image, title, description }) {
  const containerStyle = {
    width: '300px',
    border: '1px solid #ddd',
    borderRadius: '8px',
    overflow: 'hidden',
    fontFamily: 'Arial, sans-serif',
  };

  const imgStyle = { width: '100%', display: 'block' };
  const contentStyle = { padding: '12px' };
  const titleStyle = { margin: '0 0 8px', fontSize: '18px' };
  const descStyle = { margin: 0, fontSize: '14px', color: '#555' };

  return (
    <div style={containerStyle}>
      <img src={image} alt={title} style={imgStyle} />

      <div style={contentStyle}>
        <h3 style={titleStyle}>{title}</h3>

        <p style={descStyle}>{description}</p>
      </div>
    </div>
  );
}

