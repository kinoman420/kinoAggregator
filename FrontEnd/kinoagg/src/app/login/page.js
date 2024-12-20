'use client'

import React, { useEffect, useState } from "react";
import { useFormState, useFormStatus } from 'react-dom'
import { signup } from '../actions/auth'
import { roboto_mono } from '../ui/font';
import { useActionState } from 'react'
import Link from 'next/link'
import { useRouter } from "next/navigation";

 
function SignupForm() {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [username, setUsername] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const router = useRouter;

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

    try {
        const response = await fetch('/api/Token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'username': username,
                'password': password,
            }),
        });

        const exists = await response.json();

        if (response.ok) {
            
            const data = await response.json();
            localStorage.setItem('token', data.access_token);
            localStorage.setItem('username', username);
            localStorage.setItem('is_admin', data.is_admin);
            router.push('/');
        } else {
            
            setError('Something went wrong.');
            
        }
    } catch (error) {
        setError('Network error. Please try again.');
    } finally {
        setLoading(false);
    }}

  const [state, action] = useActionState(signup, undefined)
  return (
    <div className={`flex items-center justify-center min-h-screen bg-gray-100 ${roboto_mono.className}` }>
        <div className="w-full max-w-xs">
        <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" onSubmit={handleSubmit}>
            <div className="mb-4">
                <input
                    id="email"
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </div>
            {state?.errors?.email && <p>{state.errors.email}</p>}
            <div className="mb-6">
                <input
                    id="password"
                    className="shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </div>
            {state?.errors?.password && (
        <div>
          <p>Password must:</p>
          <ul>
            {state.errors.password.map((error) => (
              <li key={error}>- {error}</li>
            ))}
          </ul>
        </div>
      )}
            <div className="flex items-center justify-center">
                <SubmitButton />
            </div>
            <p className="text-center text-gray-600 text-xs mt-4">
                Don't have an account? <Link href="/register" className="text-blue-500 hover:text-blue-800">Register </Link>
            </p>
        </form>
        </div>
    </div>
  )
  
}

function SubmitButton() {
    const { pending } = useFormStatus()
   
    return (
      <button disabled={pending} className="text-black bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
        Log in
      </button>
    )
  }

export default SignupForm;