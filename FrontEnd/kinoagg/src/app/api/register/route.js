// app/api/register/route.js
import { NextResponse } from 'next/server';

export async function POST(request) {
    const { username, email, password } = await request.json();

    try {
        const response = await fetch('http://localhost:8000/Register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, email, password }),
        });

        const data = await response.json();
        if (response.ok) {
            return NextResponse.json(data);
        } else {
            return NextResponse.json(data, { status: response.status });
        }
    } catch (error) {
        return NextResponse.json({ detail: 'Internal Server Error' }, { status: 500 });
    }
}
