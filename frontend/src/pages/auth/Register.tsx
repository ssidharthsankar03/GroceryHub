import { useState } from "react";
import type { FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { registerUser } from "../../services/authServices";
import { toast } from "sonner";

function Register() {
  const navigate = useNavigate();

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    setError("");
    setIsLoading(true);

    try {
      await registerUser({
        first_name: firstName,
        last_name: lastName,
        email,
        phone_number: phoneNumber,
        password,
      });
      toast.success("Account created successfully!");

      navigate("/login");
    } catch (error) {
      console.error("Registration failed:", error);

      setError("Unable to create account. Please check your details.");
      toast.error("Unable to create account");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="auth-page">
      <section className="auth-card">
        <div className="auth-header">
          <div className="auth-logo">🛒</div>

          <h1>Create your account</h1>

          <p>Join GroceryHub today</p>
        </div>

        <form onSubmit={handleSubmit} className="auth-form">
          <div className="form-group">
            <label htmlFor="firstName">First name</label>

            <input
              id="firstName"
              type="text"
              placeholder="Enter your first name"
              value={firstName}
              onChange={(event) => setFirstName(event.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="lastName">Last name</label>

            <input
              id="lastName"
              type="text"
              placeholder="Enter your last name"
              value={lastName}
              onChange={(event) => setLastName(event.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="registerEmail">Email</label>

            <input
              id="registerEmail"
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="phoneNumber">Phone number</label>

            <input
              id="phoneNumber"
              type="tel"
              placeholder="Enter your phone number"
              value={phoneNumber}
              onChange={(event) => setPhoneNumber(event.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="registerPassword">Password</label>

            <input
              id="registerPassword"
              type="password"
              placeholder="Create a password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              required
              minLength={8}
            />
          </div>

          {error && <p className="auth-error">{error}</p>}

          <button type="submit" className="auth-submit" disabled={isLoading}>
            {isLoading ? "Creating account..." : "Create account"}
          </button>
        </form>

        <div className="auth-footer">
          <p>
            Already have an account? <Link to="/login">Login</Link>
          </p>

          <Link to="/">← Back to GroceryHub</Link>
        </div>
      </section>
    </main>
  );
}

export default Register;
