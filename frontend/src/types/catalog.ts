export interface Category {
  id: number
  name: string
  description: string | null
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface Brand {
  id: number
  name: string
  description: string | null
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface Product {
  id: number
  name: string
  description: string | null
  category_id: number
  brand_id: number
  is_active: boolean
  created_at: string
  updated_at: string
}