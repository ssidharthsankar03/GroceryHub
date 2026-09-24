import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import Home from './pages/customer/Home'
import Login from './pages/auth/Login'
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />

        {/* Temporary routes — we'll build these pages next */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<div>Register Page</div>} />
        <Route path="/admin" element={<div>Admin Dashboard</div>} />

        {/* Unknown routes */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App