import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getCurrentUser } from '../../services/authServices'

interface User {
  id: number
  first_name: string
  last_name: string
  email: string
  phone_number: string
  is_active: boolean
}

function Profile() {
  const [user, setUser] = useState<User | null>(null)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadUser = async () => {
      try {
        const data = await getCurrentUser()
        setUser(data)
      } catch (error) {
        console.error('Failed to load user:', error)
        setError('Unable to load profile')
      }
    }

    loadUser()
  }, [])

  if (error) {
    return (
      <main style={{ padding: '40px' }}>
        <h1>{error}</h1>
        <Link to="/">Back to Home</Link>
      </main>
    )
  }

  if (!user) {
    return (
      <main style={{ padding: '40px' }}>
        <h1>Loading profile...</h1>
      </main>
    )
  }

  return (
    <main style={{ padding: '40px' }}>
      <h1>
        Welcome, {user.first_name} {user.last_name}
      </h1>

      <p>Email: {user.email}</p>
      <p>Phone: {user.phone_number}</p>
      <p>Status: {user.is_active ? 'Active' : 'Inactive'}</p>

      <Link to="/">Back to Home</Link>
    </main>
  )
}

export default Profile