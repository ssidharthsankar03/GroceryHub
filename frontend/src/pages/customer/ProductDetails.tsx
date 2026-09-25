import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { getProduct } from '../../services/catalogServices'
import type { Product } from '../../types/catalog'

function ProductDetails() {
  const { productId } = useParams<{ productId: string }>()

  const [product, setProduct] = useState<Product | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadProduct = async () => {
      if (!productId) {
        setError('Product not found')
        setIsLoading(false)
        return
      }

      try {
        const data = await getProduct(Number(productId))
        setProduct(data)
      } catch (error) {
        console.error('Failed to load product:', error)
        setError('Unable to load product')
      } finally {
        setIsLoading(false)
      }
    }

    loadProduct()
  }, [productId])

  if (isLoading) {
    return (
      <main style={{ padding: '40px' }}>
        <h1>Loading product...</h1>
      </main>
    )
  }

  if (error || !product) {
    return (
      <main style={{ padding: '40px' }}>
        <h1>{error || 'Product not found'}</h1>
        <Link to="/">← Back to GroceryHub</Link>
      </main>
    )
  }

  return (
    <main style={{ padding: '40px' }}>
      <Link to="/">← Back to GroceryHub</Link>

      <section style={{ marginTop: '32px' }}>
        <div className="product-image-placeholder">🛒</div>

        <h1>{product.name}</h1>

        {product.description && <p>{product.description}</p>}

        <p>Category ID: {product.category_id}</p>
        <p>Brand ID: {product.brand_id}</p>

        <button type="button">
          Add to Cart
        </button>
      </section>
    </main>
  )
}

export default ProductDetails