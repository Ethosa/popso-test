<template>
  <div class="flex flex-col rounded-lg bg-white">
    <VuePlotly
      :data="data"
      :layout="layout"
      :config="config"
      :display-mode-bar="false"
    />
    <div class="hidden md:flex gap-4 px-12 py-4">
      <PopsoButton
        :outlined="true"
        @click="randomizeData()"
      >
        Случайные данные
      </PopsoButton>
      <PopsoButton
        :outlined="true"
        @click="addData()"
      >
        Добавить данные
      </PopsoButton>
      <PopsoButton
        :outlined="true"
        @click="removeData()"
      >
        Удалить данные
      </PopsoButton>
      <PopsoButton
        :outlined="true"
        @click="expandData()"
      >
        Увеличить кол-во данных
      </PopsoButton>
      <PopsoButton
        :outlined="true"
        @click="squeezeData()"
      >
        Уменьшить кол-во данных
      </PopsoButton>
    </div>
    <div class="flex md:hidden w-full px-4 py-4 ">
      <PopsoButton
        :outlined="true"
        class="w-full"
        @click="toggleFilter()"
      >
        Фильтры
      </PopsoButton>
    </div>
    <Transition name="bottom-sheet">
      <div
        v-show="bottomFilter"
        :key="bottomFilter"
        class="flex flex-col items-center px-4 py-8 gap-12 rounded-t-xl bg-white fixed bottom-0 left-0 right-0"
      >
        <div class="flex justify-between w-full">
          <h1 class="text-3xl">
            Фильтры
          </h1>
          <img src="/public/close_menu_mobile.svg" class="w-6 select-none cursor-pointer" @click="toggleFilter()">
        </div>
        <div class="flex flex-col gap-4 w-fit">
          <PopsoCheckbox v-model:checked="filterRandomize">
            Случайные данные
          </PopsoCheckbox>
          <PopsoCheckbox v-model:checked="filterAdd">
            Добавить данные
          </PopsoCheckbox>
          <PopsoCheckbox v-model:checked="filterRemove">
            Удалить данные
          </PopsoCheckbox>
          <PopsoCheckbox v-model:checked="filterExpand">
            Увеличить кол-во данных
          </PopsoCheckbox>
          <PopsoCheckbox v-model:checked="filterSqueeze">
            Уменьшить кол-во данных
          </PopsoCheckbox>
        </div>
        <div class="flex flex-col items-center gap-2 justify-end min-h-48">
          <PopsoButton
            @click="applyFilters()"
          >
            Применить фильтры
          </PopsoButton>
          <label
            class="text-primary hover:text-primary-hover active:text-primary-active"
            @click="clearFilters()"
          >
            Сбросить фильтры
          </label>
        </div>
      </div>
    </Transition>
  </div>
</template>


<script setup>
import { VuePlotly } from 'vue3-plotly'

const props = defineProps({
  filters: false
})

// chart data
const data = ref([])
const layout = ref({title: "Статистика"})
const config = ref({
  scrollZoom: false,
  editable: false,
  displayModeBar: false,
  locale: 'ru',
  responsive: true,
})


// filters
const filterRandomize = ref()
const filterAdd = ref()
const filterRemove = ref()
const filterExpand = ref()
const filterSqueeze = ref()


const bottomFilter = ref(false)


/**
 * clear filters from filter menu
 */
function clearFilters() {
  filterRandomize.value = false
  filterAdd.value = false
  filterRemove.value = false
  filterExpand.value = false
  filterSqueeze.value = false
  toggleFilter()
}


/**
 * Apply filters from filter menu
 */
function applyFilters() {
  console.log(filterRandomize.value)
  if (filterRandomize.value) {
    randomizeData()
  }
  if (filterAdd.value) {
    addData()
  }
  if (filterRemove.value) {
    removeData()
  }
  if (filterExpand.value) {
    expandData()
  }
  if (filterSqueeze.value) {
    squeezeData()
  }
  clearFilters()
}


/**
 * just random :p
 * @param {number} from start number
 * @param {number} to end number
 */
function random(from, to) {
  return Math.floor(Math.random() * (to - from) + from)
}


/**
 * Add point to every line
 */
function expandData() {
  data.value.forEach(i => {
    i['x'] = i['x'].concat(`Дата ${i['x'].length}`)
    i['y'] = i['y'].concat(random(-60, 60))
  })
  data.value = [...data.value]
}


/**
 * Remove last point from every line
 */
function squeezeData() {
  data.value.forEach(i => {
    if (i['x'].length > 0) {
      i['x'] = i['x'].slice(0, i['x'].length-1)
      i['y'] = i['y'].slice(0, i['y'].length-1)
    }
  })
  data.value = [...data.value]
}


/**
 * Toggles mobile filter menu
 */
function toggleFilter() {
  bottomFilter.value = !bottomFilter.value
}


/**
 * Add new line
 */
function addData() {
  const pointsCount = random(2, 10)
  let newData = {
    x: [],
    y: [],
    type:"scatter",
    name: `data_${random(0, 100000)}`,
    line: {shape: 'spline'}
  }
  if (data.value.length === 0) {
    for (let point = 0; point < pointsCount; point++) {
      newData['x'].push(`Дата ${newData['x'].length}`)
    }
  } else {
    newData['x'] = data.value[data.value.length-1]['x']
  }
  for (let point = 0; point < newData['x'].length; point++) {
    newData['y'].push(random(-60, 60))
  }
  data.value.push(newData)
  data.value = [...data.value]
}


/**
 * Remove last line
 */
function removeData() {
  if (data.value.length > 0) {
    data.value.pop()
    data.value = [...data.value]
  }
}


/**
 * Deletes all lines and generate it randomly
 */
function randomizeData() {
  data.value = []
  const dataSize = random(1, 5)
  for (let index = 0; index < dataSize; index++) {
    addData()
  }
}


// generate random chart
onMounted(() => {
  randomizeData()
})

</script>


<style scoped>
.bottom-sheet-enter-active, .bottom-sheet-leave-active {
  transition: all 0.05s ease-in-out;
}
.bottom-sheet-enter-from, .bottom-sheet-leave-to {
  opacity: 0;
  transform: translateY(-110%);
}
</style>
