// app/api/token/route.js
import { NextResponse } from 'next/server';

export async function POST(request) {
    const { username, password } = await request.json();

    try {
        const response = await fetch('http://localhost:8000/Token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'username': username,
                'password': password,
            }),
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
