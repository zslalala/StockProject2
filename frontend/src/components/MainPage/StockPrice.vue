<template>
  <div>
    <el-input placeholder="请输入内容" v-model="stockid">
      <template slot="prepend">Http://</template>
    </el-input>
    <el-input placeholder="请输入内容" v-model="startdate">
      <template slot="prepend">起始日期</template>
    </el-input>
    <el-input placeholder="请输入内容" v-model="enddate">
      <template slot="prepend">终止日期</template>
    </el-input>
    <el-button type="primary" round @click="showstock">查看</el-button>
  </div>
</template>

<script>
export default {
  name: "StockPrice",
  data(){
    return{
      stockid:'',
      startdate:'',
      enddate:'',
    }
  },
  methods:{
    showstock(){
      this.$axios.post('http://127.0.0.1:8000/backend/showstock',{
        stockid:this.stockid,
        startdate:this.startdate,
        enddate:this.enddate,
      })
    }
  }
}
</script>

<style scoped>
.el-input{
  width:300px;
  margin-right: 20px;
}
</style>
