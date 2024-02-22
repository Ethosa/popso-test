<template>
  <div class="flex flex-col items-end rounded-lg bg-white p-8 gap-4">
    <div class="flex w-full gap-8">
      <div class="flex flex-col w-full gap-4">
        <PopsoInput
          placeholder="Имя"
          :flat="true"
          :error="firstNameError"
          v-model:value="firstName"
        />
        <PopsoInput
          placeholder="Фамилия"
          :flat="true"
          :error="lastNameError"
          v-model:value="lastName"
        />
      </div>
      <div class="flex flex-col w-full gap-4">
        <PopsoInput
          placeholder="Логин"
          :flat="true"
          :error="loginError"
          v-model:value="login"
        />
        <PopsoInput
          placeholder="Пароль"
          :flat="true"
          :error="passwordError"
          type="password"
          v-model:value="password"
        />
      </div>
    </div>
    <PopsoButton
      class="w-fit"
      @click="saveUser()"
    >
      сохранить
    </PopsoButton>
  </div>
</template>

<script setup>
import api from '~/mixins/api'
import { useAuthStore } from "~/stores/auth"


const loginCookie = useCookie('login', {default: (v) => ""})
const passwordCookie = useCookie('password', {default: (v) => ""})


const firstNameError = ref('')
const lastNameError = ref('')
const loginError = ref('')
const passwordError = ref('')

const firstName = ref('')
const lastName = ref('')
const login = ref(loginCookie.value)
const password = ref(passwordCookie.value)

const authStore = useAuthStore()


async function saveUser() {
  const response = await api.updateUser(
    loginCookie.value, passwordCookie.value,
    firstName.value, lastName.value, login.value, password.value
  )
  console.log(response)
  if ('response' in response) {
    authStore.firstName = firstName.value
    authStore.lastName = lastName.value
    loginCookie.value = login.value
    passwordCookie.value = password.value
  } else {
    passwordError.value = response['error']
  }
}

onMounted(async () => {
  const response = await api.getById(authStore.id)
  console.log(response)
  if ('response' in response) {
    firstName.value = response['response']['first_name']
    lastName.value = response['response']['last_name']
  }
})

</script>
