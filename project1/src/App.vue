<template>
<!--根路径应该只被一个元素包裹起来。不能多个元素并列。-->
<div class='app'>
  <h3>{{ msg }}</h3>
  <Vheader></Vheader>
  <Vcontent></Vcontent>
  <Vfooter></Vfooter>
</div>

</template>

<script>
// 1、首先需要引入，后缀名.vue可以不写（在一个父组件中引入子组件）
import Vheader from './components/Vheader'
import Vcontent from './components/Vcontent.vue'
import Vfooter from './components/Vfooter'

// 页面的业务逻辑，所有页面的DOM操作都会放到script里
// 这个组件里面的这个对象，起就是Vue.component("Vheader", {})这里的这个对象
export default {
  // name这个属性代指的就是app这个名字，没有什么太多的意义，对于测试有用。
  name: 'App',
  data(){
    return {
      msg: 'hello 组件',
    }
  },
  methods:{

  },
  computed:{},
  // 2、引入了以后需要挂载，挂载了以后就可以使用了。
  components:{
    // 这样直接写一个Vheader，相当于Vheader:Vheader，即如果key=value，就可以直接这么写。
    Vheader,
    Vcontent,
    Vfooter
  },
}
</script>

<style>

</style>



