import { useState, useEffect } from "react";
import axios from "axios";

export default function ImageGallery() {
    const [images, setImages] = useState([]);
    const [selectedImage, setSelectedImage] = useState(null);

    useEffect(() => {
        fetchImages();
    }, []);

    const fetchImages = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:8000/media/images");
            setImages(response.data.images);
        } catch (error) {
            console.error("Error fetching images:", error);
        }
    };

    return (
        <div className="mt-6">
            <h2 className="text-2xl font-semibold text-center">Image Gallery</h2>
            <div className="flex flex-wrap justify-center gap-4 mt-4">
                {images.map((img, index) => (
                    <img
                        key={index}
                        src={`http://127.0.0.1:8000/media/image/${img}`}
                        alt="Uploaded"
                        className="w-24 h-24 object-cover rounded cursor-pointer transition hover:scale-110"
                        onClick={() => setSelectedImage(img)}
                    />
                ))}
            </div>

            {selectedImage && (
                <div
                    className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-80"
                    onClick={() => setSelectedImage(null)}
                >
                    <img
                        src={`http://127.0.0.1:8000/media/image/${selectedImage}`}
                        className="max-w-full max-h-full rounded-lg"
                    />
                </div>
            )}
        </div>
    );
}
