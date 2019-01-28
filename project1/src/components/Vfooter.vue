<template>
<!--根路径应该只被一个元素包裹起来。不能多个元素并列。-->
<div class='app'>
  <header class="footer">
      我是页脚部分
  </header>
</div>
</template>

<script>
// 页面的业务逻辑，所有页面的DOM操作都会放到script里
// 这个组件里面的这个对象，起就是Vue.component("Vheader", {})这里的这个对象
export default {
  // name这个属性代指的就是app这个名字，没有什么太多的意义，对于测试有用。
  name: 'Vfooter',
  data(){
    return {
    }
  },
  methods:{

  },
  computed:{}
}
</script>

<style>

</style>