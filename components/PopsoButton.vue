<template>
  <button
    class="px-2 md:px-4 py-2 rounded-lg cursor-pointer select-none duration-150 flex justify-center items-center border-[1px] border-black/70 hover:border-primary-hover active:border-primary-active bg-transparent text-black/70 hover:text-primary-hover active:text-primary-active"
    @click="$emit('clicked')"
    v-if="props.outlined"
  >
      <slot></slot>
  </button>
  <button
    class="px-16 py-2 rounded-lg cursor-pointer select-none duration-150 flex text-white justify-center items-center bg-primary hover:bg-primary-hover active:bg-primary-active"
    @click="$emit('clicked')"
    v-else
  >
      <slot></slot>
  </button>
</template>

<script setup>

const props = defineProps({
  outlined: false
})

const emits = defineEmits(['clicked'])

</script>
