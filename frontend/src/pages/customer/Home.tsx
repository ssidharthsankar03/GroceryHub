import "../../App.css";
import { useEffect, useState } from "react";
import { getCategories, getProducts } from "../../services/catalogServices";
import type { Category, Product } from "../../types/catalog";
import { Link } from "react-router-dom";
import { toast } from "sonner";
import { useAuthStore } from "../../store/authStore";

function Home() {
  const [categories, setCategories] = useState<Category[]>([]);
  const [isLoadingCategories, setIsLoadingCategories] = useState(true);
  const [products, setProducts] = useState<Product[]>([]);
  const [isLoadingProducts, setIsLoadingProducts] = useState(true);
  const { isAuthenticated, user, logout } = useAuthStore();

  useEffect(() => {
    const loadCategories = async () => {
      try {
        const data = await getCategories();
        setCategories(data);
      } catch (error) {
        console.error("Failed to load categories:", error);
      } finally {
        setIsLoadingCategories(false);
      }
    };

    loadCategories();
  }, []);
  useEffect(() => {
    const loadProducts = async () => {
      try {
        const data = await getProducts();
        setProducts(data);
      } catch (error) {
        console.error("Failed to load products:", error);
      } finally {
        setIsLoadingProducts(false);
      }
    };

    loadProducts();
  }, []);
  return (
    <div className="app">
      <header className="navbar">
        <div className="brand">
          <span className="brand-icon">🛒</span>
          <span>GroceryHub</span>
        </div>

        <nav className="nav-links">
          <a href="#">Home</a>
          <a href="#">Products</a>
          <a href="#">Categories</a>
        </nav>

        <div className="nav-actions">
          <button type="button" className="icon-button">
            🔍
          </button>

          <button type="button" className="icon-button">
            🛒
          </button>

          {isAuthenticated ? (
            <>
              <Link to="/profile" className="login-button">
                {user ? user.first_name : "Profile"}
              </Link>

              <button
                type="button"
                className="login-button"
                onClick={() => {
                  logout();
                  toast.success("Logged out successfully!");
                }}
              >
                Logout
              </button>
            </>
          ) : (
            <Link to="/login" className="login-button">
              Login
            </Link>
          )}
        </div>
      </header>

      <main>
        <section className="hero-section">
          <div className="hero-content">
            <span className="hero-badge">Fresh groceries, delivered</span>

            <h1>
              Everything you need,
              <br />
              <span>right at your doorstep.</span>
            </h1>

            <p>
              Shop fresh groceries, everyday essentials and your favourite
              products from the comfort of your home.
            </p>

            <div className="hero-actions">
              <button type="button" className="primary-button">
                Shop Now
              </button>

              <button type="button" className="secondary-button">
                Explore Categories
              </button>
            </div>
          </div>
        </section>

        <section className="categories-section">
          <div className="section-heading">
            <div>
              <span className="section-label">Browse</span>
              <h2>Shop by Category</h2>
            </div>

            <a href="#">View all →</a>
          </div>

          <div className="category-grid">
            {isLoadingCategories ? (
              <p>Loading categories...</p>
            ) : categories.length === 0 ? (
              <p>No categories available.</p>
            ) : (
              categories.map((category) => (
                <div className="category-card" key={category.id}>
                  <h3>{category.name}</h3>

                  {category.description && <p>{category.description}</p>}
                </div>
              ))
            )}
          </div>
        </section>

        <section className="products-section">
          <div className="product-grid">
            {isLoadingProducts ? (
              <p>Loading products...</p>
            ) : products.length === 0 ? (
              <p>No products available.</p>
            ) : (
              products.map((product) => (
                <article className="product-card" key={product.id}>
                  <div className="product-image-placeholder">🛒</div>

                  <div className="product-card-content">
                    <h3>{product.name}</h3>
                    {product.description && <p>{product.description}</p>}
                    <Link to={`/products/${product.id}`}>
                      View Product
                    </Link>{" "}
                  </div>
                </article>
              ))
            )}
          </div>
        </section>
      </main>

      <footer className="footer">
        <div>
          <strong>🛒 GroceryHub</strong>
          <p>Your everyday grocery destination.</p>
        </div>

        <p>© 2026 GroceryHub. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default Home;
