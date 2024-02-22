import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    isAuthorized: false,
    userId: 0,
    firstName: '',
    lastName: '',
  })
})