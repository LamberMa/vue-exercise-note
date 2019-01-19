<template>
  <div class='hi'>
    {{ message }}
  </div>
</template>

<script>
export default {
  data () {
    return { 
        message: "hello maxiaoyu!"
    }
  }
}
</script>

<style>
.hi {
    color: red;
    font-size: 22px;
}
</style>