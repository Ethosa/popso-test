<template>
  <div class="flex w-screen h-screen">
    <!-- navigation -->
    <div
      class="flex flex-col relative bg-white px-12 py-6 items-center gap-24 transition-all duration-150"
    >
      <Transition name="logo" mode="out-in">
        <div :key="sidebar">
          <img class="h-12" v-show="sidebar" src="/popso_first_letter.svg">
          <img class="h-12" v-show="!sidebar" src="/popso.svg">
        </div>
      </Transition>
      <div
        class="absolute -right-8 top-2 w-16 h-16 bg-white drop-shadow-lg cursor-pointer select-none flex justify-center items-center rounded-full"
        @click="toggle()"
      >
        <img ref="arrow" src="/arrow_back.svg" class="scale-100 duration-150">
      </div>
      <div class="flex flex-col items-center gap-4">
        <PopsoMenuItem
          :extend="sidebar"
          :color="current === 'Мой профиль' ? 'fill-primary' : 'fill-black'"
          :class="current === 'Мой профиль' ? 'text-primary' : 'text-black'"
          icon="work"
          title="Мой профиль"
          @click="current = 'Мой профиль'"
        />
        <PopsoMenuItem
          :extend="sidebar"
          :color="current === 'Список задач' ? 'fill-primary' : 'fill-black'"
          :class="current === 'Список задач' ? 'text-primary' : 'text-black'"
          icon="tasks"
          title="Список задач"
          @click="current = 'Список задач'"
        />
        <PopsoMenuItem
          :extend="sidebar"
          :color="current === 'Статистика' ? 'fill-primary' : 'fill-black'"
          :class="current === 'Статистика' ? 'text-primary' : 'text-black'"
          icon="stats"
          title="Статистика"
          @click="current = 'Статистика'"
        />
      </div>
      <div class="flex flex-col h-full items-center justify-end gap-4">
        <PopsoMenuItem
          :extend="sidebar"
          color="fill-exit"
          class="text-exit"
          icon="exit"
          title="Выйти"
          @click="navigateTo('/')"
        />
      </div>
    </div>
    <div class="flex flex-col py-16 pl-16 pr-8 bg-dashboard w-full h-full">
      <Transition name="current" mode="out-in">
        <div :key="current" class="flex flex-col gap-8">
          <h1 class="md:text-2xl font-medium">
            {{ current }}
          </h1>
          <div v-show="current === 'Мой профиль'">
            <PopsoDashboardProfile />
          </div>
          <div v-show="current === 'Список задач'">
          
          </div>
          <div v-show="current === 'Статистика'">
          
          </div>
        </div>
      </Transition>
    </div>
  </div>
</template>


<script setup>

definePageMeta({
  middleware: 'auth'
})

const sidebar = ref(false)

const current = ref("Мой профиль")

const arrow = ref(null)


function toggle() {
  sidebar.value = !sidebar.value
  if (sidebar.value) {
    arrow.value.classList.add("-scale-100")
    arrow.value.classList.remove("scale-100")
  } else {
    arrow.value.classList.remove("-scale-100")
    arrow.value.classList.add("scale-100")
  }
}

</script>


<style scoped>
.logo-enter-active, .logo-leave-active {
  transition: all 0.15s ease-in-out;
}
.logo-enter-from, .logo-leave-to {
  opacity: 0;
}

.current-enter-active, .current-leave-active {
  transition: all 0.15s ease-in-out;
}
.current-enter-from, .logo-leave-to {
  opacity: 0;
}
</style>
