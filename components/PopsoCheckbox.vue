<template>
  <label class="flex gap-4" @click="checked = !checked">
    <div class="flex justify-center items-center bg-transparent min-w-6 min-h-6 border-[2px] md:border-[1px]">
      <img v-show="checked" src="/public/check.svg">
    </div>
    <slot></slot>
  </label>
</template>


<script setup>
const checked = defineModel('checked')
</script>
