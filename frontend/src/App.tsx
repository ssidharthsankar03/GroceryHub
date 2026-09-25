import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Home from "./pages/customer/Home";
import Login from "./pages/auth/Login";

import Profile from "./pages/customer/Profile";

import Register from "./pages/auth/Register";

import ProductDetails from "./pages/customer/ProductDetails";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />

        {/* Temporary routes — we'll build these pages next */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/admin" element={<div>Admin Dashboard</div>} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/products/:productId" element={<ProductDetails />} />
        {/* Unknown routes */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
