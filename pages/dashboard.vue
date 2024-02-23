<template>
  <div class="relative flex flex-col md:flex-row w-screen h-screen overflow-x-hidden bg-dashboard">
    <!-- navigation desktop -->
    <div
      class="hidden md:flex flex-col h-screen bg-white max-h-screen fixed px-12 py-6 items-center gap-24 transition-all duration-150"
    >
      <Transition name="logo" mode="out-in">
        <div :key="sidebar">
          <img class="h-12" v-show="sidebar" src="/public/popso_first_letter.svg">
          <img class="h-12" v-show="!sidebar" src="/public/popso.svg">
        </div>
      </Transition>
      <div
        class="absolute -right-8 top-2 w-16 h-16 bg-white drop-shadow-lg cursor-pointer select-none flex justify-center items-center rounded-full"
        @click="toggle()"
      >
        <img ref="arrow" src="/public/arrow_back.svg" class="scale-100 duration-150">
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
    <!-- navigation mobile -->
    <div class="sticky top-0 z-10 flex md:hidden gap-4 w-full bg-white p-4">
      <img class="cursor-pointer select-none" src="/public/mobile_menu.svg" @click="toggleMobile()">
      <img class="h-6 select-none" src="/public/popso.svg">
    </div>
    <div
      :class="`flex flex-col py-8 md:py-16 pl-4 ${!sidebar ? 'md:pl-96' : 'md:pl-64'} pr-4 md:pr-8 w-full h-full`"
    >
      <Transition name="current" mode="out-in">
        <div :key="current" class="flex flex-col gap-4 md:gap-8">
          <h1 class="text-3xl md:text-2xl font-medium">
            {{ current }}
          </h1>
          <div v-show="current === 'Мой профиль'">
            <PopsoDashboardProfile />
          </div>
          <div v-show="current === 'Список задач'">
            <PopsoDashboardTasks />
          </div>
          <div v-show="current === 'Статистика'">
            <PopsoDashboardStats />
          </div>
        </div>
      </Transition>
    </div>
    <!-- sidebar mobile -->
    <Transition name="sidebar" mode="out-in">
      <div :key="sidebarMobile" class="fixed md:hidden z-20">
        <div v-show="sidebarMobile" class="fixed flex flex-col gap-4 w-3/4 drop-shadow-lg h-screen bg-white p-6">
          <img class="fixed top-4 left-4 cursor-pointer select-none h-6" src="/public/close_menu_mobile.svg" @click="toggleMobile()">
          <div class="flex flex-col items-center gap-4 pt-12">
            <PopsoMenuItem
              :extend="sidebar"
              :color="current === 'Мой профиль' ? 'fill-primary' : 'fill-black'"
              :class="current === 'Мой профиль' ? 'text-primary' : 'text-black'"
              icon="work"
              title="Мой профиль"
              @click="current = 'Мой профиль'; toggleMobile()"
            />
            <PopsoMenuItem
              :extend="sidebar"
              :color="current === 'Список задач' ? 'fill-primary' : 'fill-black'"
              :class="current === 'Список задач' ? 'text-primary' : 'text-black'"
              icon="tasks"
              title="Список задач"
              @click="current = 'Список задач'; toggleMobile()"
            />
            <PopsoMenuItem
              :extend="sidebar"
              :color="current === 'Статистика' ? 'fill-primary' : 'fill-black'"
              :class="current === 'Статистика' ? 'text-primary' : 'text-black'"
              icon="stats"
              title="Статистика"
              @click="current = 'Статистика'; toggleMobile()"
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
      </div>
    </Transition>
  </div>
</template>


<script setup>

definePageMeta({
  middleware: 'auth'
})

const sidebar = ref(false)
const sidebarMobile = ref(false)
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


function toggleMobile() {
  sidebarMobile.value = !sidebarMobile.value
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
.current-enter-from, .current-leave-to {
  opacity: 0;
  z-index: 0;
}

.sidebar-enter-active, .sidebar-leave-active {
  transition: all 0.05s ease-in-out;
}
.sidebar-enter-from, .sidebar-leave-to {
  opacity: 0;
  transform: translateX(-110%);
}
</style>
