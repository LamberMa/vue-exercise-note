<template>
<!--根路径应该只被一个元素包裹起来。不能多个元素并列。-->
<div class='app'>
  <header class="nav">
      导航栏
  </header>
</div>
</template>

<script>
// 页面的业务逻辑，所有页面的DOM操作都会放到script里
// 这个组件里面的这个对象，起就是Vue.component("Vheader", {})这里的这个对象
export default {
  // name这个属性代指的就是app这个名字，没有什么太多的意义，对于测试有用。
  name: 'Vheader',
  // data一定是个函数，return一个是返回一个对象
  data(){
    return {
      msg: 'hello 组件',
    }
  },
  methods:{

  },
  computed:{}
}
</script>

<style scoped>
/* scoped注入，表示将当前的样式属性只对当前的样式结构起作用，与其他组件没有任何关系。
 * 这样就降低了组件的耦合度。
 */

</style>