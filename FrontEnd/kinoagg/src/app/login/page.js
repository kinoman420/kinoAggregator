import { useEffect, useState } from "react";
import axios from "../utils/axios";
import { useRouter } from "next/router";

export default function Admin() {
    const [message, setMessage] = useState("");
    const router = useRouter();

    useEffect(() => {
        const fetchData = async () => {
            const token = localStorage.getItem("token");
            if (!token) {
                router.push("/login");
                return;
            }
            try {
                const response = await axios.get("/admin", {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });
                setMessage(response.data.message);
            } catch (error) {
                console.error("Error fetching admin data:", error);
                router.push("/login");
            }
        };
        fetchData();
    }, [router]);

    return (
        <div>
            <h1>Admin Page</h1>
            <p>{message}</p>
        </div>
    );
}
