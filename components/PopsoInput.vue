<template>
  <input
    :placeholder="props.placeholder"
    class="bg-transparent outline-none border-[1px] rounded-lg px-4 py-2 "
    v-model="value"
    :type="props.type"
  >
</template>


<script setup>

const props = defineProps({
  placeholder: String,
  type: String
})

const value = defineModel('value')

</script>
