<template>
  <div class="flex flex-col bg-white rounded-lg p-8 mb-8">
    <div class="flex pb-2 opacity-60 px-2">
      <div class="w-5/6">Задача</div>
      <div class="w-1/6">Статус</div>
    </div>
    <div class="flex flex-col gap-2">
      <div v-for="i in tasks" v-bind:key="i">
        <div class="flex items-center border-t-[1px] border-exit/25 pt-2 px-2">
          <div class="w-5/6 h-full">
            {{ i['title'] }}
          </div>
          <div class="w-1/6">
            <div
              class="flex items-center cursor-pointer justify-center border-[2px] min-w-6 min-h-6 w-fit"
              @click="i['completed'] = !i['completed']"
            >
              <img v-show="i['completed']" src="/public/check.svg">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import axios from "axios"


const JSON_PLACEHOLDER_API_URL = "https://jsonplaceholder.typicode.com/todos"

const tasks = ref([])

onMounted(async () => {
  const {data} = await axios.get(JSON_PLACEHOLDER_API_URL)
  tasks.value = data.slice(Math.random() * 10, Math.random() * (100 - 10) + 10)
})
</script>
