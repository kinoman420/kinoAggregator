import { useState } from "react";
import axios from "axios";

export default function ImageUpload({ refreshGallery }) {
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        if (!selectedFile) return alert("Please select a file.");

        const formData = new FormData();
        formData.append("file", selectedFile);

        try {
            await axios.post("http://127.0.0.1:8000/media/upload", formData);
            alert("Upload successful!");
            refreshGallery(); // Refresh gallery after upload
        } catch (error) {
            console.error("Upload failed:", error);
            alert("Upload failed. Try again.");
        }
    };

    return (
        <div className="flex flex-col items-center space-y-4">
            <input
                type="file"
                className="border p-2 rounded w-60 text-gray-700"
                onChange={handleFileChange}
            />
            <button
                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
                onClick={handleUpload}
            >
                Upload Image
            </button>
        </div>
    );
}
