import { useAuthStore } from "~/stores/auth"

export default defineNuxtRouteMiddleware((to, from) => {
  const authState = useAuthStore()
  
  if (!authState.isAuthorized && to.fullPath !== "/") {
    return navigateTo("/")
  }
})