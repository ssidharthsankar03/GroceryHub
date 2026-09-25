import { create } from 'zustand'

interface User {
  id: number
  first_name: string
  last_name: string
  email: string
  phone_number: string
  is_active: boolean
}

interface AuthState {
  token: string | null
  user: User | null
  isAuthenticated: boolean
  login: (token: string) => void
  setUser: (user: User) => void
  logout: () => void
}

const storedToken = localStorage.getItem('access_token')

export const useAuthStore = create<AuthState>((set) => ({
  token: storedToken,
  user: null,
  isAuthenticated: Boolean(storedToken),

  login: (token) => {
    localStorage.setItem('access_token', token)

    set({
      token,
      isAuthenticated: true,
    })
  },

  setUser: (user) => {
    set({
      user,
    })
  },

  logout: () => {
    localStorage.removeItem('access_token')

    set({
      token: null,
      user: null,
      isAuthenticated: false,
    })
  },
}))