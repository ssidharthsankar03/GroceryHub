import '../../App.css'

function Home() {
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
          <button type="button" className="login-button">
            Login
          </button>
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
            <div className="category-card">
              <span>🥦</span>
              <h3>Vegetables</h3>
              <p>Fresh & healthy</p>
            </div>

            <div className="category-card">
              <span>🍎</span>
              <h3>Fruits</h3>
              <p>Fresh every day</p>
            </div>

            <div className="category-card">
              <span>🥛</span>
              <h3>Dairy</h3>
              <p>Milk & essentials</p>
            </div>

            <div className="category-card">
              <span>🛢️</span>
              <h3>Cooking Oils</h3>
              <p>Everyday essentials</p>
            </div>

            <div className="category-card">
              <span>🍪</span>
              <h3>Snacks</h3>
              <p>Tasty favourites</p>
            </div>

            <div className="category-card">
              <span>🧹</span>
              <h3>Household</h3>
              <p>Home essentials</p>
            </div>
          </div>
        </section>

        <section className="products-section">
          <div className="section-heading">
            <div>
              <span className="section-label">Featured</span>
              <h2>Popular Products</h2>
            </div>

            <a href="#">View all →</a>
          </div>

          <div className="empty-products">
            <span>🛍️</span>
            <h3>Products coming soon</h3>
            <p>
              Our product catalogue will appear here once we connect the
              frontend to the GroceryHub API.
            </p>
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
  )
}

export default Home