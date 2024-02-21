<template>
  <button
    class="px-16 py-2 rounded-lg cursor-pointer select-none duration-150 flex text-white justify-center items-center bg-primary hover:bg-primary-hover active:bg-primary-active"
    @click="$emit('clicked')"
  >
      <slot></slot>
  </button>
</template>

<script setup>

const emits = defineEmits(['clicked'])

</script>
