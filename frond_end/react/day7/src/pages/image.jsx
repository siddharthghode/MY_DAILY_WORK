import ImageCard from "../components/image_card";

export default function ImagePage() {
  const images = [
    {
      id: 1,
      image:
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=400&h=250&fit=crop",
      title: "Mountain View",
      description: "A peaceful view of mountains under a clear blue sky.",
    },
    {
      id: 2,
      image:
        "https://images.unsplash.com/photo-1494526585095-c41746248156?w=400&h=250&fit=crop",
      title: "City Lights",
      description: "Night view of the city filled with bright lights and energy.",
    },
    {
      id: 3,
      image:
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=400&h=250&fit=crop",
      title: "Forest Path",
      description: "A calm walking path surrounded by green forest.",
    },
    {
      id: 4,
      image:
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=400&h=250&fit=crop",
      title: "Ocean Waves",
      description: "Waves crashing on the shore with a relaxing sound.",
    },
    {
      id: 5,
      image:
        "https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=400&h=250&fit=crop",
      title: "Sunset Sky",
      description: "Beautiful sunset colors spreading across the sky.",
    },
  ];

  return (
    <div style={{ padding: "20px" }}>
      <h1>Image Page</h1>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
        }}
      >
        {images.map((img) => (
          <ImageCard
            key={img.id}
            image={img.image}
            title={img.title}
            description={img.description}
          />
        ))}
      </div>
    </div>
  );
}
