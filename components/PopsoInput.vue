<template>
  <div>
    <div v-if="props.flat">
      <label class="text-exit">
        {{ props.placeholder }}
      </label>
      <input
        :class="`peer w-full bg-transparent outline-none border-b-[1px] pb-1 ` + (props.error ? 'border-red-500' : 'border-exit')"
        v-model="value"
        :type="props.type"
      >
      <label class="md:text-sm text-red-500 min-h-10">
        {{ props.error }}
      </label>
    </div>
    <div v-else>
      <input
        :placeholder="props.placeholder"
        class="peer w-full bg-transparent outline-none border-[1px] rounded-lg px-4 py-2 "
        v-model="value"
        :type="props.type"
      >
      <label v-show="props.error" class="md:text-sm text-red-500">
        {{ props.error }}
      </label>
    </div>
  </div>
</template>


<script setup>

const props = defineProps({
  placeholder: String,
  type: String,
  error: String,
  flat: Boolean,
})

const value = defineModel('value')

</script>
