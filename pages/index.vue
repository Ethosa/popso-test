<template>
  <div class="flex w-screen h-screen justify-center items-center">
    <div class="flex flex-col items-center gap-4 h-1/3 md:h-3/5 md:w-1/4 text-lg">
      <img src="~/public/popso.svg" class="select-none pointer-events-none w-2/3 md:w-1/2 mb-8">
      <PopsoInput class="w-full" placeholder="Логин" type="text" v-model:value="login" />
      <PopsoInput class="w-full" placeholder="Пароль" type="password" v-model:value="password" />
      <PopsoButton class="w-full" @clicked="console.log(login)">
        войти
      </PopsoButton>
    </div>
  </div>
</template>


<script setup>

const login = ref()
const password = ref()

</script>
