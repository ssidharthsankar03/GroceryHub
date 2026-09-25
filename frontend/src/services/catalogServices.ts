import api from './api'
import type { Brand, Category, Product } from '../types/catalog'

export async function getCategories(): Promise<Category[]> {
  const response = await api.get<Category[]>('/categories')

  return response.data
}

export async function getBrands(): Promise<Brand[]> {
  const response = await api.get<Brand[]>('/brands')

  return response.data
}

export async function getProducts(): Promise<Product[]> {
  const response = await api.get<Product[]>('/products')

  return response.data
}

export async function getProduct(productId: number): Promise<Product> {
  const response = await api.get<Product>(`/products/${productId}`)

  return response.data
}