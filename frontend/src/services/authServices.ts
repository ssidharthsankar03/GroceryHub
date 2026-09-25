import api from "./api";

interface LoginRequest {
  email: string;
  password: string;
}

interface LoginResponse {
  access_token: string;
  token_type: string;
}

interface UserResponse {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
  is_active: boolean;
}
interface RegisterRequest {
  first_name: string
  last_name: string
  email: string
  phone_number: string
  password: string
}


export async function loginUser(
  credentials: LoginRequest,
): Promise<LoginResponse> {
  const response = await api.post<LoginResponse>("/auth/login", credentials);

  return response.data;
}

export async function getCurrentUser(): Promise<UserResponse> {
  const response = await api.get<UserResponse>("/auth/me");

  return response.data;
}

export async function registerUser(
  userData: RegisterRequest,
) {
  const response = await api.post('/auth/register', userData)

  return response.data
}