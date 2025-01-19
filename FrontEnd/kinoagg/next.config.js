/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    images: {
        domains: ['127.0.0.1'], // Allow images from the FastAPI server
    },
};

module.exports = nextConfig;
