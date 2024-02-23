<template>
  <div class="flex w-screen h-screen justify-center items-center">
    <div class="flex flex-col items-center gap-4 h-1/3 md:h-3/5 md:w-1/4 text-lg">
      <img src="/popso.svg" class="select-none pointer-events-none w-2/3 md:w-1/2 mb-8">
      <PopsoInput
        class="w-full"
        placeholder="Логин"
        :error="loginError"
        type="text"
        v-model:value="login"
      />
      <PopsoInput
        class="w-full"
        placeholder="Пароль"
        :error="passwordError"
        type="password"
        v-model:value="password"
      />
      <PopsoButton class="w-full" @clicked="auth()">
        {{ authState.value ? 'войти' : 'зарегистрироваться' }}
      </PopsoButton>
    </div>
  </div>
</template>


<script setup>
import api from '~/mixins/api'
import { useAuthStore } from "~/stores/auth"

definePageMeta({
  middleware: 'auth'
})

// cookies
const loginCookie = useCookie('login', {default: _ => ""})
const passwordCookie = useCookie('password', {default: _ => ""})
const authState = useState('auth', () => loginCookie.value !== '' && passwordCookie.value !== '')

// data
const login = ref(loginCookie)
const password = ref(passwordCookie)
const loginError = ref()
const passwordError = ref()

const authStore = useAuthStore()

async function auth() {
  let data = null
  if (authState.value) {
    const response = await api.auth(login.value, password.value)
    data = response
  } else {
    const response = await api.register(login.value, password.value)
    data = response
  }

  if ('response' in data) {
    loginCookie.value = login.value
    passwordCookie.value = password.value
    authStore.isAuthorized = true
    authStore.id = data['response']['id']
    await navigateTo("/dashboard")
  } else {
    passwordError.value = data["error"]
  }
}

</script>
